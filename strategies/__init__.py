# -*- coding: utf-8 -*-
"""
strategies 包

本包用于管理各组的斗地主出牌策略模块。  
每个子模块（如 template_strategy、group1_strategy 等）都必须定义：
    
    def strategy(
        hand: List[Tuple[str, Suit]],
        last_play: Tuple[List[Tuple[str, Suit]], int] or None,
        history: List[Dict],
        player_id: int,
        game_state: Dict
    ) -> List[Tuple[str, Suit]]:
        ...
    
并返回本轮要出的牌列表（空列表表示“过”）。

你可以在这里扩展如动态加载、注册等功能，也可保持空包结构。
"""

__all__ = [
    "template_strategy",
    "group1_strategy",
    "group2_strategy",
    "group3_strategy",
]
