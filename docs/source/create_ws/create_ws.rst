Create Workspace
========================================

    .. image:: images/tree.png
        :alt: tree
        :align: center  

1. สร้าง directory สำหรับ workspace 
---------------------------------

    สร้าง directory ชื่อ catkin_ws ที่ directory **home** และสร้าง directory **src** ใน **catkin_ws** ::

    $ cd ~/ 
    $ mkdir catkin_ws  
    $ cd ~/catkin_ws 
    $ mkdir src 
    
    
2. สั่ง catkin_init_workspace    
------------------------------------------------------

    สั่ง catkin_init_workspace ที่ directory **catkin_ws/src** :: 
    
    จะเป็นตัวกำหนด workspace โดยจะมีการสร้างไฟล์ CMakeList.txt ขึ้นมา ::
    
    $ cd ~/catkin_ws/src 
    $ catkin_init_workspace 
