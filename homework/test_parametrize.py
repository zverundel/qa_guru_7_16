import pytest
from selene import browser


"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@pytest.fixture(params=[{"height": 1920, "width": 1080}])
def browser_opt(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_height = request.param['height']
    browser.config.window_width = request.param['width']



desktop_only = pytest.mark.parametrize('browser_opt', [{"height": 2560, "width": 1440}, {"height": 4096, "width": 2160}], indirect=True)
mobile_only = pytest.mark.parametrize('browser_opt', [{"height": 600, "width": 300},{"height": 896, "width": 414}], indirect=True)


@desktop_only
def test_github_desktop(browser_opt):
    browser.open("/")
    browser.element('[href="/login"]').click()

@mobile_only
def test_github_mobile(browser_opt):
    browser.open("/")
    browser.element('[class="flex-1 flex-order-2 text-right"] [aria-label="Toggle navigation"]').click()
    browser.element('[href="/login"]').click()