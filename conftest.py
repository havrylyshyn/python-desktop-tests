import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\qa\\desktop_auto\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

