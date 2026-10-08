# CHANGELOG.md - 版本演進歷史

本專案遵循語意化版本與演進式交付原則，記錄自專案初始建立迄今的所有重大變更。

---

## [v4.2.0] - 2026-10-08
### 完整對話獨立記錄庫匯出 (Export Completed Conversations)
- **獨立完整對話匯出**：建立 `conversations/completed/` 目錄，將專案歷程中所有完整對話（001 至 008）以一則對話一 Markdown 檔案的形式全數匯出。
- **純對話紀錄規範**：嚴格依使用者指示採純對話紀錄版，保留完整提問、工具調用歷程與執行輸出，不額外附帶摘要區塊。
- **對話溯源庫同步維護**：同步歸檔 `conversations/raw/008_export_completed_conversations.md` 與對應獨立摘要。
- **合規審計驗證**：通過 `python3 audit_project.py` 100% 合規檢核與單元測試。

## [v4.1.0] - 2026-10-08
### 結構對齊與合規審計 (Alignment & Compliance Audit)
- **架構規範嚴格對齊**：遵循 `02_PROJECT_ALIGN_CHECK_GUIDE.md` 規範完成 5 大標準步驟檢驗，防範同名冗餘檔案。
- **審計腳本納管**：於專案根目錄納管 `audit_project.py`，支援一鍵合規性檢核（`make audit` 或 `python3 audit_project.py`）。
- **工具鏈雙模升級**：升級 `Makefile` 涵蓋標準 target（`sync`, `test`, `dev`, `lint`, `audit`, `run`, `check`, `clean`），支援 `uv` 優先並提供原生 `python3` / `pytest` 優雅 fallback。
- **規格文檔齊備**：補齊 `docs/PROMPT_TEMPLATES.md`，並擴充 `evals/README.md` 評估維度與基準案例。
- **對話溯源庫補齊**：歸檔 `conversations/raw/007_project_alignment_audit.md` 及其獨立摘要。

## [v4.0.0] - 2026-10-08
### 重大架構升級 (Major Restructuring)
- **架構模組化**：導入標準 `src-layout` 架構，建立 `src/hello_python/` 套件：
  - `core.py`：將打招呼問候、日期解析與巴斯卡三角形生成演算法封裝為可重用、可測試之獨立純函式。
  - `cli.py`：提供標準命令列程式入口。
  - `hello.py`：根目錄保留向後相容層，確保既有 `python3 hello.py` 執行方式依然有效。
- **對話溯源庫 (Conversations Archive)**：
  - 新增 `conversations/raw/`：完整收錄自第 1 次環境檢測至本重構階段之原始對話與指令歷程。
  - 新增 `conversations/summaries/`：針對每次關鍵對話提煉核心目標、技術決策與成果摘要。
- **專案治理與合規文檔**：
  - 新增 `README.md`：專案核心說明書與快速啟動指南。
  - 新增 `AGENTS.md`：AI 代理協同角色、權限及審查通訊協定。
  - 新增 `WORKFLOW_GUIDE.md`：標準開發作業規範 (SOP) 與審查指引。
  - 新增 `DECISIONS.md`：記錄 ADR-001 至 ADR-006 之重大架構決策。
  - 新增 `KNOWN_ISSUES.md`：環境陷阱、指令相容性與踩坑避障手冊。
- **依賴管理與現代化工具鏈**：
  - 新增 `pyproject.toml`：符合 PEP 517 / PEP 621 之標準專案定義檔，宣告 Python >= 3.10、依賴與測試工具。
  - 新增 `Makefile`：整合 `run`、`test`、`lint` 等一鍵指令集。
  - 新增 `LICENSE`：正式採納 MIT 開源授權條款。
  - 新增 `.gitignore`、`.env.example`、`.vscode/` 及 `.cursorrules`。
- **自動化測試與 CI 流水線**：
  - 新增 `tests/test_core.py`：涵蓋問候語、日期取得、巴斯卡三角形動態矩陣生成與排版演算法之完整單元測試。
  - 新增 `.github/workflows/ci.yml`：建立 GitHub Actions 自動化測試工作流。

---

## [v3.0.0] - 2026-10-04 (Commit: `7a2a6a7`)
### 新增 (Added)
- **巴斯卡三角形動態繪製**：
  - 根據當前系統日期的天數（`dd`）動態計算巴斯卡三角形行數（執行當日為 10 月 4 日，產出 4 行）。
  - 實作每行元素置中演算法（`.center(rows * 4)`），提供優雅之終端機格式化對稱輸出。
- **差異教學與審查**：
  - 展示並白話解說 `git diff`，示範替換舊有列印行與新增演算法迴圈邏輯。

---

## [v2.0.0] - 2026-10-04 (Commit: `c4a0e2e`)
### 新增 (Added)
- **今日日期顯示功能**：
  - 引入 Python 標準函式庫 `datetime`，擴充輸出當前系統日期（`2026-10-04`）。
- **版本控制教學**：
  - 透過實際變更展示 `git diff`，向使用者白話解說綠色加號 (`+`) 與紅色減號 (`-`) 之版本控制核心意涵。

---

## [v1.0.0] - 2026-10-04 (Commit: `f9cfa75`)
### 初始建立 (Initial Setup)
- **初始程式碼**：
  - 建立極簡 Python 腳本 `hello.py`，印出以使用者 GitHub 帳號名 `chinkunlim` 為主體之自我介紹字串，保障真實隱私。
- **Git 版本控制初始化**：
  - 初始化本地 Git 儲存庫，主分支命名為 `main`。
  - 透過 `git config --local` 設定使用者名稱為 `chinkunlim`，作者信箱為 `chinkunlim@users.noreply.github.com`。
  - 完成專案首筆提交（訊息：「`v1：第一版`」）。

---

## [v0.1.0] - 2026-10-04
### 環境探測 (Environment Inspection)
- 唯讀檢測 macOS 本機開發環境。
- 確認 Python 3.14.4、Apple Git 2.50.1 與 Homebrew GitHub CLI (`gh`) 2.92.0 狀態。
- 確立「審前告知、授權執行、隱私保護、自主登入」之協作基準。
