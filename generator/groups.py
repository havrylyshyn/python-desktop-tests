from comtypes.client import CreateObject
import os


work_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
xl = CreateObject("Excel.Application")
xl.visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range["A%s" % (i+1)].Value[()] = "group%s" % i
wb.SaveAs(os.path.join(work_dir, "data\\groups.xlsx"))
xl.Quit()