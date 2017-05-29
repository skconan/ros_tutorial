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


Q: run control ยังไง

	A: rosrun controller Controller > roslauch controller control.launch


