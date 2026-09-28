import numpy as np 

def interior_points(Nx, Nt, x_low, x_up, t_low, t_up): 
    # interior points 
    length_x = x_up - x_low 
    length_t = t_up - t_low

    x_int_train = length_x * np.random.rand(Nx, 1) + x_low # affine transformation of x-axis 
    t_int_train = length_t * np.random.rand(Nt, 1) + t_low # affine transformation of t-axis 

    X,T = np.meshgrid(x_int_train, t_int_train)

    X_train_int = np.concatenate([X.flatten()[:,None], T.flatten()[:,None]], axis = 1) 
    
    return X_train_int 

def init_points(N_init, x_low, x_up): 
    length_x = x_up - x_low 
    x_init = length_x * np.random.rand(N_init, 1) + x_low # affine transformation of x_axis 
    return x_init 
    
def bc_points(N_bc, t_low, t_up): 
    length_t = t_up - t_low
    t_bc = length_t * np.random.rand(N_bc, 1) + t_low
    return t_bc 

