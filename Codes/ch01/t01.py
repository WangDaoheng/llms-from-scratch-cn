import torch
import numpy as np
import sys

print(sys.version)

data = [[1, 2], [3, 4]]
np_array = np.array(data)

x_data = torch.from_numpy(np_array)

print(x_data)
