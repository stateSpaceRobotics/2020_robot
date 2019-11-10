#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovariance, Point, Quaternion, Pose, PoseWithCovarianceStamped
from nav_msgs.msg import Odometry
from fiducial_msgs.msg import FiducialTransformArray

def fiducialTransformCallback(fid_transform):

    odom_msg = Odometry()
    odom_msg.header = fid_transform.header
    odom_msg.child_frame_id = "camera_link"
    odom_msg.pose = fid_transform.pose
    odomPublisher.publish(odom_msg)

odomPublisher = 0

def main():
    global odomPublisher

    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("/fiducial_pose", PoseWithCovarianceStamped, fiducialTransformCallback)
    odomPublisher = rospy.Publisher('/fiducials/odom', Odometry, queue_size=50)

    rospy.spin()

if __name__ == '__main__':
    main()