input_line1="""5 5
1 2 N
LMLMLMLMM"""

# Another input

input_line2="""5 5
3 3 E
MMRMMRMRRM"""

Directions=['N','E','S','W']
global Dir,Coordinate,max
input_list=(input_line1.split('\n'))
max=input_list[0]
pos=input_list[1]
traverse_String=input_list[2]

position=(pos.split(' '))
Coordinate=[]
Coordinate.append(int(position[0]))
Coordinate.append(int(position[1]))

Dir = position[2]

def L(Dir):
    if Coordinate[0] <= int(max[0]) and Coordinate[1] <= int(max[2]) and Dir in Directions:
        Dir = Directions[((Directions.index(Dir) - 1 + 4) % 4)]
    return Dir

def R(Dir):
    if Coordinate[0] <= int(max[0]) and Coordinate[1] <= int(max[2]) and Dir in Directions:
        Dir = Directions[((Directions.index(Dir) + 1) % 4)]
    return Dir

def M(value):

    if value=='N' and Coordinate[0] <= int(max[0]) and Coordinate[1] <= int(max[2]): Coordinate[1]+=1

    if value=='W' and Coordinate[0] <= int(max[0]) and Coordinate[1] <= int(max[2]): Coordinate[0] -= 1

    if value =='E' and Coordinate[0] <= int(max[0]) and Coordinate[1] <= int(max[2]): Coordinate[0] += 1

    if value =='S' and Coordinate[0] <= int(max[0]) and Coordinate[1] <= int(max[2]): Coordinate[1] -= 1
    return 0

for i in traverse_String:
    if(i=='L'):Dir=L(Dir)
    if(i=='R'):Dir=R(Dir)
    if(i=='M'):M(Dir)
print Coordinate, Dir


