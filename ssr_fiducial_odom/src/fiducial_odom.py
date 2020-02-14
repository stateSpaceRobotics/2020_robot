#!/usr/bin/env python

import rospy
import tf
import geometry_msgs.msg 
from nav_msgs.msg import Odometry
from fiducial_msgs.msg import FiducialTransformArray

def fiducialTransformCallback(fid_transform):
    
    for transform in fid_transform.transforms:
        br = tf.TransformBroadcaster()
        fid_pose = Pose(Point(transform.transform.translation.x, transform.transform.translation.y, transform.transform.translation.z), transform.transform.rotation)
        br.sendTransform(fid_pose, fid_transform[1], rospy.Time.now(), "fiducial_" + str(transform.fiducial_id), "camera_link")
        
        #need to figure out how to get quaternion info



def main():

    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, fiducialTransformCallback)
    
    rospy.spin()

if __name__ == '__main__':
    main()