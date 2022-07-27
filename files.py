# Python has functions for creating, reading, updating, and deleting files.

# create and open a file
myFile = open("myFile.txt", "w")
myFile2 = open("myFile.txt", "a")

# get info
# print(f"Name: {myFile.name}")
# print(f"Is Closed: {myFile.closed}")
# print(f"Mode: {myFile.mode}")

# edit file
myFile.writelines("I love JS \n")
myFile.close()
myFile2.write("Python is Awesoem")
myFile.close()
