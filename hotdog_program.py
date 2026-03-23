vendor_data=[]
with open("Hotdogs.txt", "r") as file:
    print(file.read())


hotdog_data=[]
with open("Hotdogs.txt", "r") as file:
    for line in file:
        items=line.strip().split(",")
        hotdog_data.append(items)
