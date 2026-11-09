
name = input("What is your name? ")

print("Welcome", name)

print("\nChoose your career interest:")
print("1. Technology")
print("2. Finance")
print("3. Healthcare")
print("4. Agriculture")
print("5. Education")

interest = input("\nEnter your choice (1-5): ")

if interest == "1":
    careers = ["Software Developer", "Data Analyst", "Cybersecurity Specialist"]

elif interest == "2":
    careers = ["Accountant", "Financial Analyst", "Auditor"]

elif interest == "3":
    careers = ["Doctor", "Nurse", "Pharmacist"]

elif interest == "4":
    careers = ["Agronomist", "Farm Manager", "Agricultural Engineer"]

elif interest == "5":
    careers = ["Teacher", "Lecturer", "Education Officer"]

else:
    careers = []

if careers:
    print("\nHello", name)
    print("Here are some careers you can explore:")

    for career in careers:
        print("-", career)

else:
    print("Invalid choice. Please select between 1 and 5.")
