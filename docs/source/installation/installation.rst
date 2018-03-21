Install ROS in Ubuntu
========================================

1. การติดตั้ง
============ 

    1.1. ตั้งค่า sources.list 

    เพิ่ม deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main ใน /etc/apt/sources.list.d/ros-latest.list เพื่อให้คอมพิวเตอร์ของเราสามารถเข้าถึงซอร์ฟแวร์จาก packages.ros.org. ได้

        $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" >/etc/apt/sources.list.d/ros-latest.list' 

    1.2. การตั้งค่า Key        

