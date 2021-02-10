### Urx Python

Some importnant commands in urx to control robot

## Command
### 1.initalization
Function | Explaination
--- | ---
rob = urx.Robot("192.168.0.100") | Connect to robot
rob.set_tcp((0, 0, 0.1, 0, 0, 0)) | Set tooltip pose
rob.set_payload(2, (0, 0, 0.1)) | Set payload and center of gravity
import time <br /> time.sleep(0.2) | leave some time for robot to process the setup commands

### 2.motion
Function | Explaination
--- | ---
rob.getj() | Get 6 joint position in radius
rob.getpose() | Orientation + vector
rob.movej((1, 2, 3, 4, 5, 6), a, v) | (Joint variable, acc, vel) <br /> free space non-linear path
rob.movel((x, y, z, rx, ry, rz), a, v)  <br /> rob.movel((0,0,0.1,0,0,0), relative=True) | (pose, acc, vel) <br /> linear motion
rob.movep((x, y, z, rx, ry, rz), acc=a, vel=v) | (pose, acc=a, vel=v, wait=False) <br /> constant speed through several waypoints
rob.movec(via, to, acc=a, vel=v) | circular motion constant speed
rob.movels([p1, p2], vel=v, acc=a, radius=r) | moving through several points with a radius
rob.translate((l, 0, 0), acc=a, vel=v, wait=False)| ((l, 0, 0), acc, vel) <br /> Translation w.r.t base frame
rob.translate_tool((0, 0, l), vel=v, acc=a, wait=False) | moving tool z in tool coordinate
t = rob.get_pose() <br /> t.orient.rotate_zb(pi / 8) <br /> rob.set_pose(t, vel=v, acc=a, wait=False) | rotate tcp around around base z <br /> The position of tcp remain
rob.speedl_tool((0, 0, -v, 0, 0, 0), acc=a, min_time=3) | moving in tool -z using speed command <br /> The robot will stop automatically after 3s <br /> if the spped is high, "sudden stop"
rob.stopj(a) | The robot will stop at an acceleration
rob.x | returns current x
rob.z_t += 0.01 | move robot in tool z axis for +1cm
rob.rx | returns 0 (return x component of axis vector)
rob.rx -= 0.1 | rotate tool around X axis
robot.getForce() | get force
rob.stopl() |
csys = rob.new_csys_from_xpy() <br /> rob.set_csys(csys) | generate a new csys from 3 points: X, origin, Y

### motion type
![motion type](/image/urx_motion_type.png)

## Note
1.The wait function is not working well in simulation, it did not reflect the real time to reach a certain target, instead, urx uses an algorithm to calculate the time and it creates many problems >> add ```wait=False``` in movel, movej, movep, movec, setpose... for simulation (by default wait=True for real robot)

2.```First pose``` is crucial, when the robot is in singularity (straight), vulnerable to violation and singularity config. Two situation:
a.Follow the original script of move_ur if no tcp is set
b.change the pose value >> use movej

3.Two ways to set TCP:  
A.teach pendant  
B.urx   
URX is more flexible in setting payload and TCP, however, critical violation may happen and persist if it is wrongly set >> safer to use teach pendant instead.

4.Check ```UR script``` for the full explanation of urx

### Development using Transform objects from math3d library:
```
from urx import Robot
import math3d as m3d

robot = Robot("192.168.1.1")
mytcp = m3d.Transform()  # create a matrix for our tool tcp
mytcp.pos.z = 0.18
mytcp.orient.rotate_zb(pi/3)
robot.set_tcp(mytcp)
time.sleep(0.2)

# get current pose, transform it and move robot to new pose
trans = robot.get_pose()  # get current transformation matrix (tool to base)
trans.pos.z += 0.3
trans.orient.rotate_yb(pi/2)
robot.set_pose(trans, acc=0.5, vel=0.2)  # apply the new pose

#or only work with orientation part
o = robot.get_orientation()
o.rotate_yb(pi)
robot.set_orientation(o)
```
