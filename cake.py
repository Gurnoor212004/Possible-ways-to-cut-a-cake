n=int(input("Enter number of pieces to cut cake:"))
if (360%n==0):
    print("Yes! Cake can be cut equally into given number of pieces.")
else:
    print("No, Cake can not be cut equally.")
if (n<=360 and n!=0):
    print("Yes! Cake can be cut into given number of pieces.")
else:
    print("No, Cake can not be cut in iven number of pieces.")
if (((n*(n+1)))//2<=360):
    print("Yes! Cake can be cut into given number of pieces such that no piece is equal.")
else:
    print("No, Cake can not be cut into given number of pieces such that no piece is equal.")
