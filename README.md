# Playwright 爬蟲 Starter 專案

這是一個使用 [Playwright](https://playwright.dev/python/) 的 Python 爬蟲起始專案，適合用來快速建立自動化瀏覽器任務，例如擷取網頁截圖、資料爬取等。

## 📁 專案結構

```
playwright-starter/
├── .venv/                # 虛擬環境資料夾
├── example.py            # 範例爬蟲腳本
├── example.png           # 執行後產生的截圖
├── requirements.txt      # 相依套件清單
└── README.md             # 專案說明文件
```

## 🚀 快速開始

### 1. 建立虛擬環境並啟用

```bash
uv venv
source .venv/bin/activate
```

### 2. 安裝相依套件

```bash
uv pip install -r requirements.txt
playwright install
```

### 3. 執行範例腳本

```bash
python example.py
```

執行後會開啟瀏覽器，前往 `https://example.com`，等待 2 秒後擷取畫面並儲存為 `example.png`。

## 📦 安裝新套件

若需額外安裝套件，例如：

```bash
uv pip install beautifulsoup4
```

安裝後記得更新 `requirements.txt`：

```bash
uv pip freeze > requirements.txt
```

## 🧠 延伸應用建議

- 搭配 `BeautifulSoup` 或 `lxml` 做 HTML 資料解析
- 使用 `page.locator()` 或 `page.query_selector()` 擷取特定元素
- 加入錯誤處理與重試機制
- 將爬蟲邏輯模組化，方便維護與擴充

## 📝 備註

- 本專案使用 [uv](https://github.com/astral-sh/uv) 作為套件與虛擬環境管理工具，速度更快也更簡潔。
- 若你尚未安裝 `uv`，可先執行：

  ```bash
  curl -Ls https://astral.sh/uv/install.sh | sh
  ```
