# strategies/group2_strategy.py

from card_logic import is_pair, is_valid_play

def strategy(hand, last_play, history, player_id, game_state):
    """
    该策略始终选择手牌中的一对牌进行出牌。
    """
    if not hand:
        return []  # 过牌

    # 寻找对子
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            if hand[i][0] == hand[j][0]:  # 找到一对牌
                # 检查是否能合法出牌
                if last_play and not is_valid_play([hand[i], hand[j]], last_play, hand):
                    continue  # 如果不合法，跳过
                return [hand[i], hand[j]]
    
    return []  # 没有对子，过牌
