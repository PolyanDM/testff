import pytest
from playwright.sync_api import expect
class TestLogin:
    @pytest.mark.smoke
    def test_successful_login(self, page):
            page.goto('https://kover.ru/cabinet/')
            page.locator('input[type="text"]').fill('dm.polianskov@kokoc.tech')
            page.locator('input[type="password"]').fill('dm.polianskov')
            page.get_by_role('button', name='Войти').click()
            expect(page.get_by_text("dm.polianskov@kokoc.tech")).to_be_visible(timeout=10000)
            print("Успешная авторизация")

    @pytest.mark.smoke
    def test_failed_login(self, page):
            page.goto('https://kover.ru/cabinet/')
            page.locator('input[type="text"]').fill('dm.polianskov@kokoc.tech')
            page.locator('input[type="password"]').fill('wrongpassword')
            page.get_by_role('button', name='Войти').click()
            error_message = page.get_by_text('Неправильный логин или пароль')
            expect(error_message).to_be_visible(timeout=10000)
            print("Не удалось авторизоваться!")