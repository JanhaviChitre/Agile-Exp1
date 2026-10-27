name = input("Enter student name: ")
email = input("Enter student email: ")

if name.strip() and "@" in email and "." in email:
print("Student details are valid.")
else:
print("Invalid student details.")
