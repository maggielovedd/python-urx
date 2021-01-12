### adding get joints velocity vector ability in the following way, must in RT monitor mode.

```python
import urx
r = urx.Robot('192.168.10.1', use_rt=True)
qd = r.rtmon.qd_actual()
```

### Record joint velocity

record_joint_velocity.py

```python
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

start = time.time()
while time.time() - start < 60:
    # use freedrive mode
    print(rob.rtmon.qd_actual())


rob.stop()
rob.close()
```

