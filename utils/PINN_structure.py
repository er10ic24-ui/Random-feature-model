from collections import OrderedDict 
from torch import nn 
# The deep neural network 
class DNN(nn.Module):
    def __init__(self, layers): 
        super(DNN, self).__init__() 

        # parameters 
        self.depth = len(layers) - 1 

        # set up layer order dict 
        self.activation = nn.Tanh 

        layer_list = list() 
        for i in range(self.depth - 1): 
            layer_list.append(
                ('layer_%d' % i, nn.Linear(layers[i], layers[i+1])) 
            ) 
            layer_list.append(('activation_%d' % i, self.activation()))

        layer_list.append(
            ('layer_%d' % (self.depth - 1), nn.Linear(layers[-2], layers[-1]))
        ) 
        layerDict = OrderedDict(layer_list)
        
        # deploy layers 
        self.layers = nn.Sequential(layerDict) 

    def forward(self, x): 
        out = self.layers(x) 

        return out 

    
        