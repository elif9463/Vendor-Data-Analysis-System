# --- Vendor Data Analysis System --- 

# requirement 1- reads vendor data from Hotdogs.txt, splits each line into fields 
# and stores records in a list for later analysis (requirement 2)

# Load data

vendor_data=[]
with open("Hotdogs.txt", "r") as file:
    print("Vendor data:")
    for line in file:
        items=line.strip().split(",")
        vendor_data.append(items)
for vendor in vendor_data:
    print(vendor)

# Requirement 3- Validation of data
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

original_data = valid_data
quick_data = original_data.copy()
bubble_data = original_data.copy()

# Requirement 4- Searching the data (Linear search with partial and case insensitive matching)

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

# Requirement 5: Quick sort algorithm to sort vendor data

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

# Requirement 6 - Bubble sort

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

# Requirement 7 - Linear search on sorted data

print("\n--- Linear Search on Sorted Data ---")

while True:
    search_name = input("enter vendor name to search, type 'exit' to quit: ").strip()

    if search_name.lower() == "exit":
        break

    found = False
    
    # case insensitive partial match on vendor name (index 1)
    for record in bubble_sorted_data:
        if search_name.lower() in record[1].lower():
            print(record)
            found = True

    if not found:
        print("No matching records found")

# Requirement 8 - Binary search

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

# Requirement 9: Comparing search efficiency

search_name = input("Enter vendor name to test timing: ")

# Linear search timing
                    
import time

# Linear search timing
start = time.time() # records start time before search begins

# loop through all records in dataset (linear search process)
for record in valid_data:
    # checks if search term is contained in vendor name (case insensitive)
    if search_name.lower() in record[1].lower():
        pass # no output needed, just measuring time

end = time.time() # records end time after search completes 

linear_time = end - start # calculates total time taken for linear search 

# displays result to 6 dp
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

# Requirement 10: Comparing sort efficiency 

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

# Requirement 11: Analysing vendor data

print("\n--- Vendor Data Analysis---")
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

# get total hotdogs value
most_productive_value = vendor_totals[most_productive]

print("\nMost productive vendor:",
      most_productive,
      "(",
      most_productive_value,
      "hotdogs )")

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
least_ketchup_value = ketchup_totals[least_ketchup_vendor]
print("\nVendor with least ketchup usage:",
      least_ketchup_vendor,
      "(", least_ketchup_value, "litres )")

# find busiest week with highest total hotdog sales

# dictionary to store total hotdogs per week
week_totals = {}

# loop through each record in dataset
for record in valid_data:
    week = record[2]
    hotdogs = int(record[3]) + int(record[4])

    # if week already exists in dictionary, add to it
    if week in week_totals:
        week_totals[week] += hotdogs
    else: # otherwise create new entry for that week
        week_totals[week] = hotdogs
        
# find week with highest total sales    
busiest_week = max(week_totals, key=week_totals.get)

# split the combined code into readable year and week
year = str(busiest_week)[:4]
week = str(busiest_week)[4:]

# display result with week and year separated
print("\nBusiest week: Week", week, "of year", year) 

# requirement 12 - Save results to output file

# open a new text file in write mode (creates file if it doesn't exist)
with open("analysis_results.txt", "w") as file:

    # title and header for readability
    file.write("Vendor data analysis results\n")
    file.write("--------------------------------\n\n")

    # write most productive vendor and its total hotdogs
    file.write("Most productive vendor: " + most_productive +
               " (" +str(most_productive_value) + " hotdogs)\n")

    # write total vegan and meat hotdogs across all vendors
    file.write("Total vegan hotdogs: " +str(vegan_total) + "\n")
    file.write("Total meat hotdogs: " + str(meat_total) + "\n\n")

    # write vendor wtih least ketchup usage and its value
    file.write("Vendor with least ketchup usage: " +
               least_ketchup_vendor +
               " (" + str(least_ketchup_value) + " litres)\n")
    
