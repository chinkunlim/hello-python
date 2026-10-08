# hello-python

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-chinkunlim%2Fhello--python-green.svg)](https://github.com/chinkunlim/hello-python)
[![Code Style: Standard](https://img.shields.io/badge/Architecture-src--layout-orange.svg)](#專案目錄架構)

> 一個從極簡腳本演進至現代化工程體系的 Python 示範專案。包含身分隱私防護、動態日期運算、巴斯卡三角形視覺化演算法，以及完整的 AI 對話歷史溯源庫。

---

## 🌟 專案特色

1. **核心業務功能**：
   - **自我介紹**：以 GitHub 帳號名 `chinkunlim` 輸出問候，絕不洩漏個人真實隱私。
   - **動態日期**：精確解析並顯示執行當日日期。
   - **巴斯卡三角形**：以今日日期的日數（`dd`）為階數，動態計算並於終端機優雅置中輸出巴斯卡三角形。
2. **現代化工程架構 (v4)**：
   - 採現代標準 **`src-layout`** 模組化設計（`src/hello_python/`），同時在根目錄提供向後相容啟動腳本 [hello.py](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/hello.py)。
   - **PEP 621** 標準配置 [pyproject.toml](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/pyproject.toml)，相容 `uv` 與標準 `pip`。
   - 內建單元測試套件（`tests/`）與 GitHub Actions 自動化 CI 檢查。
3. **對話溯源庫 (Conversations Traceability)**：
   - 完整備份歷次開發對話於 [conversations/raw/](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/conversations/raw/)。
   - 每段對話均配有獨立摘要文檔於 [conversations/summaries/](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/conversations/summaries/)。
4. **完備的治理文檔**：
   - 包含 [AGENTS.md](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/AGENTS.md)、[CHANGELOG.md](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/CHANGELOG.md)、[WORKFLOW_GUIDE.md](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/WORKFLOW_GUIDE.md)、[DECISIONS.md](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/DECISIONS.md) 與 [KNOWN_ISSUES.md](file:///Users/limchinkun/Desktop/AI%20vibe%20coding/hello-python/KNOWN_ISSUES.md)。

---

## 🚀 快速上手 (Quick Start)

### 1. 執行主程式
本專案支援兩種啟動方式：

```bash
# 方式 A：直接執行根目錄相容腳本（最簡便）
python3 hello.py

# 方式 B：透過模組化套件入口執行
PYTHONPATH=src python3 -m hello_python.cli
```

### 2. 執行單元測試
```bash
# 執行所有單元測試
python3 -m unittest discover tests

# 或透過 Makefile
make test
```

### 3. 一鍵指令 (Makefile)
專案提供標準指令集：
- `make run`：執行主程式。
- `make test`：執行測試套件。
- `make check`：執行語法與結構檢查。
- `make audit`：執行 Antigravity 專案合規自動化審計。
- `make help`：查看所有指令說明。

---

## 📂 專案目錄架構

```text
hello-python/
├── .python-version              # 鎖定 Python Runtime
├── pyproject.toml               # PEP 621 主要依賴聲明與專案元數據
├── .gitignore                   # Git 排除清單 (.venv, __pycache__ 等)
├── .env.example                 # 環境變數範本
├── Makefile                     # 一鍵常用指令集 (run, test, check, audit, sync)
├── LICENSE                      # MIT 開源授權條款
├── audit_project.py             # Antigravity 專案合規性自動化審計腳本
│
├── .vscode/                     # VS Code 開發環境配置
│   ├── settings.json            # 解譯器與格式化器設定
│   └── launch.json              # 偵錯啟動組態
├── .cursorrules                 # AI 協同開發規則指引
│
├── .github/                     # GitHub 自動化治理
│   ├── workflows/ci.yml         # CI 自動化測試流水線
│   ├── CONTRIBUTING.md          # 貢獻與開發指南
│   └── SECURITY.md              # 資安通報政策
│
├── README.md                    # 本專案入口文件
├── AGENTS.md                    # AI 代理協作規範與職責
├── WORKFLOW_GUIDE.md            # 標準作業程序 (SOP)
├── CHANGELOG.md                 # 完整版本演進紀錄 (v1 ~ v4.1)
├── DECISIONS.md                 # 架構重大決策記錄 (ADR)
├── KNOWN_ISSUES.md              # 已知問題與踩坑指南
│
├── src/                         # 應用程式核心原始碼目錄 (src-layout)
│   └── hello_python/
│       ├── __init__.py
│       ├── core.py              # 問候、日期與巴斯卡三角形純函式邏輯
│       └── cli.py               # 命令列入口
├── hello.py                     # 根目錄向後相容入口腳本
│
├── docs/                        # 深度架構文檔
│   ├── ARCHITECTURE.md          # 系統架構圖與設計
│   ├── TOOLS.md                 # 工具集與指令介面規範
│   ├── CONTEXT.md               # 系統全域背景 (供 Agent 吸收)
│   ├── DEPLOYMENT.md            # 環境安裝與部署手冊
│   └── PROMPT_TEMPLATES.md      # 提示詞範本與調教手冊
│
├── tests/                       # 單元測試套件
│   ├── __init__.py
│   └── test_core.py             # 核心計算邏輯測試
│
├── evals/                       # 提示詞評估集與輸出基準
│   └── README.md
│
└── conversations/               # 專案對話溯源儲存庫
    ├── raw/                     # 歷次開發對話完整原始 Markdown 記錄
    │   ├── 001_env_inspection.md
    │   ├── 002_initial_setup_v1.md
    │   ├── 003_date_feature_v2.md
    │   ├── 004_pascal_triangle_v3.md
    │   ├── 005_github_repo_push.md
    │   ├── 006_project_restructuring_v4.md
    │   └── 007_project_alignment_audit.md
    └── summaries/               # 每段對話對應的獨立摘要 Markdown 記錄
        ├── 001_env_inspection_summary.md
        ├── 002_initial_setup_v1_summary.md
        ├── 003_date_feature_v2_summary.md
        ├── 004_pascal_triangle_v3_summary.md
        ├── 005_github_repo_push_summary.md
        ├── 006_project_restructuring_v4_summary.md
        └── 007_project_alignment_audit_summary.md
```

---

## 📈 版本演進簡介

* **v1.0.0**：建立首版問候腳本，設定 local Git 作者（`chinkunlim`），避免揭露個人隱私。
* **v2.0.0**：新增今日日期顯示，實施 `git diff` 差異檢視與白話教學。
* **v3.0.0**：新增以系統日數（`dd`）為階數之巴斯卡三角形，並推播至遠端 GitHub。
* **v4.0.0**：全專案重構為現代 `src-layout`，導入對話溯源庫、PEP 621 規格、單元測試與六大治理文檔。
* **v4.1.0**：嚴格遵循 02 指引完成專案結構對齊、雙模 Makefile 工具鏈升級、提示詞手冊補齊與 100% 合規自動化審計。

---

## 📄 開源授權 (License)

本專案採用 [MIT License](LICENSE) 條款開源釋出。
