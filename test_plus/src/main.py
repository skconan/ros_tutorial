#!/usr/bin/python2
import rospy
if __name__=='__main__':
	rospy.init_node('calculator')
	cmd = int(input())
	
	a = float(input())
	b = float(input())
	
	if cmd == 1:
		print(a+b)
	else:
		print(a-b)
