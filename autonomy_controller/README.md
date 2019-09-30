# autonomy_controller

This package provides a SMACH state machine to control the robot behavior

## To Use:
Include this node in one of your launch files:
```xml
<node pkg="autonomy_controller" type="andy_demo.py" name="state_machine" output="screen" />
```

Available nodes are:
* andy_demo.py
    * Launches the state machine for the andy demo

* Total_State_Machine.py
    * Launches the state machine for the three-robot system