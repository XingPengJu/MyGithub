import torch
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# DEVICE = torch.device('cpu')
DEFAULT_CONFIG = {
    'save_path': './saves'
}