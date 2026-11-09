
name = input("What is your name? ")

print("Welcome", name)

careers = {
    "1": ["Software Developer", "Data Analyst", "Cybersecurity Specialist"],
    "2": ["Accountant", "Financial Analyst", "Auditor"],
    "3": ["Doctor", "Nurse", "Pharmacist"],
    "4": ["Agronomist", "Farm Manager", "Agricultural Engineer"],
    "5": ["Teacher", "Lecturer", "Education Officer"]
}

choice = "yes"

while choice == "yes":

    print("\nChoose your career interest:")
    print("1. Technology")
    print("2. Finance")
    print("3. Healthcare")
    print("4. Agriculture")
    print("5. Education")

    interest = input("Enter your choice (1-5): ")

    if interest in careers:
        print("\nHello", name)
        print("Here are some careers you can explore:")

        for career in careers[interest]:
            print("-", career)

    else:
        print("Invalid choice. Please select 1 to 5.")

    choice = input("\nExplore another category? (yes/no): ").lower()

print("\nThank you", name, "for exploring careers!")
print("Goodbye!")
