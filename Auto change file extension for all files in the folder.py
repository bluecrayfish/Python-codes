#To change file extension of files in the folder, useful for image projects
import os

path = 'C:\\Users\\Name\\Desktop\\folder'  #type in your file path with \\
folder= os.chdir(path)

os.listdir(folder)
i=0
count=0
for file in os.listdir(folder):
    print(file) # to check on the existing files in the folder
    filename, extension = os.path.splitext(file)
    new_extension='.png' #type in your desired filetype, example '.jpg','.tif','.png' etc
    #new_filename="myfile{}".format(i)  #use this to change filename
    #i=i+1 
    #new=os.rename(file, new_filename + new_extension) #to change both filename and extension together
    new=os.rename(file, filename + new_extension) #change this to comment if filename renaming cmd above is used.
    count=count+1


print("There are", (count),"files in this folder.\nThank you!")

path = os.path.realpath(path)
os.startfile(path)

