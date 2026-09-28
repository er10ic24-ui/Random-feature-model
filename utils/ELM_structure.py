import torch
from torch import nn 
import math 
class ELM_coefficients(nn.Module): 
    # def __init__(self, in_dim, D, sigma): 
    def __init__(self, in_dim, D): 
        super().__init__() 
        # set up parameters for random features
        self.register_buffer("W", torch.randn(in_dim, D) / math.sqrt(2))
        self.register_buffer("b", 2 * torch.rand(D) - 1)        

    def forward(self, x): 
        proj = torch.mm(x, self.W) # (N, 2) x (2, D) matrix multiplication = (N, D)  
        Z = torch.tanh(proj + self.b) 
        return Z # (N, D) 


class ELM(nn.Module): 
    def __init__(self, in_dim, D, out_dim = 1): 
        super().__init__()
        self.elm_coeff = ELM_coefficients(in_dim, D) 
        self.linear = nn.Linear(D, out_dim, bias = False) 

    def forward(self, x): 
        phi = self.elm_coeff(x) 
        return self.linear(phi) # (N,1) 