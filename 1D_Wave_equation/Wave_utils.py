import numpy as np 

# Define the initial condition
def u_0(x): 
    u = np.sin(np.pi * x) + np.sin(4 * np.pi * x) / 2 
    return u         

def u_true(x, t):
    return np.sin(np.pi * x) * np.cos(2 * np.pi * t) + np.sin(4 * np.pi * x) * np.cos(8 * np.pi * t) / 2 


def test_data(Nx, Nt, x_low, x_up, t_low, t_up): 
    x_test = np.linspace(x_low, x_up, Nx)
    t_test = np.linspace(t_low, t_up, Nt)

    X, T_grid = np.meshgrid(x_test, t_test)
    X = X.reshape(Nx * Nt, 1) # flattens row by row 
    T_grid = T_grid.reshape(Nx * Nt, 1) # flattens row by row 

    X_test = np.concatenate([X, T_grid], axis = 1) 
    u_test = u_true(X_test[:,0:1], X_test[:,1:2])

    return X_test, u_test