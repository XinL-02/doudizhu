# strategies/group1_strategy.py

import random
from card_logic import is_valid_play

def strategy(hand, last_play, history, player_id, game_state):
    """
    该策略随机从手牌中选择一张牌进行出牌。
    """
    if not hand:
        return []  # 过牌

    # 随机选择一张牌
    play = random.choice(hand)
    
    # 检查是否能合法出牌
    if last_play and not is_valid_play([play], last_play, hand):
        return []  # 如果不合法，则过牌
    return [play]
