import csv

# Create CSV file
file = open("address_book.csv", "w", newline="")
writer = csv.writer(file)

# Write column names
writer.writerow(["Name", "Address", "Mobile", "Email"])

# Insert 3 dummy records entered by user
for i in range(3):
    print(f"\nEnter details of person {i+1}")
    
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    mobile = input("Enter Mobile: ")
    email = input("Enter Email: ")

    writer.writerow([name, address, mobile, email])

file.close()

print("\nData saved successfully in address_book.csv")