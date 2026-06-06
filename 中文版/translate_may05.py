import os
import subprocess
import time
import sys

PROMPT = """You are an expert financial translator. I will provide you with a markdown file's text.
Task:
1. Translate the entire content into Chinese with elegant, professional financial terminology.
2. Preserve exact formatting (markdown tables, bullet points, headers, YAML frontmatter, lists).
3. Append a block at the very end starting with '> **💡 Appendix: 领域知识小贴士**' explaining the core financial concepts mentioned in the text for an absolute beginner (using engaging, easy to understand language).
4. OUTPUT ONLY THE FINAL FILE CONTENT. DO NOT wrap your output in ```markdown ... ``` blocks. DO NOT add any intro or outro.

File content to translate:
"""

# Load translation list
translation_list = []
with open('/tmp/translation_list.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        src_rel, dst_rel = line.split('|')
        translation_list.append((src_rel, dst_rel))

plugins_root = '../financial-services-plugins/plugins'
chinese_root = '../financial-services-plugins/中文版'

total = len(translation_list)
print(f"Starting translation of {total} files.", flush=True)

success_count = 0
error_count = 0
skip_count = 0

for i, (src_rel, dst_rel) in enumerate(translation_list):
    src_full = os.path.join(plugins_root, src_rel)
    dst_full = os.path.join(chinese_root, dst_rel)

    # Skip if target already exists and has content
    if os.path.exists(dst_full) and os.path.getsize(dst_full) > 10:
        print(f"[{i+1}/{total}] Skipped (already exists): {dst_rel}", flush=True)
        skip_count += 1
        continue

    print(f"[{i+1}/{total}] Translating {src_rel} -> {dst_rel}...", flush=True)

    # Read source
    try:
        with open(src_full, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  -> Error reading source: {e}", flush=True)
        error_count += 1
        continue

    full_prompt = PROMPT + content

    try:
        result = subprocess.run(
            ['claude', '-p', full_prompt],
            capture_output=True,
            text=True,
            check=True
        )

        output_text = result.stdout.strip()
        # Clean up accidental markdown code block wrappers
        if output_text.startswith("```markdown"):
            output_text = output_text[11:]
        elif output_text.startswith("```"):
            output_text = output_text[3:]
        if output_text.endswith("```"):
            output_text = output_text[:-3]

        # Ensure directory exists
        os.makedirs(os.path.dirname(dst_full), exist_ok=True)

        with open(dst_full, 'w', encoding='utf-8') as f:
            f.write(output_text.strip() + "\n")

        print(f"  -> Success!", flush=True)
        success_count += 1

        time.sleep(1)  # slight rate limit
    except subprocess.CalledProcessError as e:
        print(f"  -> Error: claude command failed (exit {e.returncode})", flush=True)
        print(f"  -> Stderr: {e.stderr[:200]}", flush=True)
        error_count += 1
        time.sleep(5)
    except Exception as e:
        print(f"  -> Error: {str(e)}", flush=True)
        error_count += 1
        time.sleep(5)

print(f"\nTranslation complete! Success: {success_count}, Skipped: {skip_count}, Errors: {error_count}", flush=True)
