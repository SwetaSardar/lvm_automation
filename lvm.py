import os
import time

os.system("clear")
os.system("tput setaf 2")
print("""\t*************************************************************************************************************************""")
print("""\t\t\t\t Welcome to my Logical Volume Management Menu""")
print("""\t*************************************************************************************************************************""")
while True:
    os.system("tput setaf 6")
    print("""\t\t\tLVM Partition Commands \n
    press q: To exit
    press 1: To see the all hard disk available in your system
    press 2: To create physical volume
    press 3: To check all physical volume available in your system
    press 4: To create volume group
    press 5: To check volume group available in your system
    press 6: To create logical volume partition 
    press 7: To check logical volume partition available in your system
    press 8: To format the partition 
    press 9: To create folder
    press 10: To mount the partition
    press 11: To check mounted partition
    press 12: To extend the size of logical volume partition 
    press 13: To re-format the left part(remaining partition)
    """)
    os.system("tput setaf 3")
    choose = input("choose your requirement : ")
    if choose == "q":
        exit()
    elif int(choose) == 1:
        os.system("fdisk -l")
        time.sleep(4)
        os.system("clear")
    elif int(choose) == 2:
        print("ex- sda,b,c whatever disk you have")
        pv = input("enter the volume name : ")
        os.system("pvcreate /dev/{}".format(pv))
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 3:
        os.system("pvdisplay")
        time.sleep(3) 
        os.system("clear")
    elif int(choose) == 4:
        print("first give new vgname then give your pv path")
        vg = input("enter vgname :")
        pv1 = input("enter first pv :")
        pv2 = input("enter second pv :")
        os.system("vgcreate {}vg /dev/{} /dev/{}".format(vg, pv1, pv2))
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 5:
        os.system("vgdisplay")
        time.sleep(4)
        os.system("clear")
    elif int(choose) == 6:
        print("give the size in G or M then name of your lv then your vgname")
        size = input("enter the size you want :")
        name = input("give new lvname :")
        gvg = input("enter vgname :")
        os.system("lvcreate --size {} --name {} /dev/{}".format(size, name, gvg))
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 7:
        os.system("lvdisplay")
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 8:
        print("give your vgname and lvname")
        vn = input("vgname :")
        lvn = input("lvname :")
        os.system("mkfs.ext4 /dev/{}/{}".format(vn, lvn))
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 9:
        f = input("give folder name :")
        os.system("mkdir /{}".format(f))
        print("your folder has been created successfully")
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 10:
        vgn = input("vgnme :")
        lvnm = input("lvname :")
        fname = input("give folder name :")
        os.system("mount /dev/{}/{}  /{}".format(vgn, lvnm, fname))
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 11:
        os.system("df -hT")
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 12:
        size = input("give the size in M,G :")
        vgname = input("give vgname :")
        lvname = input("give lvname :")
        os.system("lvextend --size +{} /dev/{}/{}".format(size, vgname, lvname))
        time.sleep(3)
        os.system("clear")
    elif int(choose) == 13:
        vgnm = input("vgname :")
        lvnm = input("lvname :")
        os.system("resize2fs /dev/{}/{}".format(vgnm, lvnm))
        time.sleep(3)
        os.system("clear")
    else:
        print("invalid input")
        input("please choose correct option : ")
