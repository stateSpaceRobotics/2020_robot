#!/usr/bin/env python

import rospy
import tf
import geometry_msgs.msg 
from nav_msgs.msg import Odometry
from fiducial_msgs.msg import FiducialTransformArray

def fiducialTransformCallback(fid_transform):

    
    try:
        #transform from map to camera
        #(trans,rot) = listener.lookupTransform('map', 'camera_link', rospy.Time(0))
        for transform in fid_transform.transforms:
            br = tf.TransformBroadcaster()
            
            #get the pose of the fidoosh
            fid_pose = Pose(Point(transform.transform.translation.x, transform.transform.translation.y, transform.transform.translation.z), transform.transform.rotation)
            
            #transform pose from cam to map?
            fid_pose_from_map = tf.transformPose('map', fid_pose)
            
            rot = fid_pose_from_map.orientation
            trans = fid_pose_from_map.position
            #publish that $tuFf
            br.sendTransform((trans.x, trans.y, trans.z), (rot.x, rot.y, rot.z, rot.w), rospy.Time.now(), "fiducial_" + str(transform.fiducial_id), "camera_link")

            #time.now may not be right
            #look at fiducial slam to see how it publishes 
    except tf.LookupException:
        pass

        

listener = 0
def main():
    global listener 
    rospy.init_node('listener', anonymous = True)
    listener = tf.TransformListener()
    
    rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, fiducialTransformCallback)
    
    rospy.spin()

if __name__ == '__main__':
    main()