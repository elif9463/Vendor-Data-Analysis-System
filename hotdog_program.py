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

print("\n--- SORTING ---")
original_data = valid_data
quick_data = original_data.copy()
bubble_data = original_data.copy()

# Linear search with partial and case insensitive matching
print("\n--- Linear search on unsorted data ---")

# loop allows repeated searches until user exits
while True:
    search_name=input("Enter a vendor name to search, type 'exit' to quit: ")

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
quick_sorted_data = quick_sort(valid_data)

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

# binary search on sorted data
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    target = target.lower()

    #continue searching while there is a valid range
    while low <= high:

        #find the middle index
        mid = (low + high) // 2

        # get vendor name at midpoint
        mid_name = data[mid][1].lower()

        if mid_name == target:
            results = [data[mid]]

            # check records before midpoint
            i = mid - 1
            while i >= 0 and data[i][1].lower() == target:
                results.append(data[i])
                i -= 1

            # check records after midpoint
            i = mid + 1
            while i < len(data) and data[i][1].lower() == target:
                results.append(data[i])
                i += 1
                
            return results
        
        # search right half if target is greater
        elif mid_name < target:
            low = mid + 1
            
        # otherwise search left half 
        else:
            high = mid - 1
            
    return None

print("\n--- Binary Search ---")

# loop allows repeated searches until user exits
while True:
    search_name = input("Enter vendor name to search(exact match), type 'exit' to quit: ").strip()

    if search_name.lower() == "exit":
        break

    # call binary search on sorted data
    result = binary_search(quick_sorted_data, search_name)

    if result:
        # print all matching records returned
        for record in result:
            if record[1].lower() == search_name.lower():
                print(record)
    else:
        print("no matching records found")

# --- Linear Search Timing ---
import time

start = time.time() # record start time

# perform linear search on unsorted data
for record in valid_data:
    if search_name.lower() in record[1].lower():
        pass # simulate search without printing
    
end = time.time() # record end time

# calculate total time taken
linear_time = end-start
print("\nLinear search time:", format(linear_time, ".6f"), "seconds")


# --- Binary Search Timing ---

start = time.time()

# perform binary search on sorted data
result = binary_search(quick_sorted_data, search_name)
end = time.time()

binary_time = end - start
print("Binary search time:", format(binary_time, ".6f"), "seconds")

# print the faster result
if linear_time < binary_time:
    print("Linear search was faster")
elif binary_time < linear_time:
    print("Binary search was faster")


# make copies so both sorts use the same data
bubble_data = valid_data.copy()
quick_data= valid_data.copy()

# --- Bubble Sort Timing ---
start = time.time()

bubble_sorted = bubble_sort(bubble_data)

end = time.time()
bubble_time = end - start

print("\nBubble sort time:", format(bubble_time, ".6f"), "seconds")

# --- Quick Sort Timing ---
start = time.time()

quick_sorted = quick_sort(quick_data)

end = time.time()
quick_time = end - start

print("Quick sort time:", format(quick_time, ".6f"), "seconds")

# print faster result
if quick_time < bubble_time:
    print("Quick sort was faster")
elif bubble_time < quick_time:
    print("Bubble sort was faster")

# --- Vendor Data Analysis ---

# Most productive vendor (highest total hotdogs)
vendor_totals = {}

for record in valid_data:
    name = record[1]
    hotdogs = int(record[3])

    # accumulate total per vendor
    if name in vendor_totals:
        vendor_totals[name] += hotdogs
    else:
        vendor_totals[name] = hotdogs
        
# find vendor with highest total
most_productive = max(vendor_totals, key=vendor_totals.get)
print("\nMost productive vendor:", most_productive)

# Total vegan vs meat hotdogs (across both vendors)
vegan_total = 0
meat_total = 0

for record in valid_data:
    # column 3 = vegan, column 4 = meat
    vegan_total += int(record[3])
    meat_total += int(record[4])

print("\nTotal vegan hotdogs:", vegan_total)
print("Total meat hotdogs:", meat_total)

# vendor with least ketchup usage
ketchup_totals= {}

for record in valid_data:
    name = record[1]
    ketchup = float(record[6])

    # accumulate total ketchup per vendor
    if name in ketchup_totals:
        ketchup_totals[name] += ketchup
    else:
        ketchup_totals[name] = ketchup

# find vendor with lowest total ketchup usage
least_ketchup_vendor = min(ketchup_totals, key=ketchup_totals.get)
print("Vendor with least ketchup usage:", least_ketchup_vendor)
