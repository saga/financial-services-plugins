# Plugins Comparison Checklist

**Source:** `plugins/`  
**Target:** `中文版May06/`  
**Comparison Date:** 2026-05-10

---

## Summary

| Category | Total Items | Missing Items | Status |
|----------|-------------|---------------|--------|
| agent-plugins | 10 | 6 entirely missing, 4 partially | ⚠️ |
| partner-built | 2 | 2 entirely missing | ❌ |
| vertical-plugins | 7 | 4 entirely missing, 3 partially | ⚠️ |
| **Total** | **19** | **12 entirely missing, 7 partially** | |

---

## ❌ Entire Directories Missing (Critical)

These complete plugin directories exist in `plugins/` but are **completely absent** from `中文版May06/`:

### agent-plugins
- [ ] **earnings-reviewer** - Entire plugin missing
- [ ] **gl-reconciler** - Entire plugin missing
- [ ] **model-builder** - Entire plugin missing
- [ ] **month-end-closer** - Entire plugin missing
- [ ] **pitch-agent** - Entire plugin missing
- [ ] **statement-auditor** - Entire plugin missing

### partner-built
- [ ] **lseg** - Entire plugin missing (LSEG partner integration)
- [ ] **spglobal** - Entire plugin missing (S&P Global partner integration)

### vertical-plugins
- [ ] **equity-research** - Entire plugin missing
- [ ] **fund-admin** - Entire plugin missing
- [ ] **private-equity** - Entire plugin missing
- [ ] **wealth-management** - Entire plugin missing

---

## ⚠️ Partially Present (Incomplete)

These plugins exist in both directories but `plugins/` has additional files/skills not found in `中文版May06/`:

### agent-plugins

#### kyc-screener
Both exist but compare files to find missing components:
- [ ] Compare `agent-plugins/kyc-screener/` structure

#### market-researcher
Both exist but compare files to find missing components:
- [ ] Compare `agent-plugins/market-researcher/` structure

#### meeting-prep-agent
Both exist but compare files to find missing components:
- [ ] Compare `agent-plugins/meeting-prep-agent/` structure

#### valuation-reviewer
Both exist but compare files to find missing components:
- [ ] Compare `agent-plugins/valuation-reviewer/` structure

### vertical-plugins

#### financial-analysis
Both exist but compare files to find missing components:
- [ ] Compare `vertical-plugins/financial-analysis/` structure

#### investment-banking
Both exist but compare files to find missing components:
- [ ] Compare `vertical-plugins/investment-banking/` structure

#### operations
Both exist but compare files to find missing components:
- [ ] Compare `vertical-plugins/operations/` structure

---

## 📋 Action Items

1. **High Priority:** Copy the 12 entirely missing plugin directories from `plugins/` to `中文版May06/`
   - Use: `cp -r ../financial-services-plugins/plugins/agent-plugins/earnings-reviewer ../financial-services-plugins/中文版May06/agent-plugins/`
   - Repeat for all 12 missing directories

2. **Medium Priority:** For the 7 partially-missing plugins, run a detailed diff to identify and copy missing files:
   - Example: `diff -r plugins/agent-plugins/kyc-screener 中文版May06/agent-plugins/kyc-screener`

3. **Verification:** Re-run this comparison after syncing to confirm `中文版May06` is fully up to date.

---

## Notes

- Total unique items in `plugins/`: 497
- Total unique items in `中文版May06/`: 495
- Items missing from `中文版May06`: 436
- Many missing items are due to entire plugin directories being absent
- Both directories share the same top-level structure: `agent-plugins/`, `partner-built/`, `vertical-plugins/`
