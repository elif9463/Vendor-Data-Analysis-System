vendor_data=[]
with open("Hotdogs.txt", "r") as file:
    for line in file:
        items=line.strip().split(",")
        vendor_data.append(items)
for vendor in vendor_data:
    print(vendor)
