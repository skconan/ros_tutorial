Install ROS in Ubuntu
========================================

1. การติดตั้ง
------------

    **1.1. ตั้งค่า sources.list**

    เพิ่ม deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main ใน /etc/apt/sources.list.d/ros-latest.list เพื่อให้คอมพิวเตอร์ของเราสามารถเข้าถึงซอร์ฟแวร์จาก packages.ros.org. ได้ ::

    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" >/etc/apt/sources.list.d/ros-latest.list' 

    **1.2. การตั้งค่า Key** ::
    
    $ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 
    
    **1.3. อัพเดท Debian package** ::
    
    $ sudo apt-get update 

    **1.4. ติดตั้ง ROS-Kinetic โดยเราจะลงตัวเต็มที่มีครบทุก package** ::
    
    $ sudo apt-get install ros-kinetic-<package ที่จะลง> 

    แนะนำให้ลงตัวเต็ม ::

    $ sudo apt-get install ros-kinetic-desktop-full 

    Reference: http://wiki.ros.org/kinetic/Installation/Ubuntu 