# DECISIONS.md - 架構重大決策記錄 (ADR)

本文檔記錄 `hello-python` 專案自初始建立至今所有關鍵架構、安全與工程決策（Architecture Decision Records）。

---

## 目錄
- [ADR-001: 隱私優先之 Local Git 作者身分綁定](#adr-001-隱私優先之-local-git-作者身分綁定)
- [ADR-002: 審前揭露與逐步授權之協調機制](#adr-002-審前揭露與逐步授權之協調機制)
- [ADR-003: 演進式功能擴充與 Git Diff 白話教學設計](#adr-003-演進式功能擴充與-git-diff-白話教學設計)
- [ADR-004: 遠端儲存庫原子化多版本推送與同步驗證機制](#adr-004-遠端儲存庫原子化多版本推送與同步驗證機制)
- [ADR-005: 導入 src-layout 模組化與根目錄相容啟動層](#adr-005-導入-src-layout-模組化與根目錄相容啟動層)
- [ADR-006: 對話溯源庫 (Conversations Archive) 與 PEP 621 規範](#adr-006-對話溯源庫-conversations-archive-與-pep-621-規範)

---

### ADR-001: 隱私優先之 Local Git 作者身分綁定
* **狀態**：已採納 (Accepted)
* **日期**：2026-10-04
* **背景**：開發者電腦全域 Git 設定為學號與校園信箱（`411383025@gms.ndhu.edu.tw`）。在建立公開開源儲存庫時，若直接提交將導致個人隱私洩漏。
* **決策**：在專案初始化時，使用 `git config --local` 專屬綁定：
  - `user.name = "chinkunlim"`
  - `user.email = "chinkunlim@users.noreply.github.com"`
* **後果**：
  - 優點：完全隱蔽本機真實學號與個資，杜絕網路爬蟲蒐集。
  - 代價：僅對本專案生效，其他專案需各別留意或設定。

---

### ADR-002: 審前揭露與逐步授權之協調機制
* **狀態**：已採納 (Accepted)
* **日期**：2026-10-04
* **背景**：AI 代理若擁有全自動執行權限，容易產生非預期的破壞性寫入或遠端推播。
* **決策**：落實「審前揭露 $\rightarrow$ 人工核可 $\rightarrow$ 執行 $\rightarrow$ 成果複檢」四步迴路。凡寫入硬碟、Git 變更、遠端推送指令，均須事先揭露指令內容並經使用者同意。
* **後果**：
  - 優點：極高安全性與開發者掌控感，完全杜絕誤刪或非預期副作用。
  - 代價：互動回合數增加，需要使用者適時確認。

---

### ADR-003: 演進式功能擴充與 Git Diff 白話教學設計
* **狀態**：已採納 (Accepted)
* **日期**：2026-10-04
* **背景**：從最陽春的 Hello 程式，逐步導入動態日期 (v2) 與巴斯卡三角形 (v3)，需要建立開發者對版本差異的比對直覺。
* **決策**：每次功能迭代皆執行 `git diff`，並由 AI 代理以白話闡釋紅色減號（舊程式行刪除／置換）與綠色加號（新邏輯加入）的本質差異。
* **後果**：
  - 優點：將程式開發與工程素養教學深度整合，強化版本控制透明度。
  - 代價：輸出報告篇幅較長。

---

### ADR-004: 遠端儲存庫原子化多版本推送與同步驗證機制
* **狀態**：已採納 (Accepted)
* **日期**：2026-10-04
* **背景**：本機已完成 v1、v2、v3 三筆歷史提交，需建立遠端 GitHub 公開儲存庫並推播。
* **決策**：
  - 使用 GitHub CLI：`gh repo create hello-python --public --source=. --remote=origin --push`。
  - 登入 Token 失效時，遵循安全性協議由使用者自主登入。
  - 推送完成後強制以 `git log --oneline` 與 `git status --short --branch` 驗證本地與遠端雙向對齊（`HEAD -> main, origin/main`）。
* **後果**：
  - 優點：完整保留開發軌跡，無壓扁歷史（Squash），狀態驗證確實。
  - 代價：需要 GitHub CLI 網路與鑑權就緒。

---

### ADR-005: 導入 src-layout 模組化與根目錄相容啟動層
* **狀態**：已採納 (Accepted)
* **日期**：2026-10-08
* **背景**：原本專案為單檔 `hello.py`。為了符合現代化 Python 封裝、可測試性與工業標準，需提升為模組化套件，但仍需照顧使用者習慣直接執行 `python3 hello.py` 的直覺體驗。
* **決策**：
  - 建立標準套件目錄 `src/hello_python/`，包含純演算法模組 `core.py` 與命令列入口 `cli.py`。
  - 根目錄保留 `hello.py` 作為相容轉接器（Compatibility Shim），直接委派呼叫 `src/hello_python/cli.py`。
* **後果**：
  - 優點：結構符合現代 Python 標準，支援單元測試與依賴打包，同時保留既有命令執行習慣。
  - 代價：專案目錄檔案層級略微增加。

---

### ADR-006: 對話溯源庫 (Conversations Archive) 與 PEP 621 規範
* **狀態**：已採納 (Accepted)
* **日期**：2026-10-08
* **背景**：AI 協同開發過程的對話脈絡（意圖、權衡、錯誤糾正）為專案極其寶貴的智慧資產，傳統程式庫往往丟失此上下文。
* **決策**：
  - 建立 `conversations/raw/` 與 `conversations/summaries/`，完整以 Markdown 歸檔歷次開發會話。
  - 採用 PEP 621 現代標準之 `pyproject.toml` 取代舊式 `setup.py` 或單純 `requirements.txt`，並相容現代打包工具 `uv` 與標準 `pip`。
* **後果**：
  - 優點：專案具備完整之歷史可解釋性（Explainability）與 AI 友好度（Agent-readable），環境標準化。
  - 代價：需持續維護對話歸檔與摘要檔。
