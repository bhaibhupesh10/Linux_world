import os

print("\t\t\tWelcome to out Tool\n\n")
print("Press1: to open notepad")
print("Press2: to open chrome")
ch = input("Enter your choice : ")
if int(ch)==1:
    os.system("notepad")
elif int(ch)==2:
    os.system("start chrome")
else:
    print("idk")