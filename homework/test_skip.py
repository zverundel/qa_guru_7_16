"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[{'width': 3840, 'height': 2160}, {'width': 380, 'height': 844}])
def browser_opt(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_height = request.param['height']
    browser.config.window_width = request.param['width']


def test_github_desktop(browser_opt):
    if browser.config.window_width <= 390:
        pytest.skip("Мобильное разрешение")
    browser.open("/")
    browser.element('[href="/login"]').click()


def test_github_mobile(browser_opt):
    if browser.config.window_width > 390:
        pytest.skip("Десктопное разрешение")
    browser.open("/")
    browser.element('[class="flex-1 flex-order-2 text-right"] [aria-label="Toggle navigation"]').click()
    browser.element('[href="/login"]').click()