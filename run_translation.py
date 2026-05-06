import os
import subprocess
import concurrent.futures

PROMPT = """You are an expert financial translator. I will provide you with a markdown file's text.
Task:
1. Translate the entire content into Chinese with elegant, professional financial terminology.
2. Preserve exact formatting (markdown tables, bullet points, headers, YAML frontmatter, lists).
3. Append a block at the very end starting with '> **💡 Appendix: 领域知识小贴士**' explaining the core financial concepts mentioned in the text for an absolute beginner (using engaging, easy to understand language).
4. OUTPUT ONLY THE FINAL FILE CONTENT. DO NOT wrap your output in ```markdown ... ``` blocks. DO NOT add any intro or outro.

File content to translate:
"""

def process_file(filepath):
    target = f"中文版May06/{filepath}"
    os.makedirs(os.path.dirname(target), exist_ok=True)
    if os.path.exists(target) and os.path.getsize(target) > 10:
        return f"Skipped {filepath}"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    full_prompt = PROMPT + content

    print(f"Translating {filepath}...")
    try:
        # Run claude -p
        result = subprocess.run(
            ['claude', '-p', full_prompt],
            capture_output=True,
            text=True,
            check=True
        )

        # Write the output
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

        return f"Successfully translated {filepath}"
    except Exception as e:
        return f"Error translating {filepath}: {str(e)}"

# Find all markdown files in skills/
files_to_process = []
for root, dirs, files in os.walk('plugins/vertical-plugins'):
    if '/skills' in root or root.endswith('/skills'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                files_to_process.append(filepath)

print(f"Found {len(files_to_process)} files to translate in the skills/ folders.")

# Process in parallel (max 10 workers to respect potential rate limits/CPU)
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(process_file, files_to_process))

for r in results:
    if "Error" in r:
        print(r)
print("All files processed!")
