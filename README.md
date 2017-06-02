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
Q: How to run zeabus completely
	
	A1: 	1. roscore
		2. roslaunch zeabus_bringup minimal.launch
		3. roslainch zeabus_bringup zeabus_localize.launch
		4. roslaunch controller control.launch
		5. Run joy zeabus
		
	A2:	1. roscore
		2. minimal
		3. localization
		4. joy
		5. joy_pub
		6. open_camera
		
Q: Error Could not find a package configuration file provided by "joy" with any ofthe following names:
   joyConfig.cmake
   joy-config.cmake
(ตอนลง SIM เกิดจากไม่มี pkg)
	
	A: pkg ที่ไม่เจอ คือ joy ลองหาประมาณว่า sudo apt-get install ros-kinetic-ชื่อpkg ลอง tab tab ดู
		Example sudo apt-get install ros-kinetic-joy   	
		
Q: Set network for multiple machines

	A1: For SERVER:
		1. เข้าไปดูชื่อ เครื่องที่ hostname 
			$ cat /etc/hostname
		2. ถ้าจะแก้ชื่อเครื่อง 
			// หา 127.0.1.1	แล้วแก้ชื่อ 
			$ sudo nano /etc/hosts		//จำชื่อเดิมไว้ แล้วก็แก้ชื่อใหม่ 
			$ sudo nano /etc/hostname	//หาชื่อเดิมเมื่อกี้ แล้วแก้เป็นชื่อใหม่ให้เหมือนกับใน hosts
		3. เพิ่มเครื่อง CLIENT ให้ครบทุกเครื่อง
			$ sudo nano /etc/hosts
			เพิ่ม ip กับ hostname เครื่อง
			สมมติไรไปก่อน เช่น 192.168.1.xx (xx = ไรก้ได้) ตามด้วย hostname 
			Example 192.168.1.100	skconan
	
	A2: For CLIENT:
		1. ถ้าจะแก้ชื่อเครื่อง 
			// หา 127.0.1.1	แล้วแก้ชื่อ 
			$ sudo nano /etc/hosts		//จำชื่อเดิมไว้ แล้วก็แก้ชื่อใหม่ 
			$ sudo nano /etc/hostname	//หาชื่อเดิมเมื่อกี้ แล้วแก้เป็นชื่อใหม่ให้เหมือนกับใน hosts
		2. เพิ่มเครื่อง SERVER
			$ sudo nano /etc/hosts
			เพิ่ม ip กับ hostname เครื่อง server 
			Example 192.168.1.50	zeabus
			
	A3: Setting CONNECTIONS FOR SERVER and CLIENT:
		1. Go to 'Edit Connections..'
		2. (Optional) setting 'connection name'
		3. Go to 'IPv4 Settings'
			3.1 Method : Manual
			3.2 Address : ip ที่สมมติไว้ ตรง A1, A2
			3.3 Netmask : 255.255.255.0
			3.4 Gateway : 192.168.1.1
			
	A4: เวลา run 'roscore' ก็ run ที่เครื่อง server ที่เดียว

Q: Set ROS_MASTER_URI for multiple machines
	
	A: export ROS_IP=`hostname -I`
	   export ROS_MASTER_URI=http://192.168.1.50:11311

Q: Create RSA key (Client=Your notebook)
	
	A: 1. Open Terminal (ctrl + alt + t).
	   2. Create a new RSA keys. Run command :
		ssh-keygen
	   3. Tranfer RSA keys to host. Run command :
	   	ssh-copy-id username@hostname
Q: In file /etc/hosts

	192.168.1.100   zeabus01
	192.168.1.50    zeabus00
	192.168.1.69    skconan
	192.168.1.27    dantai 
	192.168.1.38    redsanji
	192.168.1.10    Ekarat 
	192.168.1.84    eveem
