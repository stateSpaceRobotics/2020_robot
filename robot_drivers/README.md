# ssr_robot_drivers

This package provides a python script that will take in twist messages from the navigation stack and send them to the robot over UDP in the required format.

## To Use:
Include this node in a launch file:
```xml
<node name="robot_driver" pkg="ssr_robot_drivers" type="robotdriver.py" />
```