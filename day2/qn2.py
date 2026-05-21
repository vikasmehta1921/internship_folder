str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + " " + str2

print("Concatenated String:", result)

print("Lower:", result.lower())
print("Upper:", result.upper())
print("Title:", result.title())
print("Swapcase:", result.swapcase())
print("Capitalize:", result.capitalize())
print("Casefold:", result.casefold())
print("Center:", result.center(50, "*"))
print("Count of 'a':", result.count("a"))
print("Endswith 'a':", result.endswith("a"))
print("Find 'a':", result.find("a"))
print("Isalnum:", result.isalnum())
print("Isdigit:", result.isdigit())
print("Isnumeric:", result.isnumeric())
print("Isspace:", result.isspace())
print("Replace:", result.replace("a", "@"))
