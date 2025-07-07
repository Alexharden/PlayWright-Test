# SauceDemo Login Automation Test

本專案為針對 [https://www.saucedemo.com/](https://www.saucedemo.com/) 網站的登入流程撰寫的自動化測試，使用 Playwright + pytest 實作。

## 📦 使用技術與套件

- Python 3.11
- Playwright
- Pytest
- Pytest-html（測試報告套件）

## 🛠️ 環境建置方式

```bash
# 建立虛擬環境（可選）
python -m venv venv
source venv/bin/activate  # Windows：venv\Scripts\activate

# 安裝套件
pip install -r requirements.txt

# 安裝 Playwright 驅動
playwright install
