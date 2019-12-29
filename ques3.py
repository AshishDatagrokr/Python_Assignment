""" user input """

STRING = str(input("Enter comma separated integers: "))
print("Input string: ", str)


STRING_LIST = STRING.split(",")
print("Stringlist: ", STRING_LIST)

# convert each element as integers
INTEGER_LIST = []

for number in STRING_LIST:
    INTEGER_LIST.append(int(number))
print("list (Integer_List) : ", INTEGER_LIST)

DISTINCT_ELEMENT = []


DISTINCT_ELEMENT = set(INTEGER_LIST)

print(DISTINCT_ELEMENT)
print(type(DISTINCT_ELEMENT))

RESULT = []
for element in INTEGER_LIST:
    if element in DISTINCT_ELEMENT:
        RESULT.append(element)
        DISTINCT_ELEMENT.remove(element)
print(RESULT)
