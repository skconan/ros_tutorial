#!/usr/bin/python2 
import rospy 
from test_service_client.srv import service_test 
from std_msgs.msg import String 

def callback(req): 
    req_data_no = req.requestNO
    req_obj_str = req.request 
    req_data_str = req_obj_str.data 
    print(req_data_no) 
    print(req_data_str)
    response = String()
    response.data = "recieve"
    return req_data_no,response
 
if __name__ == '__main__': 
    rospy.init_node('node_service', anonymous=True) 
    try: 
        service = rospy.Service('name_service', service_test, callback) 
        rospy.spin() 
    except rospy.ServiceException, e: 
        print "Service call failed: %s" % e  
