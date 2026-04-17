# requirement 1- reads vendor data from Hotdogs.txt, splits each line into fields and stores records in a list for later analysis
vendor_data=[]
with open("Hotdogs.txt", "r") as file:
    for line in file:
        items=line.strip().split(",")
        vendor_data.append(items)
for vendor in vendor_data:
    print(vendor)

valid_data=[]
for record in vendor_data:
    try:
        vendor_id=record[0]
        name=record[1]
        week=record[2]
        hotdogs=int(record[3])
        onions=float(record[5])
        ketchup=float(record[6])

        valid=True

        #ID format check
        if not (len(vendor_id)==6 and
                vendor_id[:2].isalpha and vendor_id[:2].isupper and
                vendor_id[2]== "_" and
                vendor_id[3:].isdigit()):
            valid=False
            
        #Name length check
        if len(name)<2 or len(name)>25:
            valid=False

        #Week format check
        if not (len(week)==6 and week.isdigit() and 1 <= int(week[4:])<=52):
            valid=False
            

        #Vegan hotdogs divisible by 10
            if vegan_hotdogs%10 !=0:
                valid=False
            
        #Meat hotdogs divisible by 10
            if meat_hotdogs%10 !=0:
                valid=False
        
        #Onions in 0.5 increments
            if onions *2 != int(onions *2):
                valid=False

        #Ketchup range check(1-4)
            if ketchup <1 or ketchup>4:
                valid=False
                    

        if valid:
            valid_data.append(record)
        else:
            print("invalid record:",record)
    except:
        print("invalid record found:",record)
print("Valid records:")
for v in valid_data:
    print(v)
