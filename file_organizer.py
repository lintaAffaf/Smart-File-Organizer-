import os
import shutil
#defining category folders inside a dictionary 
assembled={                                  
    ".png"  : "images",
    ".jpeg" : "images",
    ".pdf"  : "documents",
    ".docx" : "documents",
    ".pptx" : "presentations",
    ".mp4"  : "videos",
    ".keras": "documents"
    }

def File_Organizer(folder):
    """ Organizes files in a given folder by moving them into
        subfolders based on their file extension categories."""
    filenames=os.listdir(folder)                   #list of file  names inside folder
    moved_count=0                                  #counter for how many files are moved
    skipped_count=0                                #counter for how many files are skipped 
    
   
 
    for file in filenames:       #Iterating over each file name to get full usable path and applying 
        full_path=os.path.join(folder,file)                 
        if os.path.isfile(full_path):              
            extension=os.path.splitext(full_path)   
            ext=extension[1]              # extracting only file extension from file name"          
            category=assembled.get(ext,"others")   
            category_folder=os.path.join(folder,category)    
            if not os.path.isdir(category_folder):#  if condition to ignore any subfolder or any other category not defined 
                os.mkdir(category_folder)                   
            try: 
                shutil.move(full_path, category_folder) 
                print(f"moved {file}, to {category}")  
                moved_count+=1
            except shutil.Error as e:
                print(f"Skipped {file}: {e}")
                skipped_count+=1
    #Outputs a summary of files moved and skipped.
    print(f"Organizing complete:{moved_count} files moved , {skipped_count} files skipped.") 

# run only when script is executed directly, not when imported    
if __name__ == "__main__":
    folder =input("Enter the folder path to organize: ")               
    if not os.path.isdir(folder):
        print("Error: folder path not found. Please check the path and try again")
        exit()                                             
    File_Organizer(folder)