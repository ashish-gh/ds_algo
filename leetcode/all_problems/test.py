import os
from collections import Counter
from typing import List



# files = ["ashish.jpg", "ashish1.jpg", "ashish2.jpg", "ashish3.jpg"]

def check_file_names(files: List[str]):
    all_files = []

    def get_file_with_counter(all_files, file, idx = 0):
        f_name, ext = os.path.splitext(file)
        idx = int(idx +1)
        f_name = f_name + str(idx) + ext
        print(f_name, "----")
        print(all_files)

        if f_name in all_files:
            get_file_with_counter(all_files, f_name, idx )

        all_files.append(f_name)

        
    if not files:
        return all_files
    
    for file in files:
        if not file in all_files:
            print(file)
            all_files.append(file)
        else:
            idx = 0
            get_file_with_counter(all_files, file, idx)
    
    return all_files

    




files = ["ashish.jpg", "ashish1.jpg", "ashish2.jpg", "ashish.jpg","ashish1.jpg"]
print(check_file_names(files))


    











