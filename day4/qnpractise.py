file = open("sample.txt", "w")
file.write("Hello World\n")
file.write("Python File Handling")
file.close()

file = open("sample.txt", "r")
print("Reading File:")
print(file.read())
file.close()

file = open("sample.txt", "a")
file.write("\nThis line is appended.")
file.close()

file = open("sample.txt", "r")
print("\nAfter Appending:")
print(file.read())
file.close()