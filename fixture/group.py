from pywinauto.keyboard import send_keys
from pywinauto import timings
import time


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        groups = [node.text() for node in root.children()]
        self.close_group_editor()
        return groups

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        #send_keys(name)
        #send_keys("{ENTER}")
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def delete_group(self, name):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        root.get_child(child_spec=name).click()
        while not tree.is_selected("\\Contact groups\\" + name):
            root.get_child(child_spec=name).click()
        time.sleep(1)
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group = self.app.application.window(title="Delete group")
        self.delete_group.wait("visible")
        self.delete_group.window(auto_id="uxDeleteAllRadioButton").click()
        #send_keys("{ENTER}")
        self.delete_group.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

