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

# Find all markdown files in skills/
files_to_process = []
for root, dirs, files in os.walk('plugins/vertical-plugins'):
    if '/skills' in root or root.endswith('/skills'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                files_to_process.append(filepath)

files_to_process.sort()

print(f"Found {len(files_to_process)} files to process sequentially.")

success_count = 0
error_count = 0

for i, filepath in enumerate(files_to_process):
    target = f"中文版May06/{filepath}"
    os.makedirs(os.path.dirname(target), exist_ok=True)

    if os.path.exists(target) and os.path.getsize(target) > 10:
        print(f"[{i+1}/{len(files_to_process)}] Skipped (already exists): {filepath}")
        continue

    print(f"[{i+1}/{len(files_to_process)}] Translating {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    full_prompt = PROMPT + content

    try:
        # Run claude -p
        result = subprocess.run(
            ['claude', '-p', full_prompt],
            capture_output=True,
            text=True,
            check=True
        )

        output_text = result.stdout.strip()
        # Clean up if the model accidentally wrapped it in markdown tags
        if output_text.startswith("```markdown"):
            output_text = output_text[11:]
        elif output_text.startswith("```"):
            output_text = output_text[3:]
        if output_text.endswith("```"):
            output_text = output_text[:-3]

        with open(target, 'w', encoding='utf-8') as f:
            f.write(output_text.strip() + "\n")

        print(f"  -> Success!")
        success_count += 1

        # Sleep to avoid rate limits
        time.sleep(2)

    except subprocess.CalledProcessError as e:
        print(f"  -> Error: claude command failed with exit code {e.returncode}")
        print(f"  -> Stderr: {e.stderr[:200]}...")
        error_count += 1
        time.sleep(5)  # Back off on error
    except Exception as e:
        print(f"  -> Error: {str(e)}")
        error_count += 1
        time.sleep(5)

print(f"Done! Successfully translated {success_count} files. Errors: {error_count}")
