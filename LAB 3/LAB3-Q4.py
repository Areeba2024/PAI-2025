def dictionary(list1, list2):
    if len(list1) != len(list2):
        print("List sizes don't match!")
    else:
        result = {}
        for i in range(len(list1)):
            result[list1[i]] = list2[i]
        print("Dictionary created:", result)

list1 = input("Enter the first list elements separated by space: ").split()
list2 = input("Enter the second list elements separated by space: ").split()

dictionary(list1, list2)
