class Reverselter:
    def __init__(self,value):
        for number in range(len(value)-1,-1,-1):
            print(value[number])
value=[11,12,13,14,15]
Reverselter(value)
