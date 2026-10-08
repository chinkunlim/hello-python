# 貢獻指南 (Contributing Guide)

感謝您對 `hello-python` 的關注！

## 參與貢獻流程
1. Fork 本儲存庫並在本地複製。
2. 建立新功能分支：`git checkout -b feature/my-feature`。
3. 遵循模組化規範，核心計算放於 `src/hello_python/`，並於 `tests/` 撰寫對應單元測試。
4. 執行本地檢查：
   ```bash
   make check
   make test
   ```
5. 提交變更並遵循 Conventional Commits 或專案既有 `vX：說明` 風格。
6. 發起 Pull Request 並描述您的變更。

## 隱私守則
- 請勿提交包含個人私密個資或真實姓名之程式碼與設定。
