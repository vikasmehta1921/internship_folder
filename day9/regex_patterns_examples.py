# ============================================
# REGEX PATTERNS EXPLORATION IN PYTHON
# ============================================

# Import Regular Expression Library
import re

# ------------------------------------------------
# 1. Validate Email Address
# ------------------------------------------------

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

emails = [
    "vikas@gmail.com",
    "hello123@yahoo.in",
    "wrong-email@",
    "test@domain"
]

print("EMAIL VALIDATION")
for email in emails:
    if re.match(email_pattern, email):
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")

print("\n")


# ------------------------------------------------
# 2. Validate Mobile Number
# ------------------------------------------------

mobile_pattern = r'^[6-9]\d{9}$'

mobile_numbers = [
    "9876543210",
    "8123456789",
    "5123456789",
    "98765"
]

print("MOBILE NUMBER VALIDATION")
for number in mobile_numbers:
    if re.match(mobile_pattern, number):
        print(number, "-> Valid")
    else:
        print(number, "-> Invalid")

print("\n")


# ------------------------------------------------
# 3. Validate Username
# Rules:
# - Only letters, numbers, underscore
# - Length between 5 to 15
# ------------------------------------------------

username_pattern = r'^[a-zA-Z0-9_]{5,15}$'

usernames = [
    "vikas_123",
    "user",
    "hello_world",
    "vikas@123"
]

print("USERNAME VALIDATION")
for username in usernames:
    if re.match(username_pattern, username):
        print(username, "-> Valid")
    else:
        print(username, "-> Invalid")

print("\n")


# ------------------------------------------------
# 4. Validate Password
# Rules:
# - At least 8 characters
# - One uppercase
# - One lowercase
# - One digit
# - One special character
# ------------------------------------------------

password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

passwords = [
    "Vikas@123",
    "password",
    "HELLO123",
    "Test@2025"
]

print("PASSWORD VALIDATION")
for password in passwords:
    if re.match(password_pattern, password):
        print(password, "-> Strong Password")
    else:
        print(password, "-> Weak Password")

print("\n")


# ------------------------------------------------
# 5. Validate PIN Code (India)
# ------------------------------------------------

pincode_pattern = r'^[1-9][0-9]{5}$'

pincodes = [
    "302001",
    "110011",
    "000123",
    "12345"
]

print("PINCODE VALIDATION")
for pin in pincodes:
    if re.match(pincode_pattern, pin):
        print(pin, "-> Valid")
    else:
        print(pin, "-> Invalid")

print("\n")


# ------------------------------------------------
# 6. Extract Numbers from String
# ------------------------------------------------

text = "My marks are 85, 90 and 78."

numbers = re.findall(r'\d+', text)

print("EXTRACTED NUMBERS")
print(numbers)

print("\n")


# ------------------------------------------------
# 7. Extract Words Starting with Capital Letter
# ------------------------------------------------

sentence = "Vikas lives in Rajasthan and studies Python."

capital_words = re.findall(r'\b[A-Z][a-z]*\b', sentence)

print("WORDS STARTING WITH CAPITAL LETTER")
print(capital_words)

print("\n")


# ------------------------------------------------
# 8. Check Date Format (DD-MM-YYYY)
# ------------------------------------------------

date_pattern = r'^\d{2}-\d{2}-\d{4}$'

dates = [
    "01-06-2026",
    "31-12-2025",
    "2025-12-31"
]

print("DATE VALIDATION")
for date in dates:
    if re.match(date_pattern, date):
        print(date, "-> Valid Format")
    else:
        print(date, "-> Invalid Format")

print("\n")


# ------------------------------------------------
# 9. Find All Hashtags
# ------------------------------------------------

caption = "Learning #Python and #DataScience is fun!"

hashtags = re.findall(r'#\w+', caption)

print("EXTRACTED HASHTAGS")
print(hashtags)

print("\n")


# ------------------------------------------------
# 10. Remove Extra Spaces
# ------------------------------------------------

text = "Python      is      very      powerful."

clean_text = re.sub(r'\s+', ' ', text)

print("TEXT AFTER REMOVING EXTRA SPACES")
print(clean_text)

print("\n")


# ------------------------------------------------
# 11. Validate URL
# ------------------------------------------------

url_pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9\-]+\.[a-z]{2,}(\S*)?$'

urls = [
    "https://google.com",
    "www.youtube.com",
    "invalid_url"
]

print("URL VALIDATION")
for url in urls:
    if re.match(url_pattern, url):
        print(url, "-> Valid URL")
    else:
        print(url, "-> Invalid URL")

print("\n")


# ------------------------------------------------
# 12. Split Sentence into Words
# ------------------------------------------------

sentence = "Python is easy to learn"

words = re.split(r'\s+', sentence)

print("WORDS AFTER SPLIT")
print(words)

print("\n")


# ------------------------------------------------
# 13. Find Repeated Words
# ------------------------------------------------

text = "hello hello world world python"

repeated = re.findall(r'\b(\w+)\s+\1\b', text)

print("REPEATED WORDS")
print(repeated)

print("\n")


# ------------------------------------------------
# 14. Replace Digits with *
# ------------------------------------------------

text = "My ATM PIN is 4589"

hidden = re.sub(r'\d', '*', text)

print("HIDDEN DIGITS")
print(hidden)

print("\n")


# ------------------------------------------------
# 15. Extract Domain Name from Email
# ------------------------------------------------

email = "vikas@gmail.com"

domain = re.search(r'@([a-zA-Z0-9.-]+)', email)

print("DOMAIN NAME")
print(domain.group(1))