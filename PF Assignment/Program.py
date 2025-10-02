import sys

name = input("Enter your Name: ")
class_name = input("Enter your Class: ")
gmail = input("Enter your Gmail: ")

print("\nLength of your name:", len(name))
print("Length of your Gmail:", len(gmail))

print("\nCount of 'a' in your Name:", name.count("a"))
print("Count of 'a' in your Gmail:", gmail.count("a"))

print("\nMemory size of your Name:", sys.getsizeof(name), "bytes")
print(" Memory size of your Gmail:", sys.getsizeof(gmail), "bytes")
print(" Memory size of your Class:", sys.getsizeof(class_name), "bytes")

print("\n===== Your Details =====")
print("Name:", name)
print("Class:", class_name)
print("Gmail:", gmail)
