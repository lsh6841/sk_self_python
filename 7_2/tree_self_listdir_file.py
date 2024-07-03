import os

def tree_find(file_path,count,f):
    listdir = os.listdir(file_path)
    for i in listdir:
        if os.path.isdir(f"{file_path}\\{i}"):
            print(f"{count*"  "}ㄴ{i}")
            f.write(f"{count*"  "}ㄴ{i}\n")
            tree_find((file_path+"\\"+i),count+1,f)
        elif os.path.isfile(f"{file_path}\\{i}"):
            print(f"{count*"  "}-{i}")
            f.write(f"{count*"  "}-{i}\n")

file_path = "."
with open("tree_file.txt", 'w', encoding='utf-8') as f:
    print(f"{file_path}")
    f.write(f"{file_path}\n")
    tree_find(file_path, 0,f)