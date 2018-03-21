Set up environment
========================================

1. เพิ่มตัวแปร ROS environment ลงใน Bash session
------------

    โดยการเพิ่มคำสั่ง source /opt/ros/kinetic/setup.bash  ลงในไฟล์ .bashrc หรือ .bash_aliases (แนะนำ: ให้เพิ่มลงใน .bash_aliases)

    เพื่อเพิ่มตัวแปร ROS environment ลงใน Bash session ทุกครั้งที่เปิด Terminal ใหม่ ::

    $ echo "source /opt/ros/kinetic/setup.bash" >> ~/.bash_aliases   

    echo คือ การ show ข้อความที่อยู่ใน double quote (“ ”) 

    >> คือ การนำ ข้อมูลด้านซ้าย ไปใส่ ในไฟล์ด้านขวา โดยถ้าหาก ไฟล์นั้นมีข้อมูลอยู่ ก็จะเขียนต่อในบรรทัดถัดไป 