list1 = [10,20,30,40,50,60,70,80,90,100]

while True:
    print("LIST OPERATIONS MENU")
    print("1.Append an element")
    print("2.Insert an element")
    print("3.Append a list to existing list")
    print("4.Modify an existing element")
    print("5.Delete element using position")
    print("6.Delete element using value")
    print("7.Sort list in ascending order")
    print("8.Sort list in descending order")
    print("9.Display the list")
    print("10.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ele = input("Enter element: ")
        list1.append(ele)
        print("Element appended successfully")


    elif choice == 2:
        pos = int(input("Enter position: "))
        ele = input("Enter element: ")
        list1.insert(pos, ele)
        print("Element inserted successfully")

    elif choice == 3:
        newlist = input("Enter list elements separated by space: ").split()
        list1.extend(newlist)
        print("List appended successfully")

    elif choice == 4:
        pos = int(input("Enter position to modify: "))
        ele = input("Enter new element: ")
        list1[pos] = ele
        print("Element modified successfully")

    elif choice == 5:
        pos = int(input("Enter position to delete: "))
        list1.pop(pos)
        print("Element deleted successfully")

    elif choice == 6:
        ele = input("Enter value to delete: ")
        list1.remove(ele)
        print("Element deleted successfully")

    elif choice == 7:
        list1.sort()
        print("List sorted in ascending order")

    elif choice == 8:
        list1.sort(reverse=True)
        print("List sorted in descending order")

    elif choice == 9:
        print("Current List:", list1)

    elif choice == 10:
        print("Program exited")
        break
    else:
        print("Invalid Choice")