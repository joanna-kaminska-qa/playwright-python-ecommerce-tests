# conftest.py
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from datetime import datetime

# ----------------- Fixture Playwright Page -----------------
@pytest.fixture
def page():
    """
    Fixture dostarcza gotową stronę Playwright dla testów.
    Po teście przeglądarka zostaje zamknięta.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True jeśli nie chcesz widzieć przeglądarki
        page = browser.new_page()
        yield page
        browser.close()


# ----------------- Hook do screenshotów przy błędzie -----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook do generowania screenshotów przy failed testach i dodawania ich do raportu HTML.
    """
    outcome = yield
    report = outcome.get_result()

    # tylko przy porażce
    if report.failed:
        page = item.funcargs.get("page")
        if page:
            # katalog na screenshoty
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            # unikalna nazwa pliku z timestampem
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = screenshots_dir / f"{item.name}_{timestamp}.png"

            # zapis screenshotu
            page.screenshot(path=str(screenshot_path))
            print(f"Screenshot zapisany w: {screenshot_path}")

            # dodanie do raportu HTML
            try:
                from pytest_html import extras
                if hasattr(report, "extras"):
                    report.extras.append(extras.png(str(screenshot_path)))
                else:
                    report.extra = getattr(report, "extra", []) + [extras.png(str(screenshot_path))]
            except ImportError:
                # jeśli brak pytest-html, po prostu ignorujemy
                pass
