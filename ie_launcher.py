import win32com.client as com
import sys

ie = com.Dispatch("InternetExplorer.Application")
ie.visible = 1
if len(sys.argv)> 1:
    ie.Navigate(sys.argv[1])
