from pytest import fixture
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.application import App
import settings

@fixture(autouse=True, scope='function')
def preconditions():
    print('setup preconditions before tests')
    yield
    print('setup postconditions after tests')


@fixture(scope='session')
def get_playwright(): #
    with sync_playwright() as playwright:
        yield playwright

@fixture(scope='session')
def desktop_app(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_auth(desktop_app):
    desktop_app.goto('/login')
    desktop_app.login(**settings.USER)
    yield desktop_app