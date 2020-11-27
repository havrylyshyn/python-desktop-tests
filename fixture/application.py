from pywinauto.application import Application as WinApplication
from fixture.group import GroupHelper
from fixture.excel import ExcelHelper


class Application:

    def __init__(self, target):
        self.application = WinApplication(backend="win32").start(target)
        self.main_window = self.application.window(title="Free Address Book")
        self.main_window.wait("visible")
        self.group = GroupHelper(self)
        self.excel = ExcelHelper(self)

    def destroy(self):
        self.main_window.close()
