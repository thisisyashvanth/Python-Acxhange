from pathlib import Path

directory = Path(r"C:\Users\YashvanthVijayabalaj\Documents\Learnings\Tasks\Python\FileHandling")

file_list = [i for i in directory.iterdir() if i.is_file()]
directory_list = [i for i in directory.iterdir() if i.is_dir()]

# file_list = []
# directory_list = []
# for item in directory.iterdir():
#     if item.is_file():
#         file_list.append(item)
#     elif item.is_dir():
#         directory_list.append(item)

with open(file="FilesList.txt", mode="w") as f:
    f.write("\n".join(i.name for i in directory.iterdir() if i.is_file()))

file_types = {}

for item in directory.iterdir():
    if item.is_file():
        
        if item.suffix not in file_types:
            file_types[item.suffix] = []
        
        file_types[item.suffix].append(item.name)

with open("GroupedFiles.txt", "w") as f:
    for k, v in file_types.items():
        f.write(f"\n{k} files:\n")
        for name in v:
            f.write(name + "\n")

max_size = 100 * 1024 * 1024
with open("FileSize.txt", "w") as f:
    for item in directory.iterdir():
        if item.is_file():
            size = item.stat().st_size
            
            if size > max_size:
                mb = size/(1024*1024)
                f.write(f"\nFiles Greater than 100MB\n{item.name} - {mb:.2f} MB")