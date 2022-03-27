# -*- encoding=utf8 -*-
__author__ = "beye"

from airtest.core.api import *
import sys
auto_setup(__file__)
uuid = sys.argv[1]

connect_device("Android://127.0.0.1:5037/"+uuid)
set_current(uuid)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco("com.android.systemui:id/alwaysUse").click()
poco("android:id/button1").click()
