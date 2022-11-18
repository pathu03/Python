import math
def input_clac(height,widht,cover):
    area=height*widht
    num_of_cans=math.ceil(area/cover)
    print(num_of_cans)

height=int(input("h"))
widht=int(input("w"))
cover=5
input_clac(height,widht,cover)