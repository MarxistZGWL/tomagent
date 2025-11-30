import os
from omegaconf import OmegaConf
from pathlib import Path
import json

current_dir = Path(__file__).resolve().parent
cfg_path = os.path.join(current_dir, "conf.yaml")

cfg = OmegaConf.load(cfg_path)

print(cfg.tools)


# dict
# cfg = OmegaConf.to_container(cfg, resolve=True)

# print(json.dumps(cfg, ensure_ascii=False, indent=2))

