print("Creating a file with Write()")
text_file = open("Writeit.txt", "w", encoding="utf-8")
text_file.write("Stroka 1\n")
text_file.write("Eto stroka 2\n")
text_file.write("A vot eto uzhe stroka 3\n")
text_file.close()

print("\nReading from created file\n")
text_file = open("Writeit.txt", "r", encoding="utf-8")
print(text_file.read())
text_file.close()

print("\n\nWriting a list into a file")
lines = ["Stroka 1\n",
         "Eto stroka 2\n",
         "A vot eto uzhe stroka 3\n"]
text_file = open("Writeit.txt", "w", encoding="utf-8")
text_file.writelines(lines)
text_file.close()

print("\nReading from created file\n")
text_file = open("Writeit.txt", "r", encoding="utf-8")
print(text_file.read())
text_file.close()
