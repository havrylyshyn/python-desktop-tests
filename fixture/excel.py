from comtypes.client import CreateObject
import os
from model.group import Group


class ExcelHelper:
    def __init__(self, app):
        self.app = app

    def get_groups(self):
        work_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        xl = CreateObject("Excel.Application")
        xl.visible = 1
        wb = xl.Workbooks.Open(work_dir + '\\data\\groups.xlsx')
        wsh = wb.sheets[1]
        groups = []
        for row in range(1,11):
            group_name = wsh.Cells[row, 1].Value()
            groups.append(Group(name=group_name))
        xl.Quit()
        return groups
