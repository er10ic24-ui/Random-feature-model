import torch 
from torch import nn

class RFN_coefficients(nn.Module): 
    def __init__(self, D_x, D_t, scale_x = 1.0,  scale_t = 1.0):
        super().__init__() 
        # set up parameters for random features 
        # Sample omega and b, store as buffers 
        # Spacial random features
        
        self.register_buffer("W_x", torch.randn(1, D_x) * scale_x)
        self.register_buffer("b_x", 2 * torch.pi * torch.rand(D_x))
        # Temporal random features      
        self.register_buffer("W_t", torch.randn(1, D_t) * scale_t)
        self.register_buffer("b_t", 2 * torch.pi * torch.rand(D_t))
        
    def forward(self, x, t):
        proj_x = torch.mm(x, self.W_x) # (N, 1) x (1, D_x) matrix multiplication = (N, D_x)  
        M_x = (proj_x + self.b_x) # (N, D_x)
        proj_t = torch.mm(t, self.W_t) # (N, 1) x (1, D_t) matrix multiplication = (N, D_t) 
        M_t = (proj_t + self.b_t) # (N, D_t) 
        Phi_x = torch.cos(M_x) # (N, D_x) 
        Phi_t = torch.cos(M_t) # (N, D_t) 
        
        return Phi_x, Phi_t  # The coefficient matrices inside the cosine function 

class Random_Feature_model(nn.Module): 
    def __init__(self, Dx, Dt, scale_x = 1.0, scale_t = 1.0, out_dim = 1): 
        super().__init__() 
        self.rff = RFN_coefficients(Dx, Dt, scale_x, scale_t) 
        
        # learn linear coefficients \alpha: map D to out_dim = 1; one hidden layer 
        self.linear = nn.Linear(Dx * Dt, out_dim, bias = False)
        
        # Optionally initialize linear weights small 
        # nn.init.normal_(self.linear.weight, mean = 0.0, std = 1e-3) 
        # nn.init.zeros_(self.linear.weight) 
        # nn.init.zeros_(self.linear.bias) 
        
    def forward(self, x, t): 
        # x must be a float tensor on the smae device as model 
        phi_x, phi_t = self.rff(x, t) # (N, Dx), (N, Dt)  
        result_einsum = torch.einsum(
            'bi,bj->bij',
            phi_x,
            phi_t
            ).reshape(phi_x.shape[0], -1)
        
        return self.linear(result_einsum) 
