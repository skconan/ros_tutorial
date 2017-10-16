#!/usr/bin/python2

import rospy
from test_service_client.srv import service_test
from std_msgs.msg import String


def client():
    rospy.wait_for_service('name_service')
    client = rospy.ServiceProxy('name_service', service_test)
    for i in range(0, 100):
        data = client(i, String("Request message"))
        print(data.responseNO)
        print(data.response.data)


if __name__ == '__main__':
    rospy.init_node('node_client', anonymous=True)
    client()