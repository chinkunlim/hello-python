# TOOLS.md - 開發工具與指令介面規範

本文件彙整專案所使用的工具鏈、命令規範及自動化任務。

---

## 1. 核心工具鏈 (Toolchain)

| 工具 | 角色 | 呼叫方式 |
| :--- | :--- | :--- |
| **Python** | 執行環境 (Runtime) | `python3` (3.10+) |
| **Git** | 版本控制 | `git` |
| **GitHub CLI** | 遠端雲端儲存庫管理 | `gh` |
| **Makefile** | 本地建置與任務編排 | `make <target>` |
| **unittest** | 單元測試框架 | `python3 -m unittest` |

---

## 2. 常用命令速查

### 執行與測試
```bash
# 執行應用程式
make run
# 或
python3 hello.py

# 執行測試套件
make test
# 或
PYTHONPATH=src python3 -m unittest discover tests

# 語法與編譯校驗
make check
```

### Git 與版本控制
```bash
# 檢視目前狀態
git status --short --branch

# 查看精簡提交歷史
git log --oneline

# 檢視差異
git diff
```
