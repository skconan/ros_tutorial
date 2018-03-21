Install ROS in Ubuntu
========================================

1. การติดตั้ง
============ 

    1.1. ตั้งค่า sources.list 

.. highlight:: bash
    เพิ่ม deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main ใน /etc/apt/sources.list.d/ros-latest.list เพื่อให้คอมพิวเตอร์ของเราสามารถเข้าถึงซอร์ฟแวร์จาก packages.ros.org. ได้

    
::
    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" >/etc/apt/sources.list.d/ros-latest.list' 
    
    1.2. การตั้งค่า Key        

.. highlight:: html

The literal blocks are now highlighted as HTML, until a new directive is found.

::
   <html><head></head>
   <body>This is a text.</body>
   </html>

The following directive changes the hightlight language to SQL.

.. highlight:: sql

::
   SELECT * FROM mytable

.. highlight:: none

From here on no highlighting will be done.

::
   SELECT * FROM mytable