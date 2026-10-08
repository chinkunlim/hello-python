# KNOWN_ISSUES.md - 已知問題與踩坑避障指南

本指南彙整 `hello-python` 專案在環境建置、指令執行、版本控制與跨平台操作時之已知邊界問題與最佳避坑解法。

---

## 1. 環境與解譯器相關 (Environment & Runtime)

### 1.1 macOS 系統找不到 `python` 指令
* **現象**：在終端機輸入 `python hello.py` 時回報 `zsh: command not found: python`。
* **原因**：現代 macOS 與官方 Python 3 安裝包預設僅建立 `python3` 執行檔，不再建立無後綴的 `python` 軟連結（避免與舊版 macOS 內建之 Python 2 衝突）。
* **解法**：
  - **推薦**：直接使用標準指令 `python3 hello.py`。
  - **方案二**：在 `~/.zshrc` 加入別名：
    ```bash
    echo "alias python='python3'" >> ~/.zshrc && source ~/.zshrc
    ```

### 1.2 Python 模組搜尋路徑 (PYTHONPATH) 匯入問題
* **現象**：若直接在子目錄執行 `python3 src/hello_python/cli.py`，可能會遭遇 `ModuleNotFoundError: No module named 'hello_python'`。
* **原因**：Python 預設僅將當前執行的腳本所在目錄放入 `sys.path[0]`。
* **解法**：
  - 在專案根目錄執行向後相容入口：`python3 hello.py`（內部已處理 `sys.path` 注入）。
  - 或透過模組化方式啟動：`PYTHONPATH=src python3 -m hello_python.cli`。
  - 或透過 `pip install -e .` 將專案以可編輯模式安裝。

---

## 2. 版本控制與遠端連線 (Git & GitHub CLI)

### 2.1 GitHub CLI (`gh`) 憑證過期失效
* **現象**：執行 `gh repo create` 或查詢時出現 `The token in default is invalid` 或 `Failed to log in to github.com`。
* **原因**：OAuth 憑證或個人存取權杖（PAT）過期。
* **解法**：
  - 於本地終端機重新進行身分鑑權：
    ```bash
    gh auth login -h github.com
    ```
  - 選擇瀏覽器登入（Web Browser）依循引導授權即可恢復正常。

### 2.2 沙盒執行環境阻擋外網存取
* **現象**：在受限沙盒或安全終端機中執行推播指令時，回報 `error connecting to api.github.com`。
* **原因**：安全防護機制預設阻斷非必要的連網行為。
* **解法**：針對需要存取外部網路之命令（如推播、安裝外部依賴），明確提請授權並啟用受信任之網路連線模式。

---

## 3. 業務演算法與終端機呈現 (Algorithm & UI)

### 3.1 月底大日數（dd > 20）巴斯卡三角形換行破版
* **現象**：當系統日期處於月底（如 28、29、30、31 號）時，巴斯卡三角形階數極高，底層數字增長至數十萬甚至數千萬，導致在窄螢幕終端機出現自動折行現象。
* **原因**：終端機標準視窗寬度通常為 80 ~ 120 欄位，大數字置中格式化需要更大寬度空間。
* **解法**：
  - 將終端機視窗最大化或切換為全螢幕檢視。
  - 在核心程式 `core.py` 中已支援自訂階數參數（`generate_pascals_triangle(num_rows)`），開發或測試時可傳入適當數字（如 4 ~ 10）以保持視覺美觀。

---

## 4. 權限與跨平台相容性 (Cross-Platform)

### 4.1 Makefile 在 Windows 環境缺乏原生 make 支援
* **現象**：Windows 預設命令提示字元無法直接執行 `make run` 或 `make test`。
* **原因**：Windows 未內建 GNU Make。
* **解法**：
  - Windows 使用者可透過 PowerShell 直接執行等價指令：
    ```powershell
    python -m unittest discover tests
    ```
  - 或透過 Scoop / Chocolatey 安裝：`choco install make`。
