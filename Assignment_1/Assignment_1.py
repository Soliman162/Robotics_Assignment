#%matplotlib qt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
#import pylab as plt   # for figure
import matplotlib.pyplot as plt

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


def trplot(Tr, origin=np.array([0,0,0]),frame=None,s=1, fig_name="",line="-", lenlim=10, color=None):
    '''
    Plot a rotation as a set of axes aligned with the x, y and z
    directions of a frame rotated by C{r}.
    '''
    
    R=Tr[0:3,0:3]# RB_O
    origin= Tr[0:3,3]# frame origin x0,y0,z0
    
    px=R @ np.array([lenlim,0,0]).T # px represented in O 
    py=R @ np.array([0,lenlim,0]).T
    pz=R @ np.array([0,0,lenlim]).T
    x0=origin[0]
    y0=origin[1]
    z0=origin[2]
    
    if color==None:
        xcolor="red"
        ycolor='green'
        zcolor="blue"
        pcolor="black"
    else:
        xcolor = ycolor = zcolor= pcolor=color
            
    
    #name of the axis ..if no frame name given axes will be just x,y,z withot frame name
    # else will get the frame name
    if frame==None:
        xlbl,ylbl,zlbl='x','y','z'
    else :
        xlbl=f'x{frame}'
        ylbl=f'y{frame}'
        zlbl=f'z{frame}'
    
    ## check if there is exists a  fig , in case if we need to add a plot in the current figure
    if plt.fignum_exists(fig_name):
        fig=plt.figure(fig_name)
        ax=fig.axes[0]
    else:
        fig=plt.figure(fig_name)
        ax=p3.Axes3D(fig)
        delta=(lenlim*10/100)
        ax.set_xlim3d(-lenlim-delta, lenlim+delta)
        ax.set_ylim3d(-lenlim-delta, lenlim+delta)
        ax.set_zlim3d(-lenlim-delta, lenlim+delta)
        
    
    ## plot 3d quiver
    Xaxis=ax.quiver(x0, y0, z0, s*px[0], s*px[1], s*px[2], color=xcolor, alpha=1, linestyles=line)
    Yaxis=ax.quiver(x0, y0, z0, s*py[0], s*py[1], s*py[2], color=ycolor, alpha=1, linestyles=line)
    Zaxis=ax.quiver(x0, y0, z0, s*pz[0], s*pz[1], s*pz[2], color=zcolor, alpha=1, linestyles=line)
    ##plot point at the origin
    ax.scatter(x0, y0,z0, marker='o', color=pcolor)
    ## write text annotation
    tx1=ax.text(s*px[0]+x0, s*px[1]+y0, (s*px[2]+z0),  xlbl , size=12,zorder=2,   color=xcolor) 
    tx2=ax.text(s*py[0]+x0, s*py[1]+y0, (s*py[2]+z0),  ylbl , size=12,zorder=2,  color=ycolor) #zorder=2, 
    tx3=ax.text(s*pz[0]+x0, s*pz[1]+y0, (s*pz[2]+z0),  zlbl , size=12,zorder=2,   color=zcolor)
    plt.ion()
    fig.canvas.draw()
    fig.canvas.flush_events()

O_T_A = Transformation_matrix( Rotation_about_X(degree_To_radian(180)) , np.array([8,0,0]) )
print("Homogeneous Transformation Matrix of frame {A} relative to frame {O}\n")
print("O_T_A = \n",O_T_A,"\n" )
trplot(O_T_A,frame=2, line="-.", color="black")

A_T_O = np.linalg.inv(Transformation_matrix( Rotation_about_X(degree_To_radian(180)) , np.array([8,0,0])))
print("Homogeneous Transformation Matrix of frame {O} relative to frame {A}\n")
print("A_T_O = \n",A_T_O,"\n")
trplot(A_T_O,frame=2, line="-.", color="black")

ROT_Z = Rotation_about_Z(degree_To_radian(90))
Trans = np.array([5,3,0])
H_3_0 = Transformation_matrix(ROT_Z,Trans)
print("H_3_0 = \n",H_3_0)
trplot(H_3_0,frame=2, line="-.", color="black")



