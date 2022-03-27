# -*- encoding=utf8 -*-
__author__ = "beye"

from airtest.core.api import *
import sys
auto_setup(__file__)
uuid = sys.argv[1]

connect_device("Android://127.0.0.1:5037/"+uuid)
set_current(uuid)
wake()
home()

