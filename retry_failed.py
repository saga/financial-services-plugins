import os
import subprocess
import time

PROMPT = """You are an expert financial translator. I will provide you with a markdown file's text.
Task:
1. Translate the entire content into Chinese with elegant, professional financial terminology.
2. Preserve exact formatting (markdown tables, bullet points, headers, YAML frontmatter, lists).
3. Append a block at the very end starting with '> **💡 Appendix: 领域知识小贴士**' explaining the core financial concepts mentioned in the text for an absolute beginner (using engaging, easy to understand language).
4. OUTPUT ONLY THE FINAL FILE CONTENT. DO NOT wrap your output in ```markdown ... ``` blocks. DO NOT add any intro or outro.

File content to translate:
"""

plugins_root = '../financial-services-plugins/plugins'
chinese_root = '../financial-services-plugins/中文版'

# Load retry list
retry_list = []
with open('/tmp/retry_list.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        src_rel, dst_rel = line.split('|')
        retry_list.append((src_rel, dst_rel))

total = len(retry_list)
print(f"Retrying {total} failed files...")

success = 0
failed = []

for i, (src_rel, dst_rel) in enumerate(retry_list):
    src_full = os.path.join(plugins_root, src_rel)
    dst_full = os.path.join(chinese_root, dst_rel)

    print(f"[{i+1}/{total}] {src_rel} -> {dst_rel}")

    # If already translated after partial success, skip
    if os.path.exists(dst_full) and os.path.getsize(dst_full) > 10:
        print("  -> Already exists, skipping")
        success += 1
        continue

    # Read source
    try:
        with open(src_full, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  -> ERROR reading: {e}")
        failed.append(src_rel)
        continue

    full_prompt = PROMPT + content

    # Try up to 3 times with increasing delays
    for attempt in range(3):
        try:
            delay = 5 * (attempt + 1)
            print(f"  -> Attempt {attempt+1} (wait {delay}s)...")
            time.sleep(delay)

            result = subprocess.run(
                ['claude', '-p', full_prompt],
                capture_output=True,
                text=True,
                check=True,
                timeout=300  # 5 minutes for large files
            )

            output_text = result.stdout.strip()
            if output_text.startswith("```markdown"):
                output_text = output_text[11:]
            elif output_text.startswith("```"):
                output_text = output_text[3:]
            if output_text.endswith("```"):
                output_text = output_text[:-3]

            os.makedirs(os.path.dirname(dst_full), exist_ok=True)
            with open(dst_full, 'w', encoding='utf-8') as f:
                f.write(output_text.strip() + "\n")

            print("  -> SUCCESS!")
            success += 1
            break

        except subprocess.CalledProcessError as e:
            print(f"  -> Attempt {attempt+1} failed (exit {e.returncode})")
            if attempt == 2:
                print(f"  -> FAILED after 3 attempts")
                failed.append(src_rel)
        except Exception as e:
            print(f"  -> Exception: {e}")
            if attempt == 2:
                print(f"  -> FAILED after 3 attempts")
                failed.append(src_rel)

print(f"\n=== Retry Summary ===")
print(f"Successfully translated: {success}/{total}")
print(f"Still failed: {len(failed)}")
if failed:
    print("Failed files:")
    for f in failed:
        print(f"  - {f}")
