import pytest
from playwright.sync_api import expect

@pytest.mark.form
def test_dynamic_loading_wait_for_selector(page):
    page.goto('https://kover.ru/product/6493807/')
    page.locator('a[name="Заказать демонстрацию домой"]').click()
    dropdown = page.get_by_role('button', id='headlessui-listbox-button-_r_2_')
    dropdown.select_option('2')
    page.locator('input[type="text"]').fill('Test')
    page.locator('input[type="tel"]').fill('9999999999')
    page.get_by_role('button', name='Заказать демонстрацию').click()

    # Ждём появления элемента (возвращаемое значение не сохраняем)
    page.wait_for_selector('button', name='Понятно', state='visible')

    # Создаём локатор для проверки
    result = page.locator('button', name='Понятно')
    expect(result).to_have_text('Понятно')
    print("Форма отправлена")