


str = str (input ("Enter comma separated integers: "))
print ("Input string: ", str)

# conver to the list
Stringlist = str.split (",")
print ("Stringlist: ", Stringlist )

# convert each element as integers
Integer_list = []

for number in Stringlist:
	Integer_list.append(int(number))

# print list as integers
print ("list (Integer_List) : ", Integer_list)

Distinct_Element = []


Distinct_Element = set(Integer_list)

print(Distinct_Element)

print(type(Distinct_Element))


result = []


for element in Integer_list :
    if element in Distinct_Element:
        result.append(element)
        Distinct_Element.remove(element)

print(result)
    



