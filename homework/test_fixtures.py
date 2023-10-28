import pytest
from selene import browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture
def browser_url():
    browser.config.base_url = 'https://github.com'


@pytest.fixture
def desktop_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920


@pytest.fixture
def mobile_size():
    browser.config.window_height = 1196
    browser.config.window_width = 400


def test_github_desktop(browser_url, desktop_size):
    browser.open('/')
    browser.element('[href="/login"]').click()


def test_github_mobile(browser_url, mobile_size):
    browser.open('/')
    browser.element('[class="flex-1 flex-order-2 text-right"] [aria-label="Toggle navigation"]').click()
    browser.element('[href="/login"]').click()