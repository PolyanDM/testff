import pytest
from playwright.sync_api import expect
from playwright.sync_api import Page
import os
from pytest_html import extras

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get('page')
        if isinstance(page, Page):
            os.makedirs('screenshots', exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            if not hasattr(report, 'extras'):
                report.extras = []
            report.extras.append(extras.image(screenshot_path))

class TestLogin:
    @pytest.mark.smoke
    def test_successful_login(self, page):
            page.goto('https://kover.ru/cabinet/')
            page.locator('input[type="text"]').fill('dm.polianskov@kokoc.tech')
            page.locator('input[type="password"]').fill('dm.polianskov')
            page.get_by_role('button', name='Войти').click()
            expect(page.get_by_text("dm.polianskov@kokoc.tech")).to_be_visible(timeout=10000)
            print("Успешная авторизация")
        # Скриншот после успешного входа
            os.makedirs('screenshots', exist_ok=True)
            page.screenshot(path='screenshots/success_login.png')

    @pytest.mark.smoke
    def test_failed_login(self, page):
            page.goto('https://kover.ru/cabinet/')
            page.locator('input[type="text"]').fill('dm.polianskov@kokoc.tech')
            page.locator('input[type="password"]').fill('wrongpassword')
            page.get_by_role('button', name='Войти').click()
            error_message = page.get_by_text('Неправильный логин или пароль')
            expect(error_message).to_be_visible(timeout=10000)
            print("Не удалось авторизоваться!")

            # Скриншот после неудачного входа
            os.makedirs('screenshots', exist_ok=True)
            page.screenshot(path='screenshots/failed_login.png')