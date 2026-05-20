import re
print("=== Password Strength Checker ===")
password = input("Enter your password: ")
if len(password) < 8:
    print("❌ Weak Password")
    print("Reason: Password must contain at least 8 characters")
elif not re.search("[A-Z]", password):
    print("❌ Weak Password")
    print("Reason: Add at least one uppercase letter")
elif not re.search("[0-9]", password):
    print("❌ Weak Password")
    print("Reason: Add at least one number")
elif not re.search("[@#$%^&*!]", password):
    print("❌ Weak Password")
    print("Reason: Add at least one special character")
else:
    print("✅ Strong Password")