# creating a file
with open('randomFile.txt', 'w') as my_file:
  my_file.write("This is a new file I am creating\n")
  my_file.write("The file is in a pdf format\n")
  my_file.write("I have some contents in the file\n")

# program to be able to read the file
with open('randomFile.txt', 'r') as my_file:
  content = my_file.read()
print(content)

# convert content in the file to a modified version
modified_content = content.upper()
print(modified_content)

# saving modified version to a new file
with open('modified_file.txt', 'w') as new_file:
  new_file.write("=== PROCESSED FILE ===\n")
  new_file.write(modified_content) 

# asking a user to enter a file name
file_name = input("Enter the name of the file here.\n")
try:
  with open(file_name, 'r') as my_file:
    data = my_file.read()
    print(f"File {file_name} opened successfully.")
except FileNotFoundError:
  print("File not found. Please check the filename.")

