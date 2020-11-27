import pytest
import os
from comtypes.client import CreateObject
from model.group import Group
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\qa\\desktop_auto\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("excel_"):
            testdata = get_groups_from_excel()
            metafunc.parametrize(fixture, testdata, ids=(str(x) for x in testdata))


def get_groups_from_excel():
    work_dir = os.path.dirname(os.path.realpath(__file__))
    xl = CreateObject("Excel.Application")
    xl.visible = 1
    wb = xl.Workbooks.Open(work_dir + '\\data\\groups.xlsx')
    wsh = wb.Sheets[1]
    groups = []
    for row in range(1, 11):
        group_name = wsh.Cells[row, 1].Value()
        groups.append(Group(name=group_name))
    xl.Quit()
    return groups
