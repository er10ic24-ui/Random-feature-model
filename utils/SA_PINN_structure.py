from torch import nn 
from collections import OrderedDict # To place the hidden layers orderly 

class AdaptiveLoss(nn.Module): 
    def __init__(self, layers, N_r, N_b, N_0): 
        super(AdaptiveLoss, self).__init__()

        # Layers 
        self.depth = len(layers) - 1 # total layers, including the input and out put layers 

        # Self Adaptive parameters 
        # The parameters will be included in adaptive_loss.parameters() 
        self.lambda_r = nn.Parameter(torch.rand(N_r, 1), requires_grad = True) 
        self.lambda_b = nn.Parameter(torch.rand(N_b, 1), requires_grad = True) 
        self.lambda_0 = nn.Parameter(torch.rand(N_0, 1), requires_grad = True) 
        

        # Set up layer order dict 
        self.activation = nn.Tanh() 

        layer_list = list() 
        for i in range(self.depth - 1):
            layer_list.append(
                ('layer_%d' % i, nn.Linear(layers[i], layers[i+1])) 
            ) 
            layer_list.append(('activation_%d' % i, self.activation)) 

        layer_list.append( 
            ('layer_%d' % (self.depth - 1), nn.Linear(layers[-2], layers[-1])) 
        ) 
        layerDict = OrderedDict(layer_list) 

        # deploy layers 
        self.layers = nn.Sequential(layerDict) 

    def forward(self, x): 
        out = self.layers(x) 
        return out 