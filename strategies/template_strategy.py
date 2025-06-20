# strategies/template_strategy.py

from typing import List, Tuple, Dict, Union
from card_logic import Suit

def strategy(
    hand: List[Tuple[str, Suit]],
    last_play: Union[Tuple[List[Tuple[str, Suit]], int], None],  # 修改此行
    history: List[Dict],
    player_id: int,
    game_state: Dict
) -> List[Tuple[str, Suit]]:
    """
    策略函数接口 —— 切勿改动签名！

    参数：
      hand         当前玩家手牌列表，形如 [('3', Suit.SPADE), ...]
      last_play    上一次有效出牌 ((牌列表), 出牌者ID)，
                   若新一轮开始则为 None
      history      已出牌历史，列表元素为 {'player_id': int, 'play': List[Tuple]}
      player_id    本玩家 ID（0/1/2）
      game_state   额外状态，如 {'remaining_counts': {0:17,1:17,2:17}}

    返回：
      本轮出牌列表，空列表表示“过”。
      必须返回合法出牌，否则引擎将抛出异常。
    """
    # 示例：始终过
    return []
