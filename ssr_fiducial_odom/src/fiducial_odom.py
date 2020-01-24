#!/usr/bin/env python

import rospy
import tf
import geometry_msgs.msg 
from nav_msgs.msg import Odometry
from fiducial_msgs.msg import FiducialTransformArray

def fiducialTransformCallback(fid_transform):
    br = tf.TransformBroadcaster()
    br.sendTransform(fid_transform[0], fid_transform[1], rospy.Time.now(), "fiducialTransforms/fiducial_" + str(fid_transform.fiducial_id), "camera_link")


def main():

    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("/fiducial_pose", PoseWithCovarianceStamped, fiducialTransformCallback)
    
    rospy.spin()

if __name__ == '__main__':
    main()