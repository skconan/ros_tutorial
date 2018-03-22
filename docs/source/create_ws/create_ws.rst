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
----------------------------

    สั่ง catkin_init_workspace ที่ directory **catkin_ws/src** :: 
    
    จะเป็นตัวกำหนด workspace โดยจะมีการสร้างไฟล์ CMakeList.txt ขึ้นมา ::
    
    $ cd ~/catkin_ws/src 
    $ catkin_init_workspace 

3. สั่ง catkin_make 
-----------------
    
    ที่ catkain_ws โดยคำสั่ง catkin_make จะเหมือนการ run คำสั่งข้างล่างนี้ ::
    
    $ cd src 
    $ catkin_init_workspace 
    $ cd .. 
    $ mkdir build 
    $ cd build 
    $ cmake ../src -DCMAKE_INSTALL_PREFIX=../install -DCATKIN_DEVEL_PREFIX=../devel 
    $ make 
    
**reference:** http://wiki.ros.org/catkin/commands/catkin_make  
    
    
