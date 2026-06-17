print("Welcome to the pattern genrator and Number analyzer!")
print("\n")

print("Select option")
print("1.Genrate Pattern")
print("2.Analyze a Range of Numbers")
print("3.Exit")
print("\n")

choice = int(input("Enter your choice:"))

print("\n")

match choice:
    case 1:
        j = int(input("enter the end number"))
        print("\n")
        print("Patten:")
        for  v in range(1,j):
            for r in range(v):
                print("*",end=" ")
            print()
        print("\n")
                
    case 2:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        print("\n")
        for l in range(start,end):
             if l % 2 == 0:
                 print("Number",l,"is even")
             else:
                 print("Number",l,"is odd ")
        total = sum(range(start,end + 1))
        print("Sum of all number from",start,"to",end,"is:",total)
        print("\n")
                
    case 3:
        print ("exit")
        print("Exiting the program. Goodbye!")
       
        
