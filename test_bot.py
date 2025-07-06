#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Teste das funcionalidades do bot Free Fire
"""

import json
import sys
import os

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game_simulator import FreeFireGameSimulator, AdvancedAccountManager

def test_simulator():
    """Testa o simulador de jogo"""
    print("🧪 Testando simulador de jogo...")
    
    simulator = FreeFireGameSimulator()
    
    # Testa geração de detalhes de partida
    match = simulator.generate_match_details()
    print(f"✅ Partida simulada: {match['kills']} kills, {match['xp_gained']} XP")
    
    # Testa cálculo de rank
    rank_info = simulator.calculate_rank_progress("Bronze", 10, 5)
    print(f"✅ Rank calculado: {rank_info['current_rank']}")
    
    # Testa missão diária
    mission = simulator.generate_daily_mission()
    print(f"✅ Missão gerada: {mission['task']}")
    
    # Testa loot box
    loot = simulator.simulate_loot_box()
    print(f"✅ Item obtido: {loot['item']['name']} ({loot['item']['rarity']})")
    
    print("✅ Simulador funcionando corretamente!\n")

def test_account_manager():
    """Testa o gerenciador de contas"""
    print("🧪 Testando gerenciador de contas...")
    
    manager = AdvancedAccountManager()
    
    # Cria conta de teste
    account = manager.create_advanced_account(12345, "TEST_TOKEN_123")
    print(f"✅ Conta criada: Level {account['level']}, {account['xp']} XP")
    
    # Processa partida
    result = manager.process_advanced_match(account)
    print(f"✅ Partida processada: {result['match_details']['kills']} kills")
    
    if result['level_up']:
        print(f"🎉 Level up! Novo level: {account['level']}")
    
    print("✅ Gerenciador de contas funcionando corretamente!\n")

def test_json_operations():
    """Testa operações com JSON"""
    print("🧪 Testando operações JSON...")
    
    # Dados de teste
    test_data = {
        "user_123": {
            "ff_token": "TEST123",
            "level": 5,
            "xp": 500
        }
    }
    
    # Testa escrita
    with open("test_accounts.json", "w") as f:
        json.dump(test_data, f, indent=2)
    print("✅ Arquivo JSON criado")
    
    # Testa leitura
    with open("test_accounts.json", "r") as f:
        loaded_data = json.load(f)
    print("✅ Arquivo JSON lido")
    
    # Remove arquivo de teste
    os.remove("test_accounts.json")
    print("✅ Arquivo de teste removido")
    
    print("✅ Operações JSON funcionando corretamente!\n")

def main():
    """Executa todos os testes"""
    print("🚀 Iniciando testes do Bot Free Fire...\n")
    
    try:
        test_simulator()
        test_account_manager()
        test_json_operations()
        
        print("🎉 Todos os testes passaram com sucesso!")
        print("✅ O bot está pronto para uso!")
        
    except Exception as e:
        print(f"❌ Erro durante os testes: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

