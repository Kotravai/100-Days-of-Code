
# Error handling and exceptions

# KeyError, TypeError, IndexError, FileNotFoundError

# try:
#     file = open("a_file.txt")
#     a_dict = { "k":"v"}
#     print(a_dict["asdf"])
# except FileNotFoundError: # except occurs only when try makes an error, in this case FileNotFoundError
#     print("File not found")
#     # file = open("a_file.txt", "w")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist")
# else: # Executes when there is no exception
#     content = file.read()
#     print(content)
# finally: # gets executed no matter what
#     raise KeyError("Make Believe")
#     # file.close()
#     # print("file closed")

# # Raising my own Errors
#
# height = float(input("height in m= "))
# weight = int(input("weight: "))
#
# if height > 3:
#     raise ValueError("Not Human height")
#
# bmi = weight / height**2
# print(bmi)





