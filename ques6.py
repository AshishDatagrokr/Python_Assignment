def gen_number():
    for num in range(INPUT_NUMBER):
        if num % 5 == 0 and num % 7 == 0:
            yield num

s= ""
INPUT_NUMBER = int(input(" Enter number "))
for gen_num in gen_number():
   # print(gen_num, end=",")
    s=s+str(gen_num)+","

print(s[ :-1])

