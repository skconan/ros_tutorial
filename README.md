For Zeabus 2017


Before you start ros tutorial ,confirm you install and setting ros complete follow:
	http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
	
Q&A

Q:  rosrun แล้วไม่เจอ package (rosrun <ไม่เจอ pkg>

	A1: source devel/setup.bash in catkin_ws 

	A2: rospack profile

Q: rosrun แล้วไม่เจอ file (rosrun pkg_name <ไม่เจอไฟล์>

	A: chmod 755 filename or chmod 755 -R directory

Q: เปิด simulator ยังไง

	A: roslaunch syrena_gazebo trandec.launch

Q: ใช้ keyboard control หุ่นยังไง
	
	A: rosrun syrena_teleop keyboard.py 

Q: เปิดดูกล้องยังไง

	A: rqt -p ชื่อไรก็ได้ > menu bar > visualization > 

Q: Run control ยังไง

	A: roslaunch controller control.launch > rosrun controller Controller
Q: Run joy zeabus

	A: roslaunch zeabus_teleop joy_F710.launch > rosrun zeabus_teleop zeabus_joy
Q: How to run completely
	
	A: 	1. roslaunch zeabus_bringup minimal.launch
		2. roslainch zeabus_bringup zeabus_localize.launch
		3. roslaunch controller control.launch
		4. Run joy zeabus
		
