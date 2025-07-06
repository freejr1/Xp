#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configurações do Bot Free Fire
"""

# Token do bot Telegram (fornecido pelo usuário)
BOT_TOKEN = "7862652022:AAG22CFcGrGavgTnMKbWjkq_qAqzVHVKjPo"

# Configurações do jogo
GAME_CONFIG = {
    'min_match_duration': 10,  # segundos (reduzido para demonstração)
    'max_match_duration': 30,  # segundos (reduzido para demonstração)
    'xp_per_match_min': 50,
    'xp_per_match_max': 200,
    'win_bonus_xp': 50,
    'win_probability': 0.33,  # 33% chance de vitória
    'max_kills_per_match': 15,
    'xp_per_level': 1000,
    'max_auto_matches': 50
}

# Configurações de arquivo
FILES_CONFIG = {
    'accounts_file': 'accounts.json',
    'logs_file': 'bot.log'
}

# Mensagens do bot
MESSAGES = {
    'welcome': """
🎮 **Bem-vindo ao Bot Free Fire Automático!** 🎮

Este bot permite automatizar suas partidas no Free Fire para ganhar XP e subir de level rapidamente!

📋 **Comandos disponíveis:**

🔹 `/add <token>` - Adicionar sua conta Free Fire
🔹 `/status` - Verificar progresso da sua conta
🔹 `/play` - Iniciar sessão automática de partidas
🔹 `/stop` - Parar sessão automática
🔹 `/help` - Mostrar esta mensagem

⚡ **Como usar:**
1. Use `/add` seguido do token da sua conta Free Fire
2. Use `/play` para começar a jogar automaticamente
3. Use `/status` para acompanhar seu progresso

🚀 **Recursos:**
- Partidas clássicas automáticas
- Ganho de XP e level up
- Estatísticas detalhadas
- Simulação realística

Digite `/add <seu_token>` para começar!
    """,
    
    'no_account': """
❌ **Nenhuma conta encontrada!**

Use `/add <token>` para adicionar sua conta primeiro.
    """,
    
    'invalid_token': """
❌ **Token inválido!** O token deve ter pelo menos 5 caracteres.
    """,
    
    'session_already_active': """
⚠️ **Sessão já ativa!**

Uma sessão automática já está rodando para sua conta.
Use `/stop` para parar ou `/status` para verificar o progresso.
    """,
    
    'no_active_session': """
❌ **Nenhuma sessão ativa!**

Não há sessão automática rodando para sua conta.
    """
}

