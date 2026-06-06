import os
import json

missing_appendix = []
total_files = 0
has_appendix = 0

# 遍历中文版目录下的所有.md文件
for root, dirs, files in os.walk('中文版'):
    for file in files:
        if file.endswith('.md'):
            total_files += 1
            full_path = os.path.join(root, file)
            relative_path = full_path.replace('中文版/', '', 1)
            
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查是否包含金融背景知识附录
                if '## Appendix: 金融背景知识' in content or '## 金融术语和知识解释' in content or '## 金融术语' in content:
                    has_appendix += 1
                else:
                    missing_appendix.append({
                        'file_path': relative_path,
                        'full_path': full_path,
                        'status': '缺失附录'
                    })
            except Exception as e:
                missing_appendix.append({
                    'file_path': relative_path,
                    'full_path': full_path,
                    'status': '读取错误: ' + str(e)
                })

# 生成JSON结果
result = {
    'summary': {
        'total_files': total_files,
        'has_appendix': has_appendix,
        'missing_appendix': len(missing_appendix),
        'appendix_coverage_rate': round(has_appendix / total_files * 100, 2) if total_files > 0 else 0
    },
    'missing_files': missing_appendix
}

# 保存为JSON
with open('missing_appendix_list.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('总文件数:', total_files)
print('有附录:', has_appendix)
print('缺失附录:', len(missing_appendix))
print('覆盖率:', result['summary']['appendix_coverage_rate'], '%')
print('---')
print('缺失附录的文件列表:')
for item in missing_appendix[:20]:
    print('  ', item['file_path'])
if len(missing_appendix) > 20:
    print('  ... 还有', len(missing_appendix) - 20, '个文件')
