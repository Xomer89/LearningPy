#Reading from a file

print("Opening and closing file")
text_file = open("readit.txt", "r", encoding="utf-8")
text_file.close()

print("\nReading symbols")
text_file = open("readit.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading the whole file")
text_file = open("readit.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nReading rows")
text_file = open("readit.txt", "r", encoding="utf-8")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nReading whole file into a list")
text_file = open("readit.txt", "r", encoding="utf-8")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nReading by rows")
text_file = open("readit.txt", "r", encoding="utf-8")
for line in text_file:
    print(line)
text_file.close()

