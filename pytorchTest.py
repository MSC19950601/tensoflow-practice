# CUDA TEST
import torch
cudnn.enabled = False
x = torch.Tensor([1.0])
xx = x.cuda()
print(xx)

# CUDNN TEST
from torch.backends import cudnn
print(cudnn.is_accectable(xx))