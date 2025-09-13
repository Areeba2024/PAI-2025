def dictionary(list1,list2):
    if len(list1) != len(list2):
        print("List sizes don't match!")
    else:
        result = dict(zip(list1,list2))
        print(result)

ids = ['001','002','003','004']
names = ['ali','saad','raza','ahmed']
dictionary(ids, names)