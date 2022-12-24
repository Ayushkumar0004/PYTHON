import os

# os.remove("demo.txt")
if os.path.exists("demo1.txt"):
    os.remove("demo1.txt")
else:
    print("File does not exist") 

# except:
#     this will raise the errors

# else:
#     this will execute if there are no errors
# finally:
#     this will execute regardless the result of try and except
              