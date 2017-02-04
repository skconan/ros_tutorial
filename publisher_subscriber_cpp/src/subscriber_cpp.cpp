#include "ros/ros.h"
#include "std_msgs/String.h"

void callback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("Mesage from topic : [%s]", msg->data.c_str());
}
  
int main(int argc, char **argv)
{
  ros::init(argc, argv, "node_subscriber");
  ros::NodeHandle n;
  // subscribe node name is /topic_publisher
  ros::Subscriber sub = n.subscribe("/topic_publisher", 1000, callback);
  ros::spin();

  return 0;
}