Create Package
========================================

Package คือ directory ที่มี source code (Program หรือ Node), library, configuration file และอื่นๆ เช่น msg, srv, และ launch 

Package name ขึ้นต้นด้วย a-z ตัวเล็ก และ แบ่งคำด้วย _ (underscore) เท่านั้น !!! 

1. ขั้นตอนการสร้างคราวๆ 
---------------------------------

    เดี๋ยวจะมีให้ลองสร้างข้างล่างนะครับ 

    1.1. เราจะสร้าง Package ไว้ที่ ~/catkin_ws/src 

    1.2. สั่ง catkin_create_pkg <ชื่อ package> <ชื่อ depend1> <depend2> <depend...> 

    1.3. Depend คือ package หรือ libraries ที่เกี่ยวข้อง เช่น roscpp rospy  ::

        catkin_create_pkg <ชื่อ package> <ชื่อ depend1> <depend2> <depend...> 
        สร้าง package โดยมี dependencies คือ depend1, depend2, … 
        !! warning !!: ชื่อ package ขึ้นต้นด้วย a-z ตัวเล็ก และ แบ่งคำด้วย _ (underscore) เท่านั้น !!! 

    1.4. สั่ง catkin_make ที่ ~/catkin_ws 

    1.5. สั่ง source devel/setup.bash ทุกครั้งที่สร้าง pkg ใหม่  ::

    $ catkin_make 
    $ source devel/setup.bash 

**reference:** http://wiki.ros.org/action/fullsearch/ROS/Tutorials/CreatingPackage    
    
    
2. การเพิ่ม Dependencies ในตอนหลัง     
-------------------------------

    เดี๋ยวจะขอพูดถึงตอนหลังนะครับ ว่าถ้าสร้าง Package ไปแล้วแต่ลืมใส่ Dependencies ที่จำเป็นไปจะไปแก้ตรงไหน

3. ลองสร้าง Package   
-----------------
    
    เราจะสร้าง Package ที่ข้างในมีโปรแกรมแสดงชื่อที่รับมาจาก User และแสดงผล Hello, ตามด้วยชื่อ ดังรูป 
    
    .. image:: images/pkg.jpg
        :alt: rosrun_pkg
        :align: center


    3.1. เราจะสร้าง Package ไว้ใน ~/catkin_ws/src 

    3.2. สร้าง package ชื่อว่า hello_pkg ซึ่ง จะเขียนโปรแกรมด้วย Python แสดงว่าต้องมีการอ้างอิง (dependency) rospy สั่ง catkin_create_pkg hello_pkg rospy ::

    $ cd ~/catkin_ws/src 
    $ catkin_create_pkg hello_pkg rospy  

    จะได้ผลลัพธ์ ดังรูป

    .. image:: images/catkin_create_pkg.jpg
        :alt: catkin_create_pkg
        :align: center  
        

    3.3. สั่ง catkin_make ที่ ~/catkin_ws หากไม่มี Error จะได้ผลลัพธ์ใกล้เคียงกับรูปด้านล่าง 

    .. image:: images/catkin_make.jpg
        :alt: catkin_make
        :align: center


    3.4. เข้าไปที่ directory hello_pkg/src 

    3.5. สร้างไฟล์ main.py เพื่อเขียนโปรแกรมรับชื่อ และแสดงผล ดังนี้ ::

        # execute with python2 
        #!/usr/bin/python2 
        import rospy 
        # check module name is main 
        if __name__=='__main__': 
        # ประกาศชื่อ node 
                rospy.init_node('hello_program') 
                print "Name: " 
                name = raw_input() 
                print("Hello, "+name)   

    3.6. สั่ง catkin_make ที่ ~/catkin_ws 

    3.7. ก่อนที่เราจะใช้ ROS หรือรันโปรแกรม ให้สั่ง roscore เพื่อเหมือนเป็นการเปิด server ให้ msg หรือ node ต่างๆสามารถทำงาน หรือคุยกันได้  ปล. ต้องเปิดทิ้งไว้นะ  

    .. image:: images/roscore.jpg
        :alt: roscore
        :align: center  


    3.8. รันโปรแกรม โดยใช้คำสั่ง rosrun ::

        **rosrun <ชื่อ package> <ชื่อไฟล์ python หรือชื่อ node>** 
        ถ้าเป็น Python: rosrun package_name file_name.py 
        ถ้าเป็น Cpp:rosrun packace_name node_name 
        Node_name ตั้งค่าใน CMakeList.txt 

    3.9. ในกรณีที่ rosrun <tab>ๆๆ (ปุ่ม Tab) แล้วชื่อ package ไม่ขึ้น ให้ทำตามนี้
        3.9.1. สั่ง source devel/setup.bash 
        3.9.2. ตามด้วย rospack profile 

    3.10. ในกรณีนี้ ถ้าไม่สามารถรันไฟล์ Python ได้ (มันจะมี error ประมาณว่าไม่สามารถ Excecute ไฟล์ชื่อ ... ได้) ให้เปลี่ยน permission ไฟล์ที่จะรัน ให้สามารถ execute ได้ ::

    $ chmod 755 <PATH ของไฟล์>

    3.11. ถ้าหากเป็นไฟล์ cpp จะต้องมีการเพิ่ม executable และตั้งค่าในไฟล์ CMakelist.txt ซึ่งจะกล่าวต่อไป  

    3.12. ที่นี้มาลองรันโปรแกรมกัน ::

    $ catkin_make  
    $ source devel/setup.bash 
    $ rospack profile 
    $ rosrun hello_pkg main.py 

    Name:  
    skconan 
    Hello, skconan. 

    .. image:: images/pkg.jpg
        :alt: rosrun_pkg
        :align: center

4. rosnode 
-----------

    rosnode เป็น Command ของ ros ที่จะใช้จัดการเกี่ยวกับ node (โปรแกรมที่กำลัง run อยู่เราเรียกว่า node)

    4.1. เราลองรันโปรแกรมค้างไว้ก่อน แล้วมาลองใช้คำสั่ง rosnode กันคร่าวๆ

    .. image:: images/running_pkg.jpg
        :alt: running_pkg
        :align: center


    4.2. รันคำสั่ง rosnode list ในอีก Terminal โดย rosnode list เป็นคำสั่งที่แสดง node กำลังทำงานอยู่ (/rosout เป็น node ที่ roscore สร้างขึ้นมา) ในบทความต่อไปเราจะมารู้จักกับ node กันให้มากขึ้น ::

    $ rosnode list 

    .. image:: images/rosnode_list.jpg
        :alt: rosnode_list
        :align: center

    
**reference:** http://wiki.ros.org/ROS/Tutorials/CreatingPackage  
