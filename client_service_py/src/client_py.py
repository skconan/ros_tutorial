#!/usr/bin/env python

import rospy
from srv_msg_pkg.srv import service
from srv_msg_pkg.msg import message
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('node_client', anonymous=True)
    rospy.wait_for_service('name_service')
    client = rospy.ServiceProxy('name_service', service)
    data = client(String("Request message"))
    data = data.data
    print data
