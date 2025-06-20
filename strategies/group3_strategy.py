# strategies/group3_strategy.py

from card_logic import is_valid_play

def strategy(hand, last_play, history, player_id, game_state):
    """
    该策略选择手牌中的最小单牌进行出牌。
    """
    if not hand:
        return []  # 过牌
    
    # 按照牌的点数从小到大排序
    hand_sorted = sorted(hand, key=lambda card: card[0])

    # 出最小的单牌
    play = hand_sorted[0]
    
    # 检查是否能合法出牌
    if last_play and not is_valid_play([play], last_play, hand):
        return []  # 如果不合法，则过牌
    return [play]
