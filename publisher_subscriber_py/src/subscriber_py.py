#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    msg = data.data
    rospy.loginfo(msg)

if __name__=='__main__':
    rospy.init_node('node_subscriber', anonymous=True)
    rospy.Subscriber('/topic_publisher', String, callback)
    rospy.spin()