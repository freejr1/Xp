#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class FreeFireGameSimulator:
    """
    Simulador avançado do Free Fire com mecânicas realísticas
    """
    
    def __init__(self):
        self.weapons = [
            "AK", "M4A1", "SCAR", "MP40", "UMP", "Vector", 
            "AWM", "Kar98k", "M82B", "SVD", "VSS"
        ]
        
        self.maps = [
            "Bermuda", "Purgatory", "Kalahari", "Alpine", "Nexterra"
        ]
        
        self.game_modes = [
            "Clássico", "Ranked", "Clash Squad", "Battle Royale"
        ]
        
        self.ranks = [
            "Bronze", "Prata", "Ouro", "Platina", "Diamante", "Mestre", "Grão Mestre"
        ]
    
    def generate_match_details(self) -> Dict:
        """Gera detalhes realísticos de uma partida"""
        
        # Seleciona elementos aleatórios
        weapon = random.choice(self.weapons)
        map_name = random.choice(self.maps)
        mode = random.choice(self.game_modes)
        
        # Simula estatísticas da partida
        kills = random.randint(0, 15)
        damage = random.randint(500, 3000)
        survival_time = random.randint(300, 1800)  # 5-30 minutos em segundos
        headshots = random.randint(0, min(kills, 8))
        
        # Determina colocação (1-50 para Battle Royale)
        if mode == "Battle Royale":
            placement = random.randint(1, 50)
            win = placement == 1
        else:
            win = random.choice([True, False, False])  # 33% chance
            placement = 1 if win else random.randint(2, 12)
        
        # Calcula XP baseado na performance
        base_xp = 50
        kill_xp = kills * 10
        damage_xp = damage // 100
        survival_xp = survival_time // 60  # 1 XP por minuto
        placement_xp = max(0, 51 - placement) * 2
        
        total_xp = base_xp + kill_xp + damage_xp + survival_xp + placement_xp
        
        if win:
            total_xp += 100  # Bônus de vitória
        
        return {
            'weapon_used': weapon,
            'map': map_name,
            'mode': mode,
            'kills': kills,
            'headshots': headshots,
            'damage': damage,
            'survival_time': survival_time,
            'placement': placement,
            'win': win,
            'xp_gained': total_xp,
            'timestamp': datetime.now().isoformat()
        }
    
    def calculate_rank_progress(self, current_rank: str, wins: int, losses: int) -> Dict:
        """Calcula progresso do rank"""
        rank_index = self.ranks.index(current_rank) if current_rank in self.ranks else 0
        
        # Simula pontos de rank
        win_points = wins * 15
        loss_points = losses * 8
        net_points = win_points - loss_points
        
        # Determina se subiu de rank
        points_needed = 100
        if net_points >= points_needed and rank_index < len(self.ranks) - 1:
            new_rank = self.ranks[rank_index + 1]
            rank_up = True
        else:
            new_rank = current_rank
            rank_up = False
        
        return {
            'current_rank': new_rank,
            'rank_up': rank_up,
            'points': net_points % points_needed,
            'points_needed': points_needed
        }
    
    def generate_daily_mission(self) -> Dict:
        """Gera missão diária aleatória"""
        missions = [
            {"task": "Eliminar 5 inimigos", "reward": 100, "progress": 0, "target": 5},
            {"task": "Jogar 3 partidas", "reward": 150, "progress": 0, "target": 3},
            {"task": "Causar 2000 de dano", "reward": 200, "progress": 0, "target": 2000},
            {"task": "Sobreviver 20 minutos", "reward": 120, "progress": 0, "target": 1200},
            {"task": "Conseguir 2 headshots", "reward": 80, "progress": 0, "target": 2},
            {"task": "Vencer 1 partida", "reward": 300, "progress": 0, "target": 1}
        ]
        
        return random.choice(missions)
    
    def simulate_loot_box(self) -> Dict:
        """Simula abertura de caixa de recompensas"""
        items = [
            {"name": "Skin de Arma AK", "rarity": "Épico", "value": 500},
            {"name": "Roupa Especial", "rarity": "Lendário", "value": 1000},
            {"name": "Diamantes", "rarity": "Comum", "value": 50},
            {"name": "Moedas", "rarity": "Comum", "value": 100},
            {"name": "Emote Raro", "rarity": "Raro", "value": 200},
            {"name": "Pet Especial", "rarity": "Épico", "value": 800}
        ]
        
        # Probabilidades baseadas na raridade
        rarity_weights = {"Comum": 60, "Raro": 25, "Épico": 12, "Lendário": 3}
        
        available_items = []
        weights = []
        
        for item in items:
            available_items.append(item)
            weights.append(rarity_weights[item["rarity"]])
        
        selected_item = random.choices(available_items, weights=weights)[0]
        
        return {
            'item': selected_item,
            'opened_at': datetime.now().isoformat()
        }
    
    def get_player_stats_summary(self, matches_data: List[Dict]) -> Dict:
        """Gera resumo estatístico do jogador"""
        if not matches_data:
            return {}
        
        total_matches = len(matches_data)
        total_kills = sum(match['kills'] for match in matches_data)
        total_damage = sum(match['damage'] for match in matches_data)
        total_wins = sum(1 for match in matches_data if match['win'])
        total_headshots = sum(match['headshots'] for match in matches_data)
        
        avg_kills = total_kills / total_matches
        avg_damage = total_damage / total_matches
        win_rate = (total_wins / total_matches) * 100
        headshot_rate = (total_headshots / max(total_kills, 1)) * 100
        
        # Arma mais usada
        weapons_used = [match['weapon_used'] for match in matches_data]
        favorite_weapon = max(set(weapons_used), key=weapons_used.count)
        
        # Mapa mais jogado
        maps_played = [match['map'] for match in matches_data]
        favorite_map = max(set(maps_played), key=maps_played.count)
        
        return {
            'total_matches': total_matches,
            'total_kills': total_kills,
            'total_damage': total_damage,
            'total_wins': total_wins,
            'total_headshots': total_headshots,
            'avg_kills': round(avg_kills, 2),
            'avg_damage': round(avg_damage, 0),
            'win_rate': round(win_rate, 1),
            'headshot_rate': round(headshot_rate, 1),
            'favorite_weapon': favorite_weapon,
            'favorite_map': favorite_map,
            'kd_ratio': round(total_kills / max(total_matches - total_wins, 1), 2)
        }

class AdvancedAccountManager:
    """
    Gerenciador avançado de contas com recursos extras
    """
    
    def __init__(self):
        self.simulator = FreeFireGameSimulator()
    
    def create_advanced_account(self, user_id: int, ff_token: str) -> Dict:
        """Cria conta com dados avançados"""
        base_account = {
            'ff_token': ff_token,
            'level': random.randint(1, 10),
            'xp': random.randint(0, 1000),
            'rank': random.choice(self.simulator.ranks[:3]),  # Ranks iniciais
            'diamonds': random.randint(100, 1000),
            'coins': random.randint(5000, 20000),
            'matches_history': [],
            'daily_missions': [],
            'inventory': [],
            'friends_count': random.randint(10, 100),
            'guild': f"Guild_{random.randint(1000, 9999)}",
            'created_at': datetime.now().isoformat(),
            'last_login': datetime.now().isoformat(),
            'total_playtime': 0,  # em minutos
            'achievements': [],
            'settings': {
                'auto_pickup': True,
                'voice_chat': False,
                'graphics_quality': 'Medium'
            }
        }
        
        # Gera missões diárias iniciais
        for _ in range(3):
            mission = self.simulator.generate_daily_mission()
            base_account['daily_missions'].append(mission)
        
        return base_account
    
    def process_advanced_match(self, account: Dict) -> Dict:
        """Processa partida com detalhes avançados"""
        match_details = self.simulator.generate_match_details()
        
        # Atualiza estatísticas da conta
        account['matches_history'].append(match_details)
        account['xp'] += match_details['xp_gained']
        account['total_playtime'] += match_details['survival_time'] // 60
        
        # Verifica level up
        level_up = False
        while account['xp'] >= account['level'] * 1000:
            account['xp'] -= account['level'] * 1000
            account['level'] += 1
            level_up = True
            
            # Recompensas por level up
            account['diamonds'] += 50
            account['coins'] += 1000
        
        # Atualiza progresso das missões diárias
        for mission in account['daily_missions']:
            if mission['task'] == "Eliminar 5 inimigos":
                mission['progress'] += match_details['kills']
            elif mission['task'] == "Jogar 3 partidas":
                mission['progress'] += 1
            elif mission['task'] == "Causar 2000 de dano":
                mission['progress'] += match_details['damage']
            elif mission['task'] == "Sobreviver 20 minutos":
                mission['progress'] += match_details['survival_time']
            elif mission['task'] == "Conseguir 2 headshots":
                mission['progress'] += match_details['headshots']
            elif mission['task'] == "Vencer 1 partida" and match_details['win']:
                mission['progress'] += 1
            
            # Completa missão se atingiu o objetivo
            if mission['progress'] >= mission['target'] and 'completed' not in mission:
                mission['completed'] = True
                account['xp'] += mission['reward']
                account['coins'] += mission['reward'] // 2
        
        # Chance de ganhar item raro
        if random.random() < 0.1:  # 10% chance
            loot = self.simulator.simulate_loot_box()
            account['inventory'].append(loot['item'])
        
        account['last_login'] = datetime.now().isoformat()
        
        return {
            'match_details': match_details,
            'level_up': level_up,
            'missions_completed': len([m for m in account['daily_missions'] if m.get('completed')])
        }

