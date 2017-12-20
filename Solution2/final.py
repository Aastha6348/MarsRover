import Rover,Traverse

input_data = ['5 5','1 2 N','LMLMLMLMM']

# input_data = ['5 5','3 3 E','MMRMMRMRRM']
Rover = Rover.Rover()
Rover.set_data(input_data)
data=Rover.get_data()

max=data[0]
data.pop(0)

Traverse = Traverse.Traverse(data)
Traverse.get_Coordinates()

for i in Traverse.get_TraverseString():
    if (i == 'L'): Traverse.L()
    if (i == 'R'): Traverse.R()
    if (i == 'M'): Traverse.M()

print Traverse.printdata()
