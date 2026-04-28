"""Program to load, validate and search vendor data"""

# requirement 1- reads vendor data from Hotdogs.txt, splits each line into fields and stores records in a list for later analysis

# Load data

vendor_data=[]
with open("Hotdogs.txt", "r") as file:
    print("Vendor data:")
    for line in file:
        items=line.strip().split(",")
        vendor_data.append(items)
for vendor in vendor_data:
    print(vendor)

# Validate data
valid_data = []

for record in vendor_data:
    try:
        vendor_id = record[0]
        name = record[1]
        week = record[2]
        vegan_hotdogs = int(record[3])
        meat_hotdogs = int(record[4])
        onions = float(record[5])
        ketchup = int(record[6])

        valid = True

        # Vendor ID format check
        if not (
            len(vendor_id) == 6 and
            vendor_id[:2].isalpha() and
            vendor_id[:2].isupper() and
            vendor_id[2] == "_" and
            vendor_id[3:].isdigit()
        ):
            valid = False

        # Name length check
        if len(name) < 2 or len(name) > 25:
            valid = False

        # Week format YYYYWW, WW 01–52
        if not (week.isdigit() and len(week) == 6):
            valid = False
        else:
            if not (1 <= int(week[4:]) <= 52):
                valid = False

        # Vegan hotdogs divisible by 10
        if vegan_hotdogs % 10 != 0:
            valid = False

        # Meat hotdogs divisible by 10
        if meat_hotdogs % 10 != 0:
            valid = False

        # Onions in 0.5 increments
        if onions * 2 != int(onions * 2):
            valid = False

        # Ketchup between 1 and 4
        if ketchup < 1 or ketchup > 4:
            valid = False

        if valid:
            valid_data.append(record)
        else:
            print("Invalid record:", record)

    except (ValueError, IndexError) as e:
        print("Error in record:", record, "|", e)

# Output results
print("\nValid records:")
for v in valid_data:
    print(v)

# Linear search on unsorted data with partial and case insensitive matching

# loop allows repeated searches until user exits
while True:
    search_name=input("Enter a vendor name to search, type 'exit' to quit")

    # allow user to exit the search loop
    if search_name.lower() == "exit":
        break
    found = False

    # check if user input matches vendor name 
    for record in valid_data:
        if search_name.lower() in record [1].lower():
            print(record)
            found = True
            
    #inform user if no matches found
    if not found:
        print("no matching records found")

def quick_sort(data):
    # base case- if list has 0 or 1 item it's already sorted
    if len(data) <= 1:
        return data
    
    # choose first item as pivot
    pivot = data[0]

    # lists to hold values smaller and larger than pivot
    left = []
    right = []

    # compare each item
    for item in data[1:]:
        if item[1].lower() < pivot[1].lower():
            left.append(item)
        else:
            right.append(item)

    # recursively sort left and right sides, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)

# apply quick sort to validated dataset
sorted_data = quick_sort(valid_data)

# Bubble Sort
def bubble_sort(data):
    n = len(data)

    for i in range(n):
        # compare adjacent items in each pass
        for j in range(0, n - i -1):
            # compare vendor names (index 1)
            if data[j][1].lower() > data[j + 1][1].lower():
                data[j], data[j + 1] = data[j +1], data[j]
    return data

# apply bubble sort to a copy of the original data
bubble_sorted_data = bubble_sort(bubble_data)

# Linear search on sorted data
print("\n--- Linear Search on Sorted Data ---")

while True:
    search_name = input("enter vendor name to search, type 'exit' to quit: ").strip()

    if search_name.lower() == "exit":
        break

    found = False
    
    # case insensitive partial match on vendor name (index 1)
    for record in sorted_data:
        if search_name.lower() in record[1].lower():
            print(record)
            found = True

    if not found:
        print("No matching records found")








