import os
import shutil
assembled={                                   #defining dictionary keys and values manually
    ".png"  : "images",
    ".jpeg" : "images",
    ".pdf"  : "documents",
    ".docx" : "documents",
    ".pptx" : "presentations",
    ".mp4"  : "videos",
    ".keras": "documents"
    }
def File_Organizer(folder):
    filenames=os.listdir(folder)                   #list of file  names inside folder
    moved_count=0
    skipped_count=0
    for file in filenames:                         #loop in list
        full_path=os.path.join(folder,file)        #iterating over each file name to get full usable path 
        if os.path.isfile(full_path):              #checking if the filename is a file or subfolder 
            extension=os.path.splitext(full_path)   #splitting path to read clearly    
            ext=extension[1]                        #extracting only extension part from full path 
            category=assembled.get(ext,"others")    #if any files that doesnot exist in folder categorize it as others 
            category_folder=os.path.join(folder,category)    #creating path for category folders
            if not os.path.isdir(category_folder):           #checking if the category folder already exists
                os.mkdir(category_folder)                     #creating  new directory
            try: 
                shutil.move(full_path, category_folder)  #checking with try except block that
                print(f"moved {file}, to {category}")  
                moved_count+=1
            except shutil.Error as e:
                print(f"Skipped {file}: {e}")
                skipped_count+=1
    print(f"Organizing complete:{moved_count} files moved , {skipped_count} files skipped.")       
if __name__ == "__main__":
    folder =input("Enter the folder path to organize: ")                #path of main folder
    if not os.path.isdir(folder):
        print("Error: folder path not found. Please check the path and try again")
        exit()                                             
    File_Organizer(folder)