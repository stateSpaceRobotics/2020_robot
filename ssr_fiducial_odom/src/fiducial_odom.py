#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovariance, Point, Quaternion, Pose
from nav_msgs.msg import Odometry
from fiducial_msgs.msg import FiducialTransformArray

def fiducialTransformCallback(fid_transforms):

    for transform in fid_transforms.transforms:

        odom_msg = Odometry()
        odom_msg.header.stamp = fid_transforms.header.stamp
        odom_msg.header.frame_id = fid_transforms.header.frame_id
        odom_msg.child_frame_id = "fid" + str(transform.fiducial_id)
        odom_msg.pose.pose = Pose(Point(transform.transform.translation.x, transform.transform.translation.y, transform.transform.translation.z), transform.transform.rotation)
        odomPublisher.publish(odom_msg)

odomPublisher = 0

def main():
    global odomPublisher

    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, fiducialTransformCallback)
    odomPublisher = rospy.Publisher('/fiducials/odom', Odometry, queue_size=50)

    rospy.spin()

if __name__ == '__main__':
    main()