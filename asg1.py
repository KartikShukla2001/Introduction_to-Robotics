import numpy as np
import math

# coor = list(map(float , input('Enter coordinates of the point:').split(' ')))
# xt , yt, zt = [int(x) for x in input('Enter the translations for x,y,z:').split(' ')]
# theta_x = float(input('Enter rotation about x-axis:')) * math.pi / 180
# theta_y = float(input('Enter rotation about y-axis:')) * math.pi / 180
# theta_z = float(input('Enter rotation about z-axis:')) * math.pi / 180

xt , yt, zt = 0, 0, 0
t_x = 30 * math.pi / 180
t_y = 30 * math.pi / 180
t_z = 30 * math.pi / 180
coor = [2,3,0]

r_x = [ [ 1,0,0],
[0 , math.cos(t_x) , -math.sin(t_x)],
[0 , math.sin(t_x) , math.cos(t_x)],]

r_y = [ [math.cos(t_y) ,0,math.sin(t_y)],
[0 , 1 , 0],
[-math.sin(t_y) , 0 , math.cos(t_y)],]

r_z = [ [ math.cos(t_z), -math.sin(t_z),0],
[math.sin(t_z) , math.cos(t_z) , 0],
[0 , 0 , 1],]

r_x = np.array(r_x)
r_y = np.array(r_y)
r_z = np.array(r_z)

r = ((r_x @ r_y) @ r_z)

transformation_matrix = [[r[0][0] , r[0][1],r[0][2],xt],
[r[1][0] , r[1][1],r[1][2],yt],
[r[2][0] , r[2][1],r[2][2],zt],
[0 ,0 ,0 ,1]]

coor.append(1.0)
coor = np.array(coor)

transformation_matrix = np.array(transformation_matrix)
sol = transformation_matrix @ coor
print('Solution Matrix:\n')
print(sol)
