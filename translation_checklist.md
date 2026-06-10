# 中文翻译缺失文件清单

> 生成日期: 2026-06-11
> 对比范围: upstream (anthropics/financial-services) vs 中文版/

---

## Git change 记录

### 中文版目录
- **修改文件**: 0
- **新增文件**: 325（upstream 删除了整个中文版，本地重新创建）

### 中文版以外
| 文件 | 变更 | 大小 | 说明 |
|------|------|------|------|
| `missing_appendix_list.json` | 新增 | 668行 | 附录缺失统计 |
| `plugins_comparison_checklist.md` | 新增 | 461行 | 插件对比清单 |
| `check_appendix.py` | 新增 | 60行 | 附录检查脚本 |
| `check_translation.py` | 新增 | 38行 | 翻译检查脚本 |
| `generate_checklist.py` | 新增 | 166行 | 清单生成脚本 |
| `AGENTS.md` | 新增 | 25行 | 项目说明 |
| `.claude/scheduled_tasks.json` | 新增 | 14行 | 定时任务 |
| `.trae/skills/finance-appendix-adder/SKILL.md` | 新增 | 218行 | 附录添加技能 |
| `plugins_missing_files.json` | 新增 | 43行 | 缺失文件JSON |
| `plugins_missing_files.csv` | 新增 | 4行 | 缺失文件CSV |
| `translation.pid` | 新增 | 1行 | 进程锁 |

---

## 翻译缺失清单（已过滤代码文件）

> 已排除: `.yaml` `.json` `.py` `.sh` `.ps1` `.mjs`
> .md 文件全部覆盖(0缺失)

| # | 文件 | 状态 |
|---|------|------|
| 1 | `README.md` | 缺失中文版 |
| 2 | `CLAUDE.md` | 缺失中文版 |
| 3 | `plugins/agent-plugins/pitch-agent/skills/dcf-model/requirements.txt` | 缺失中文版 |

---

## 结论

排除代码/配置文件后，**仅剩 3 个文件需要翻译**，全部为非 yaml/json/py/sh/ps1/mjs 类型。