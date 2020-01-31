import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

#Recieves controller state information from the Joy Node and publishes a Twist message accordingly
def ControllerCallback(controllerState):
    global notPaused
    global velocityPublisher
    global notPausedToggleTime

    #Check whether or not to "pause" control
    if controllerState.buttons[buttons["START"]]:

        #This is effectively button "debouncing" i.e. ensuring that the state change occurs only once per physical button press
        duration = rospy.Time.now() - notPausedToggleTime
        if duration.to_sec() >= 1:
            notPaused = notPaused ^ 1
            notPausedToggleTime = rospy.Time.now()

    msg = Twist()

    #Determine the linear velocity to send
    x = -1.0 * (1.0 - controllerState.axes[axes["LT"]]) / 8.0

    #Forward direction takes priority
    if controllerState.axes[axes["RT"]] != 1.0:
        x = (1.0 - controllerState.axes[axes["RT"]]) / 8.0

    #notPaused = 0 will set all math to 0.  This effectively "pauses" the robot
    x *= notPaused
    z = controllerState.axes[axes["LS_LEFT_RIGHT"]] * notPaused

    msg.linear.x = x
    msg.angular.z = z * math.pi / 2.0

    velocityPublisher.publish(msg)


#Dictionaries for Controller State array accessing
buttons =   {"Trigger" : 0, "A" : 1, "B" : 2, "C" : 3, "D" : 4, "Flip" : 5, "H1_UP" : 6, "H1_RIGHT" : 7, "H1_DOWN" : 8, "H1_LEFT" : 9, "H2_UP" : 10, "H2_RIGHT" : 11, "H2_DOWN" : 12, "H2_LEFT" : 13, "NOT_USED_14" : 14, "NOT_USED_15" : 15, "NOT_USED_16" : 16}
axes =      {"Drive_X" : 0, "Drive_Y": 1, "Twist" : 2, "POV_X" : 3, "POV_Y" : 4}