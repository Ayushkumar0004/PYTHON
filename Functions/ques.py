List=[32,21,64,100,13]

def count(List):
    even=0
    odd=0

    for i in List:
        if i%2==0:
            even=even+1
        else:
            odd+=1
    print("The no is:",even)
    print("The no is:",odd)
count(List)             



