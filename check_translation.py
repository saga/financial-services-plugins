import os

# 读取plugins目录下的所有.md文件
plugins_files = []
for root, dirs, files in os.walk('plugins'):
    for file in files:
        if file.endswith('.md'):
            full_path = os.path.join(root, file)
            relative_path = full_path.replace('plugins/', '', 1)
            plugins_files.append(relative_path)

# 读取中文版目录下的所有.md文件
zh_files = []
for root, dirs, files in os.walk('中文版/plugins'):
    for file in files:
        if file.endswith('.md'):
            full_path = os.path.join(root, file)
            relative_path = full_path.replace('中文版/plugins/', '', 1)
            zh_files.append(relative_path)

# 找出缺失的
missing = [f for f in plugins_files if f not in zh_files]
extra = [f for f in zh_files if f not in plugins_files]

print(f'plugins文件数: {len(plugins_files)}')
print(f'中文版文件数: {len(zh_files)}')
print(f'缺失数: {len(missing)}')
print(f'多余数: {len(extra)}')
print('---')
print('前10个缺失文件:')
for f in missing[:10]:
    print(f'  {f}')
print('---')
print('检查特定文件:')
test_file = 'agent-plugins/earnings-reviewer/agents/earnings-reviewer.md'
print(f'  {test_file} 在plugins: {test_file in plugins_files}')
print(f'  {test_file} 在zh: {test_file in zh_files}')
print(f'  {test_file} 在missing: {test_file in missing}')
