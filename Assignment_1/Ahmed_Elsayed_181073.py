import numpy as np

def degree_To_radian(degree):
    return (degree * np.pi/180)


def Rotation_about_X(angle):
    mat_x = np.array([
                        [1,0,0],
                        [0,np.cos(angle),-np.sin(angle)],
                        [0,np.sin(angle),np.cos(angle)]
                    ])
    return np.round(mat_x,3)


def Rotation_about_Y(angle):
    mat_y = np.array([
                        [np.cos(angle),0,np.sin(angle)],
                        [0,1,0],
                        [-np.sin(angle),0,np.cos(angle)]
                    ])
    return np.round(mat_y,3)

def Rotation_about_Z(angle):
    mat_z = np.array([
                        [np.cos(angle),-np.sin(angle),0],
                        [np.sin(angle),np.cos(angle),0],
                        [0,0,1]
                    ])
    return np.round(mat_z,3)

def Transformation_matrix(Rotation=np.identity(3),Position=np.zeros([1,3])):
    T_matrix = np.identity(4)
    T_matrix[0:3,0:3] =  Rotation
    T_matrix[0:3,3] =  Position.reshape(1,3) 
    return (np.round(T_matrix,3))

print("Homogeneous Transformation Matrix of frame {A} relative to frame {O}\n")
print("O_T_A = \n",Transformation_matrix( Rotation_about_X(degree_To_radian(180)) , np.array([8,0,0]) ),"\n" )

print("Homogeneous Transformation Matrix of frame {O} relative to frame {A}\n")
print("A_T_O = \n",np.linalg.inv(Transformation_matrix( Rotation_about_X(degree_To_radian(180)) , np.array([8,0,0]))),"\n")

old_frame = Transformation_matrix()
new_frame = Transformation_matrix()

R_Z_90 = Rotation_about_Z(degree_To_radian(90))

Trans_old_y = np.array([0,3,0])
Trans_new_X = np.array([3,0,0])

Trans_old_y[0] = 5 
Trans_new_X[1] = 5

new_frame = Transformation_matrix(R_Z_90,Trans_new_X)
new_frame = Transformation_matrix(R_Z_90,Trans_old_y)






#print(Transformation_matrix())


