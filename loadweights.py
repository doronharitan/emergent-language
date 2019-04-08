import torch
import configs
from modules.agent import AgentModule
from train import parser

args = vars(parser.parse_args())
agent_config = configs.get_agent_config(args)
agent = AgentModule(agent_config)

agent.load_state_dict(torch.load(r'C:\Users\user\Desktop\emergent-language\2114-07042019\modules_weights.pt'))
agent.eval()

for param_tensor in agent.state_dict():
    print(param_tensor, "\t", agent.state_dict()[param_tensor].size())
