# 提示詞範本與調教手冊 (PROMPT_TEMPLATES.md)

本文件收錄 `hello-python` 專案中標準 AI 代理與自動化流程之提示詞範本（Prompt Templates），協助開發者與各協作角色維持一致的高品質輸出。

---

## 1. 架構對齊與合規審計 (Alignment & Compliance Audit)

```markdown
/goal /plan /grill-me
嚴格遵守 desktop/checking/02_PROJECT_ALIGN_CHECK_GUIDE.md
對整個專案進行結構對齊、文檔整併與合規審計：
1. 歷史對話溯源與強制脫敏備份至 conversations/
2. 消除 docs/ 子目錄與根目錄的重複同名檔案
3. 工具鏈雙模相容性升級 (Makefile, uv, python3)
4. 執行 python3 audit_project.py 確保 100% 通過
```

---

## 2. 演算法擴展與核心邏輯重構 (Algorithm Extension)

```markdown
角色：Coder Agent (agent-coder)
任務：在 src/hello_python/core.py 中新增 [演算法名稱] 實作。
規範要求：
1. 遵循 PEP 8 與 PEP 484，完整標註型別與 Docstrings。
2. 在 tests/ 中編寫對應之單元測試，邊界值涵蓋率 100%。
3. 保持純標準函式庫相容性，向後相容至 Python 3.10+。
4. 嚴格遵守 AGENTS.md 隱私邊界，禁止洩漏姓名或校園 Email。
```

---

## 3. 測試基準與 Evals 驗收 (Evals Verification)

```markdown
角色：Auditor Agent (agent-audit)
任務：針對 `hello-python` 執行 Evals 輸出基準驗證。
輸入參數：
- 日期模擬值：2026-10-08
- 預期巴斯卡三角形層數：8
驗證指標：
- 終端機格式化輸出對齊
- 邊界條件處理（非正整數、空值）
- 輸出無異常除錯代碼或未處理例外
```
