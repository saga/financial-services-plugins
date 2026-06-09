#!/usr/bin/env python3
import json

with open('/Users/saga/code-repos/financial-services-plugins/missing_appendix_list.json', 'r') as f:
    data = json.load(f)

missing = [m for m in data['missing_files'] if m.get('status') == '缺失附录']

# Prefer SKILL.md and command files
priority = []
for m in missing:
    fp = m['file_path']
    if 'SKILL.md' in fp or '/commands/' in fp:
        priority.append(m)
    elif '/skills/' in fp and 'references/' not in fp:
        priority.append(m)

others = [m for m in missing if m not in priority]

print(f'Total missing: {len(missing)}')
print(f'Priority (SKILL/commands): {len(priority)}')
print(f'Others: {len(others)}')
print()
print('Top 15 priority files:')
for i, m in enumerate(priority[:15]):
    print(f'  {i+1}. {m["full_path"]}')
print()
print('Top 10 other files:')
for i, m in enumerate(others[:10]):
    print(f'  {i+1}. {m["full_path"]}')