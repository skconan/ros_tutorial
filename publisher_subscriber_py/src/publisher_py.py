#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('/topic_publisher', String, queue_size=10)
    rate = rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
        msg = "Message NO:"+str(count)
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
        count += 1

if __name__=='__main__':
    rospy.init_node('node_publisher', anonymous=True)
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass