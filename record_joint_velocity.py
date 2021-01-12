#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import sys  
sys.path.append('/home/maggie/.local/lib/python2.7/site-packages/open3d')  
import numpy as np
from urx import urrtmon
import time
import urx

rob = urx.Robot("192.168.0.2", use_rt=True)
rob.set_payload(2, (0,0,0))
rob.set_tcp((0,0,0,0,0,0))
# timeout=600000
# rob.send_program(b"def myProg():\n\tfreedrive_mode()\nsleep({})\nend".format(timeout))

start = time.time()
while time.time() - start < 60:
    print(rob.rtmon.qd_actual())


rob.stop()
rob.close()