import sys
name = input("Enter your Name: ")
program = input("Enter your Program Name: ")
age = input("Enter your Age: ")
gmail = input("Enter your Gmail: ")
university = input("Enter your University Name: ")

print("\n Student Information System ")

print("\n Length of your Name:", len(name))
print(" Length of your Gmail:", len(gmail))
print(" Length of your University Name:", len(university))

print("\n Count of 'a' in your Name:", name.count("a"))
print(" Count of '@' in your Gmail:", gmail.count("@"))
print(" Count of 's' in your Program Name:", program.lower().count("s"))

print("\n Memory size of your Name:", sys.getsizeof(name), "bytes")
print(" Memory size of your Program:", sys.getsizeof(program), "bytes")
print(" Memory size of your Gmail:", sys.getsizeof(gmail), "bytes")
print(" Memory size of your University:", sys.getsizeof(university), "bytes")
