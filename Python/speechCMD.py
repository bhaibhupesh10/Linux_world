import speech_recognition as sr
import os
import pyttsx3

pyttsx3.speak("Hello Bhupesh... Welcome to your Terminal.. I am your voice assistent. please tell how may i help you...")
print("\t\t\t Hey Bhupesh welcome to my TUI that makes life simple") 



r = sr.Recognizer()

while True:
 with sr.Microphone() as source:
  pyttsx3.speak("start saying")
  print("start saying ..")
  audio = r.listen(source)
  pyttsx3.speak("I got it , plz wait ...")
  print("I got it , Please wait ...")

  ch = r.recognize_google(audio)
  print(ch)

  #os.system("ssh -i docker3.pem ec2-user@100.25.158.237 'sudo -i'")
 
  if (("how" in ch) and ("can"  in ch)):
   pyttsx3.speak("I have following options for you")
   print("\t\t\tI have following options for you")
   '''print("""       
   to check available disk
             to create a physical volume
             to create a volume group
             to create a logical volume
             format a logical volume partition
             to increase a size of logical volume
             mount the logical volume to a folder
             show the mount space
             start the datanode
             running java processes
             show me report of connected datanode
             resize lvm while datanode connected
             start docker-services for you
             show you available docker images
             launch docker os for you
             show you running docker os
             exit""")'''
   pyttsx3.speak("I can check available disk")
   print("\t\t\tI can check available disk")
   
   pyttsx3.speak("I can create a physical volume")
   print("\t\t\tI can create a physical volume")

   pyttsx3.speak("I can create a volume group")
   print("\t\t\tI can create a volume group")
   
   pyttsx3.speak("I can create a logical volume")
   print("\t\t\tI can create a logical volume")
   
   pyttsx3.speak("I can format a logical volume")
   print("\t\t\tI can format a logical volume")
   
   pyttsx3.speak("I can increase a size of logical volume")
   print("\t\t\tI can increase a size of logical volume")
   
   pyttsx3.speak("I can resize a logical volume")
   print("\t\t\tI can resize a logical volume")

   pyttsx3.speak("I can mount the logical volume to a folder")
   print("\t\t\tI can mount the logical volume to a folder")
   
   pyttsx3.speak("I can show you mount point")
   print("\t\t\tI can show you mount space")
   
   pyttsx3.speak("I can start the datanode")
   print("\t\t\tI can start the datanode")
   
   pyttsx3.speak("I can show you running java processes")
   print("\t\t\tI can show you running java processes")
   
   pyttsx3.speak("I can show you report of connected datanode")
   print("\t\t\tI can show you report of connected datanode")
   
   pyttsx3.speak("I can resize lv while datanode connected")
   print("\t\t\tI can resize lv while datanode connected")
   
   pyttsx3.speak("I can start docker-services for you")
   print("\t\t\tI can start docker-services for you")
   
   pyttsx3.speak("I can show you available docker images")
   print("\t\t\tI can show you available docker images")
   
   pyttsx3.speak("I can launch docker os for you")
   print("\t\t\tI can launch docker os for you")
   
   pyttsx3.speak("I can show you running docker os")
   print("\t\t\tI can show you running docker os")
   
   '''pyttsx3.speak("I can resize a logical volume")
   print("I can resize a logical volume", end="")
   
   pyttsx3.speak("I can resize a logical volume")
   print("I can resize a logical volume", end="")'''
   
  elif (("disk" in ch) or ("disc" in ch) or ("Disc" in ch) or ("Disk" in ch)) and (("available" in ch) or ("show" in ch)):
         pyttsx3.speak("showing to you... available disk..")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo fdisk -l"')

  elif (("create" in ch) or ("Create" in ch)) and (("Physical volume" in ch) or ("physical volume" in ch)):
         pyttsx3.speak("creating physical volume for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo pvcreate /dev/xvdb /dev/xvdc"')
         pyttsx3.speak("physical volume created") 
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo pvdisplay"')

  elif (("create" in ch) or ("Create" in ch)) and (("Volume group" in ch) or ("volume group" in ch)):
         print("write volume group name: ",end='')
         VGname = input()
         pyttsx3.speak("creating volume group for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo vgcreate {} /dev/sdc /dev/sdb"'.format(VGname))
         pyttsx3.speak("volume group created") 
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo vgdisplay"')

  elif (("create" in ch) or ("Create" in ch)) and (("Logical volume" in ch) or ("logical volume" in ch)):
         print("write required size: ",end='')
         RequiredSize = input()
         print("write logical volume name: ",end='')
         LVname = input()
         pyttsx3.speak("creating logical volume for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvcreate --size {} --name {} myvg"'.format(RequiredSize,LVname))
         pyttsx3.speak("logical volume created")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvdisplay"')
         #createUser = input()
         #os.system("useradd  {}".format(createUser))

  elif (("format" in ch) or ("Format" in ch)) and (("partition" in ch) or ("format partition" in ch)):
         pyttsx3.speak("Partition formatted")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo mkfs.ext4 /dev/myvg/vklv"')
  elif (("Mount" in ch) or ("mount" in ch)) and (("logical volume" in ch) or ("logicalvolume" in ch)):
         print("type mountpoint :", end='')
         mountpoint = input()
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo mount /dev/myvg/vklv /{}"'.format(mountpoint))
         pyttsx3.speak("here it is your .. mounted logical volume")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo df -Th"')

  elif (("show" in ch)) and (("mountpoint" in ch) or ("Mount point" in ch)):
         pyttsx3.speak("showing mountpoint to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo df -Th"')

  elif (("start" in ch)) and (("run" in ch) or ("data not" in ch) or ("Datanode" in ch) or ("data node" in ch)):
         pyttsx3.speak("starting datanode for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo hadoop-daemon.sh start datanode"')

  elif (("show" in ch)) and (("Java process" in ch) or ("java process" in ch) or ("java processes" in ch)):
         pyttsx3.speak("showing running processes to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo jps"')

  elif (("show" in ch)) and (("connected" in ch) or ("datanode" in ch) or ("data  not" in ch)):
         pyttsx3.speak("showing connected datanodes to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo hadoop dfsadmin -report"')

  elif (("Extend" in ch) or ("extend" in ch)) and (("logical volume" in ch) or ("Logical volume" in ch)):
         print("size of logical volume: ",end='')
         SizeOfLv = input()
         pyttsx3.speak("resize your logical volume")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvresize -L {} /dev/myvg/vklv"'.format(SizeOfLv))
         pyttsx3.speak("logical volume resized")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvs"')

  elif (("Resize" in ch) or ("resize" in ch)) and (("extended" in ch) or ("increased" in ch)):
         pyttsx3.speak("resizing your logical volume")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo resize2fs -f /dev/myvg/vklv"')

  elif (("start" in ch)) and (("docker services" in ch) or ("docker service" in ch) or ("docker" in ch)):
         pyttsx3.speak("Starting docker services for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo systemctl start docker"')

  elif (("show" in ch)) and (("images" in ch)) and (("available" in ch) or ("centos" in ch) or ("o s" in ch) or ("docker os" in ch)):
         pyttsx3.speak("Showing available images to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker images"')

  elif (("Launch" in ch) or ("launch" in ch)) :
         pyttsx3.speak("Lauching centos in docker")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker run -itd centos"')

  elif (("show" in ch)) and (("running" in ch)) and (("centos" in ch) or ("os" in ch) or ("o s" in ch)):
         pyttsx3.speak("Lauching centos in docker")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')

  elif (("show" in ch)) and (("running os" in ch) or ("running" in ch) or ("os" in ch)) :
         pyttsx3.speak("showing running os to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')

  elif (("close" in ch) or ("exit" in ch) or ("shoutdown" in ch)):
         pyttsx3.speak("Thankyou for using me. I am always here for you help. good bye....")
         exit()
 
  else:
         pyttsx3.speak("option not supported....Plz try again")
         print("option not supported")

  pyttsx3.speak("plz enter for continue.....")
  input("plz enter for continue.....")
  print("""              to check available disk
             to create a physical volume
             to create a volume group
             to create a logical volume
             format a logical volume partion
             mount the logical volume to a folder
             show the mount space
             start the datanode
             running java processes
             show me report of connected datanode
             to increase a size of logical volume
             resize lvm while datanode connected
             start docker-services for you
             show you available docker images
             launch docker os for you
             show you running docker os
             exit""")