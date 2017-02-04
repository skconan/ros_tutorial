#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
    // init name of node
    ros::init(argc, argv, "node_publisher");
    ros::NodeHandle n;
    // create topic
    ros::Publisher chatter_pub = n.advertise<std_msgs::String>("/topic_publisher", 1000);
    ros::Rate loop_rate(10);
    int count = 0;    
    while (ros::ok())
    {
        // Declare variable
        std_msgs::String msg;   
        std::stringstream ss;
        
        ss << "Message NO: " << count;
        msg.data = ss.str();    
        ROS_INFO("%s", msg.data.c_str());   
        
        // Publisher 
        chatter_pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        ++count;
    }   
    return 0;
}
