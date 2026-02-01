# Playwright Python E-commerce Tests

Automated tests for a sample e-commerce website using **Playwright** with **Python** and **pytest**.  
Tests include login scenarios, validation of page URLs, and intentionally failing tests to demonstrate reporting and screenshot capturing.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.36-orange)
![pytest](https://img.shields.io/badge/pytest-9.0.2-green)
![pytest-html](https://img.shields.io/badge/pytest--html-4.2.0-blueviolet)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Status: Completed](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Project Structure
```
C:.
|   conftest.py
|   LICENSE
|   report.html
|   structure.txt
|   
+---.idea
|       .gitignore
|       checkstyle-idea.xml
|       misc.xml
|       modules.xml
|       projekt.iml
|       vcs.xml
|       workspace.xml
|       
+---.pytest_cache
|   |   .gitignore
|   |   CACHEDIR.TAG
|   |   README.md
|   |   
|   \---v
|       \---cache
|               lastfailed
|               nodeids
|               
+---pages
|   |   login_page.py
|   |   
|   \---__pycache__
|           login_page.cpython-314.pyc
|           
+---screenshots
|       test_intentionally_fail.png
|       test_intentionally_fail_2026-02-01_11-19-36.png
|       
+---tests
|   |   test_fail.py
|   |   test_first_run.py
|   |   test_login.py
|   |   test_login_parametrized.py
|   |   
|   \---__pycache__
|           test_fail.cpython-314-pytest-9.0.2.pyc
|           test_first_run.cpython-314-pytest-9.0.2.pyc
|           test_login.cpython-314-pytest-9.0.2.pyc
|           test_login_parametrized.cpython-314-pytest-9.0.2.pyc
|           
\---__pycache__
```
- `conftest.py` – konfiguracja pytest, w tym fixture `page` i screenshoty przy błędach
- `pages/` – Page Object Model, np. `login_page.py`
- `tests/` – testy automatyczne
- `screenshots/` – zrzuty ekranu z nieudanych testów
- `report.html` – raport HTML z ostatniego uruchomienia testów

---

## Requirements

- Python 3.14+
- [Playwright](https://playwright.dev/python/)
- pytest
- pytest-html

Install dependencies:

```bash
pip install -r requirements.txt
python -m playwright install
```
Tip: If you don't have requirements.txt, you can create it manually:
```
pytest
pytest-html
playwright
```
---

## Running Tests

Run all tests and generate an HTML report:

```bash
python -m pytest -v --html=report.html --self-contained-html
```
- Test results will appear in the terminal and in report.html
- Screenshots of failing tests are saved in the screenshots/ folder

## Example Tests
test_fail.py
```
def test_intentionally_fail(page):
login_page = LoginPage(page)
login_page.open()
login_page.login("standard_user", "secret_sauce")
assert page.url == "https://www.saucedemo.com/wrong_url"  # intentional fail
```
### Author

**Joanna Kamińska**  
GitHub: https://github.com/joanna-kaminska-qa

---

### Version History

| Version | Changes |
|---------|---------|
| **0.2** | README added, structure updated, TestContainers tests prepared |
| **0.1** | Initial upload |

---

### License

This project is licensed under the **MIT License**.  
See the LICENSE file for details.

### Acknowledgments
- [Python Official Documentation](https://docs.python.org/3/)
- [Playwright for Python Documentation](https://playwright.dev/python/docs/intro)
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [pytest-html Documentation](https://pytest-html.readthedocs.io/en/latest/)
- [Visual Studio Code](https://www.jetbrains.com/pycharm/)
- [Python Packaging and Virtual Environments](https://packaging.python.org/)
