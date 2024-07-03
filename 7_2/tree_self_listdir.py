import os

def tree_find(file_path,count):
    listdir = os.listdir(file_path)
    for i in listdir:
        if os.path.isdir(f"{file_path}\\{i}"):
            print(f"{count*"  "}ㄴ{i}")
            tree_find((file_path+"\\"+i),count+1)
        elif os.path.isfile(f"{file_path}\\{i}"):
            print(f"{count*"  "}-{i}")

file_path = "."
print(f"{file_path}")
tree_find(file_path, 0)