# CONTEXT.md - 專案全域背景與 AI 脈絡指引

> 專供 AI 代理人或新進協作者在零上下文情況下快速理解專案的起源、演進路徑與核心規範。

---

## 1. 專案由來 (Project Origin)
本專案源自於在 macOS 環境下探索現代 AI 協同編程（Vibe Coding / Pair Programming）的示範實踐。從零建立目錄開始，經過以下五個關鍵演進里程碑：
1. **001_env_inspection**：檢驗作業系統、Python 3.14、Git 與 GitHub CLI。
2. **002_initial_setup_v1**：建立 `hello.py`、隱私作者綁定、分支命名為 `main`、提交第一版。
3. **003_date_feature_v2**：引入日期、Git Diff 白話教學、提交第二版。
4. **004_pascal_triangle_v3**：引入當日天數巴斯卡三角形、置中排版演算法、提交第三版。
5. **005_github_repo_push**：建立公開 GitHub repo `chinkunlim/hello-python`，原子化推送三筆提交並對齊。
6. **006_project_restructuring_v4**：啟動 `/goal /plan /grill-me` 進行工業級工程重構、建置對話溯源庫與全套治理文檔。

---

## 2. 核心邊界與鐵律 (Invariants)
1. **隱私至上**：作者資訊永遠為 `chinkunlim <chinkunlim@users.noreply.github.com>`。
2. **審前揭露**：有副作用的變更必須事前告知指令並徵求核可。
3. **可追溯性**：每次關鍵會話均有對應 raw 與 summary 紀錄於 `conversations/`。
4. **零破壞性向後相容**：根目錄的 `hello.py` 永遠可直接執行，輸出與歷史行為保持一致。
