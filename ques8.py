value =[]
for number in range(1,21):
    value.append(number)
squaredNumbers = map(lambda x: x**2, value)
print (list(squaredNumbers))
