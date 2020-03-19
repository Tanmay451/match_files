import os

file_path = []

for root, dirs, files in os.walk("./to_be_scan"):
    for file in files:
        if file.endswith(""):
             file_path.append(os.path.join(root, file))

if len(file_path) == 0:
    print("No file")
    
if len(file_path) < 2:
    print("Nothing to compair")

def match_file(file1, file2):
    file1 = open(file_path[i],"r")
    file2 = open(file_path[j],"r")
    for line1 in file1:
        for line2 in file2:
            if line1 == line2:
                print(line1,line2,"SAME")
            else:
                print(line1,line2,"DIFF")

print("Number of files: ",len(file_path))

for i in range(len(file_path)):
    for j in range(i,len(file_path)):
        if i != j:
            match_file(i,j)



        

