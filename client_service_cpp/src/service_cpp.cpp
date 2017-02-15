#include "ros/ros.h"
#include "client_service_cpp/service_cpp.h"

bool callback(client_service_cpp::service_cpp::Request &req, client_service_cpp::service_cpp::Response &res)
{
    ROS_INFO("%d",(int)req.a);
    res.b = 1;
    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "service");
    ros::NodeHandle n;
    ros::ServiceServer service = n.advertiseService("topic_service", callback);
    ROS_INFO("Service Ready.");
    ros::spin();
    return 0;
}