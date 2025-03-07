# Read the file
# there is 2 mode of reading a file. normal mode, binary mode
# i have to tell python in which mode i want to read the file





# modes
# r -> read mode
# w -> write mode
# a -> append mode
# r+ -> read and write
# w+ -> write and read
# a+ -> append and read




# Open the file in the read mode
# file = open('filehandling/file.txt', 'r') #relative path, this will give error
# file = open("F:/Python/module15/filehandling/file.txt", "r") #absolute path, this works


# now using the file variable, i can read the file

# method - 1
# read file through loop
# for line in file:
#     print(line)


# method - 2
# print(file.read())


# method - 3
# with open("F:/Python/module15/filehandling/file.txt", "r") as file:
#     for line in file:
#         print(line)



# read only the first x number of characters
# with open("F:/Python/module15/filehandling/file.txt", "r") as file:
#     data = file.read(5)
#     print(data)



# code for writing the file
# file = open('F:/Python/module15/filehandling/file2.txt', 'w')
# file.write('Hello world again ')
# file.write('something')
# # closing the file
# file.close
# # if file is not created already, then it will create. if file is already created, then it will overwrite it



# write with append
# file = open('F:/Python/module15/filehandling/file2.txt', 'a')
# file.write('appending')
# file.write(' ha ha')
# file.close



# code for appending/writing to a file using with
# if i use with, i dont need to explicitly close the file
# with open("F:/Python/module15/filehandling/file3.txt", "w") as file:
#     file.write('Hello Everyone')



# delete the file
# to delete a file, i need to import os module
# import os 
# os.remove('F:/Python/module15/filehandling/file3.txt')