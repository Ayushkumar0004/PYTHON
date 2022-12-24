# try:
#     f = open("demo.py")
#     try:
#         f.write("ABC")
#     except:
#         print("Error in file")

#     finally:
#         f.close() 
# except:
#     print("Cant't open the file")     



a = 5
if a < 10:
    raise Exception("Values is less than 10")
