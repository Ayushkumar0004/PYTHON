# f = open("demo.txt","r")
# print(f.read())
# print(f.readline())
# print(f.readline())
# f1 = open("demo.text","w")
# f1.write("this is a new file")

# f2 = open("myself.txt","w")
# f2.write("My name is AYUSH")
# f2.write("Pursue B.Tech cse from LPU")
# for i in f:
#     f2.write(i)

# try:
#     f = open("demo.txt")
# finally:
#     f.close()
#this way we are making sure that file is closed properly
# even if exception is raised  that acuse the program  flow to stop
# with open("demo1.txt") as f:
#     f.read() #--> example
    #your code goes here
f = open("demo.txt","r")
print(f.read(10))
print(f.tell()) 
