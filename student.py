def validate_student(name, email):
    return bool(name) and "@" in email

print(validate_student("Janhavi", "janhavi@example.com"))