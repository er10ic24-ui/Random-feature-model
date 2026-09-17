import numpy as np 

def interior_points(N_x, N_y, x_low, x_up, y_low, y_up): 
    # Generate interior and boundary points on an interval (lb, ub)
    length_x = x_up - x_low 
    length_y = y_up - y_low
    
    x_int_train = length_x * np.random.rand(N_x, 1) + x_low # affine transformation of x-axis 
    y_int_train = length_y * np.random.rand(N_y, 1) + y_low # affine transformation of t-axis 
    X,Y = np.meshgrid(x_int_train, y_int_train)
    X_train_int = np.concatenate([X.flatten()[:,None], Y.flatten()[:,None]], axis = 1) 
    return X_train_int 

def bc_points(N_bc, x_low, x_up, y_low, y_up):
    length_x = x_up - x_low
    length_y = y_up - y_low 
    
    Bc = np.ones((N_bc, 1))  
    y_left = length_y * np.random.rand(N_bc, 1) + y_low 
    X_left = np.concatenate((x_low * Bc, y_left), axis = 1) 
    y_right = length_y * np.random.rand(N_bc, 1) + y_low 
    X_right = np.concatenate((x_up * Bc, y_right), axis = 1) 
    x_down = length_x * np.random.rand(N_bc, 1) + x_low 
    X_down = np.concatenate((x_down, y_low * Bc), axis = 1)
    x_up =  length_x * np.random.rand(N_bc, 1) + x_low 
    X_up = np.concatenate((x_up, y_up * Bc), axis = 1) 
    X = np.concatenate((X_left, X_right, X_down, X_up), axis = 1) 
    return X  
    
def u_true(x, y, a1 = 1, a2 = 4): 
    return np.sin(a1 * np.pi * x) * np.sin(a2 * np.pi * y)   

def test_data(N): 
    x_test = np.linspace(-1, 1, N) 
    y_test = np.linspace(-1, 1, N)
    XX, YY = np.meshgrid(x_test, y_test) 
    X_test = np.stack((XX,YY), axis = -1).reshape(-1, 2)
    u_test = u_true(X_test[:,0:1], X_test[:,1:2], a1 = 1, a2 = 4)

    return X_test, u_test