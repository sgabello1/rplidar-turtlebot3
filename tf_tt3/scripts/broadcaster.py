#!/usr/bin/env python  
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg



def handle_turtle_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = msg.header.stamp
    t.header.frame_id = "world"
    t.child_frame_id = "odom"
    t.transform.translation.x = -3.21840280112
    t.transform.translation.y = 6.92091427233
    t.transform.translation.z = 0.118016734757

    t.transform.rotation.x = 0.00336534120589
    t.transform.rotation.y = 0.0135161813995
    t.transform.rotation.z = -0.605611330647
    t.transform.rotation.w = 0.795638628692

    br.sendTransform(t)
    #sub_once.unregister()
    #rospy.signal_shutdown("cazzi miaa")

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    global sub_once
    sub_once = rospy.Subscriber("/vrpn_client_node/turtlebot/pose",
                     geometry_msgs.msg.PoseStamped,
                     handle_turtle_pose)
    rospy.spin()
    rospy.loginfo("eh...ciao allora!")
