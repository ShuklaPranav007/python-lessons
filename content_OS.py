import os

directory_path = "/Program Files/__phello__"

contents = os.listdir(directory_path)

for items in contents:
    print(items)