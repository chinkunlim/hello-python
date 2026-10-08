# DEPLOYMENT.md - 本地建置與執行部署指南

本文件引導如何在全新機器或本機環境下載、配置並執行 `hello-python`。

---

## 1. 系統需求 (Prerequisites)
- **作業系統**：macOS、Linux 或 Windows。
- **Python**：Python 3.10 或以上版本（推薦 Python 3.12 ~ 3.14）。
- **Git**：2.30 以上版本。

---

## 2. 下載與安裝 (Installation)

### 2.1 複製儲存庫
```bash
git clone https://github.com/chinkunlim/hello-python.git
cd hello-python
```

### 2.2 建立虛擬環境 (可選但推薦)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2.3 安裝開發依賴
```bash
pip install -e ".[dev]"
```

---

## 3. 執行與驗證 (Verification)
```bash
# 執行應用程式
python3 hello.py

# 執行自動化測試
PYTHONPATH=src python3 -m unittest discover tests
```
