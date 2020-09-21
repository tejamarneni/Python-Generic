import os
import shutil

s_path = "C:/Users/tejam/Desktop/one"

d_path = "C:/Users/tejam/Desktop/two"

def move_files():
        for i in range(1,len(os.listdir(d_path))+1):
            if os.path.exists(s_path + '/Excel-0' + str(i) + '.xlsx'):
                shutil.move(s_path + '/Excel-0' + str(i) + '.xlsx',d_path + '/Excel-0' + str(i)) # moves the files from one folder to different folders based on their names
            else:
                print(s_path + '/Excel-0' + str(i) + '.xlsx' + ' does not exist')
        
def move_back():
    for i in range(1,len(os.listdir(d_path))+1):
        if os.path.exists(d_path + '/Excel-0' + str(i) + '/Excel-0' + str(i) + '.xlsx'):
            shutil.move(d_path + '/Excel-0' + str(i) + '/Excel-0' + str(i) + '.xlsx',s_path) # moves the files from different folders into one folder
        else:
            print("file doesn't exist")
