from playwright.sync_api import sync_playwright, expect

def test_successful_login():
    with sync_playwright() as p:
        # 1. Запускаем браузер (в видимом режиме для наглядности)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 2. Переходим на страницу логина
        page.goto('https://kover.ru/cabinet/')

        # 3. Действия: заполняем форму
        page.locator('input[type="text"]').fill('dm.polianskov@kokoc.tech')
        page.locator('input[type="password"]').fill('dm.polianskov')
        page.get_by_role('button', name='Войти').click()
        page.wait_for_timeout(2000)

        # 4. Проверки (assertions)
        #    Проверяем, что сообщение об успехе видно
        expect(page.get_by_text("dm.polianskov@kokoc.tech")).to_be_visible()

        # 5. Закрываем браузер
        browser.close()
        print("Всё ок!")

def test_failed_login():
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto('https://kover.ru/cabinet/')

                # Вводим неправильный пароль
                page.locator('input[type="text"]').fill('dm.polianskov@kokoc.tech')
                page.locator('input[type="password"]').fill('wrongpassword')
                page.get_by_role('button', name='Войти').click()


                # Проверяем, что появилось сообщение об ошибке
                # Текст ошибки должен точно совпадать с тем, что на сайте
                error_message = page.get_by_text('Неправильный логин или пароль')
                expect(error_message).to_be_visible()


                browser.close()
                print("Не ок!")

if __name__ == "__main__":
    test_successful_login()
    test_failed_login()