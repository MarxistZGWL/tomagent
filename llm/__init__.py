# 当前模型配置比较简单，所以所有的代码放在一起，之后需要将公共配置抽取为 llm_conf，然后每个模型具有一个包
from .llms import Doubao

__all__ = ["Doubao"]