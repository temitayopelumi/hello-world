def sumt(ar):
    return sum(ar)

def prompt():
    while True:
        try:
            return int(input())
            break
        except ValueError:
            print("Enter an integer")
ar=[]
print("Enter the number of elements in the list:")
n=prompt()
if n > 0 and n<=1000:
    for i in range(n):
        print("Enter the numbers in the list")
        p=prompt()
        ar.append(p)

    print(sumt(ar))
else:
    print("number of element is list is out of range")

