import pytest
from actions import Actions

@pytest.fixture
def action(request):
    browser = Actions()
    yield browser
    browser.destroy()