import json
import csv
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
if os.path.exists('中文版/plugins'):
    for root, dirs, files in os.walk('中文版/plugins'):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                relative_path = full_path.replace('中文版/plugins/', '', 1)
                zh_files.append(relative_path)

# 读取managed-agent-cookbooks目录下的所有.md文件
mac_files = []
if os.path.exists('managed-agent-cookbooks'):
    for root, dirs, files in os.walk('managed-agent-cookbooks'):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                relative_path = full_path.replace('managed-agent-cookbooks/', '', 1)
                mac_files.append(relative_path)

# 读取中文版managed-agent-cookbooks目录下的所有.md文件
zh_mac_files = []
if os.path.exists('中文版/managed-agent-cookbooks'):
    for root, dirs, files in os.walk('中文版/managed-agent-cookbooks'):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                relative_path = full_path.replace('中文版/managed-agent-cookbooks/', '', 1)
                zh_mac_files.append(relative_path)

# 找出缺失的plugins文件
missing_plugins = [f for f in plugins_files if f not in zh_files]

# 找出缺失的managed-agent-cookbooks文件
missing_mac = [f for f in mac_files if f not in zh_mac_files]

# 找出中文版多余的文件
extra_zh = [f for f in zh_files if f not in plugins_files]
extra_zh_mac = [f for f in zh_mac_files if f not in mac_files]

# 生成JSON格式
data = {
    'summary': {
        'plugins_total': len(plugins_files),
        'zh_plugins_total': len(zh_files),
        'mac_total': len(mac_files),
        'zh_mac_total': len(zh_mac_files),
        'missing_plugins': len(missing_plugins),
        'missing_mac': len(missing_mac),
        'extra_zh': len(extra_zh),
        'extra_zh_mac': len(extra_zh_mac),
        'plugins_translation_complete': len(missing_plugins) == 0,
        'mac_translation_complete': len(missing_mac) == 0
    },
    'missing_plugins_files': [],
    'missing_mac_files': [],
    'extra_zh_files': [],
    'extra_zh_mac_files': []
}

for file_path in missing_plugins:
    parts = file_path.split('/')
    category = parts[0] if parts else 'other'
    subcategory = parts[1] if len(parts) > 1 else ''
    filename = parts[-1] if parts else ''
    
    data['missing_plugins_files'].append({
        'file_path': file_path,
        'category': category,
        'subcategory': subcategory,
        'filename': filename,
        'type': 'plugins缺失',
        'status': '待翻译'
    })

for file_path in missing_mac:
    parts = file_path.split('/')
    category = parts[0] if parts else 'other'
    subcategory = parts[1] if len(parts) > 1 else ''
    filename = parts[-1] if parts else ''
    
    data['missing_mac_files'].append({
        'file_path': file_path,
        'category': category,
        'subcategory': subcategory,
        'filename': filename,
        'type': 'managed-agent-cookbooks缺失',
        'status': '待翻译'
    })

for file_path in extra_zh:
    parts = file_path.split('/')
    category = parts[0] if parts else 'other'
    subcategory = parts[1] if len(parts) > 1 else ''
    filename = parts[-1] if parts else ''
    
    data['extra_zh_files'].append({
        'file_path': file_path,
        'category': category,
        'subcategory': subcategory,
        'filename': filename,
        'type': '中文版多余',
        'status': '需确认'
    })

for file_path in extra_zh_mac:
    parts = file_path.split('/')
    category = parts[0] if parts else 'other'
    subcategory = parts[1] if len(parts) > 1 else ''
    filename = parts[-1] if parts else ''
    
    data['extra_zh_mac_files'].append({
        'file_path': file_path,
        'category': category,
        'subcategory': subcategory,
        'filename': filename,
        'type': '中文版managed-agent-cookbooks多余',
        'status': '需确认'
    })

# 保存为JSON
with open('plugins_missing_files.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 保存为CSV
with open('plugins_missing_files.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['file_path', 'category', 'subcategory', 'filename', 'type', 'status'])
    
    for item in data['missing_plugins_files']:
        writer.writerow([item['file_path'], item['category'], item['subcategory'], item['filename'], item['type'], item['status']])
    
    for item in data['missing_mac_files']:
        writer.writerow([item['file_path'], item['category'], item['subcategory'], item['filename'], item['type'], item['status']])
    
    for item in data['extra_zh_files']:
        writer.writerow([item['file_path'], item['category'], item['subcategory'], item['filename'], item['type'], item['status']])
    
    for item in data['extra_zh_mac_files']:
        writer.writerow([item['file_path'], item['category'], item['subcategory'], item['filename'], item['type'], item['status']])

print(f'已更新JSON文件: plugins_missing_files.json')
print(f'已更新CSV文件: plugins_missing_files.csv')
print(f'---')
print(f'plugins目录: {len(plugins_files)}个.md文件')
print(f'中文版plugins: {len(zh_files)}个.md文件')
print(f'plugins缺失: {len(missing_plugins)}个')
print(f'---')
print(f'managed-agent-cookbooks目录: {len(mac_files)}个.md文件')
print(f'中文版managed-agent-cookbooks: {len(zh_mac_files)}个.md文件')
print(f'managed-agent-cookbooks缺失: {len(missing_mac)}个')
print(f'---')
print(f'中文版多余文件: {len(extra_zh) + len(extra_zh_mac)}个')
