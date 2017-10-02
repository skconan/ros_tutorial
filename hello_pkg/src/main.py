#!/usr/bin/python2
import rospy
if __name__=='__main__':
	rospy.init_node('hello_program')
	print "Name: "
	name = raw_input()
	print("Hello, "+name)
