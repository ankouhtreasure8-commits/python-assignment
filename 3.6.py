Guest_list=['Norris','Bright','Zutchi','James']
print(f"{Guest_list[0]} ,you are invited")
print(f"{Guest_list[1]} ,you are invited")
print(f"{Guest_list[2]} ,you are invited")
print(f"{Guest_list[3]} ,you are invited")
# james is not able to make it so he told bright spot
Guest_list[1]= "JAMES"
Guest_list[3]=('Bright')
print(Guest_list)
#Replacing James and Bright
Guest_list[0]= "William"
Guest_list[1]= "John"
print(Guest_list)
#New invite list
print(f"{Guest_list[0]} ,you are invited")
print(f"{Guest_list[1]} ,you are invited")
print(f"{Guest_list[2]} ,you are invited")
print(f"{Guest_list[3]} ,you are invited")
#informing People about a bigger dinning set
print("Hello Everyone Are Dinning Space was Larger and Expected So We Will Be including 3 More Persons")
# Adding the 3 New Person's to the list
Guest_list.insert(0,'Roman')
Guest_list.insert(3,'Daniel')
Guest_list.append('Pablo')
print(Guest_list)
# printing out New Invite List After Adding the 3 New Person's
print(f"{Guest_list[0]} ,you are invited")
print(f"{Guest_list[1]} ,you are invited")
print(f"{Guest_list[2]} ,you are invited")
print(f"{Guest_list[3]} ,you are invited")
print(f"{Guest_list[4]} ,you are invited")
print(f"{Guest_list[5]} ,you are invited")
print(f"{Guest_list[6]} ,you are invited")
