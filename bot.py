#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import json
import random
import time
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token do bot Telegram
BOT_TOKEN = "7862652022:AAG22CFcGrGavgTnMKbWjkq_qAqzVHVKjPo"

# Arquivo para armazenar dados das contas
ACCOUNTS_FILE = "accounts.json"

class FreeFireBotSimulator:
    def __init__(self):
        self.accounts = self.load_accounts()
        self.running_sessions = {}
    
    def load_accounts(self):
        """Carrega contas do arquivo JSON"""
        try:
            with open(ACCOUNTS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_accounts(self):
        """Salva contas no arquivo JSON"""
        with open(ACCOUNTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.accounts, f, indent=2, ensure_ascii=False)
    
    def add_account(self, user_id, ff_token):
        """Adiciona uma nova conta Free Fire"""
        account_data = {
            'ff_token': ff_token,
            'level': random.randint(1, 10),
            'xp': random.randint(0, 1000),
            'matches_played': 0,
            'wins': 0,
            'kills': 0,
            'last_played': None,
            'status': 'offline',
            'created_at': datetime.now().isoformat()
        }
        
        self.accounts[str(user_id)] = account_data
        self.save_accounts()
        return account_data
    
    def get_account(self, user_id):
        """Obtém dados da conta"""
        return self.accounts.get(str(user_id))
    
    def simulate_match(self, user_id):
        """Simula uma partida clássica"""
        account = self.get_account(user_id)
        if not account:
            return None
        
        # Simula resultado da partida
        win = random.choice([True, False, False])  # 33% chance de vitória
        kills = random.randint(0, 15)
        xp_gained = random.randint(50, 200)
        
        # Atualiza estatísticas
        account['matches_played'] += 1
        account['kills'] += kills
        account['xp'] += xp_gained
        
        if win:
            account['wins'] += 1
            xp_gained += 50  # Bônus por vitória
            account['xp'] += 50
        
        # Verifica level up
        level_up = False
        xp_needed = account['level'] * 1000
        if account['xp'] >= xp_needed:
            account['level'] += 1
            account['xp'] = account['xp'] - xp_needed
            level_up = True
        
        account['last_played'] = datetime.now().isoformat()
        account['status'] = 'online'
        
        self.save_accounts()
        
        return {
            'win': win,
            'kills': kills,
            'xp_gained': xp_gained,
            'level_up': level_up,
            'new_level': account['level']
        }
    
    async def auto_play_session(self, user_id, matches_count=10):
        """Executa sessão automática de partidas"""
        if str(user_id) in self.running_sessions:
            return False
        
        self.running_sessions[str(user_id)] = True
        
        try:
            for i in range(matches_count):
                if str(user_id) not in self.running_sessions:
                    break
                
                # Simula tempo de partida (2-5 minutos)
                await asyncio.sleep(random.randint(10, 30))  # Reduzido para demonstração
                
                result = self.simulate_match(user_id)
                if result:
                    logger.info(f"Usuário {user_id} - Partida {i+1}: {'Vitória' if result['win'] else 'Derrota'}")
        
        finally:
            if str(user_id) in self.running_sessions:
                del self.running_sessions[str(user_id)]
            
            # Atualiza status para offline
            account = self.get_account(user_id)
            if account:
                account['status'] = 'offline'
                self.save_accounts()
        
        return True

# Instância global do simulador
simulator = FreeFireBotSimulator()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - Mensagem de boas-vindas"""
    welcome_message = """
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
    """
    
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /add - Adicionar conta Free Fire"""
    user_id = update.effective_user.id
    
    if not context.args:
        await update.message.reply_text(
            "❌ **Erro:** Você precisa fornecer o token da conta!\n\n"
            "**Uso:** `/add <token_da_conta>`\n"
            "**Exemplo:** `/add FF123456789`",
            parse_mode='Markdown'
        )
        return
    
    ff_token = context.args[0]
    
    # Simula validação do token
    if len(ff_token) < 5:
        await update.message.reply_text(
            "❌ **Token inválido!** O token deve ter pelo menos 5 caracteres.",
            parse_mode='Markdown'
        )
        return
    
    # Adiciona a conta
    account = simulator.add_account(user_id, ff_token)
    
    success_message = f"""
✅ **Conta adicionada com sucesso!**

🎮 **Informações da conta:**
🔸 Token: `{ff_token}`
🔸 Level inicial: {account['level']}
🔸 XP inicial: {account['xp']}
🔸 Status: Conectado

🚀 Agora você pode usar `/play` para começar a jogar automaticamente!
    """
    
    await update.message.reply_text(success_message, parse_mode='Markdown')

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /status - Verificar progresso da conta"""
    user_id = update.effective_user.id
    account = simulator.get_account(user_id)
    
    if not account:
        await update.message.reply_text(
            "❌ **Nenhuma conta encontrada!**\n\n"
            "Use `/add <token>` para adicionar sua conta primeiro.",
            parse_mode='Markdown'
        )
        return
    
    # Calcula estatísticas
    win_rate = (account['wins'] / account['matches_played'] * 100) if account['matches_played'] > 0 else 0
    kd_ratio = account['kills'] / max(account['matches_played'], 1)
    xp_needed = account['level'] * 1000 - account['xp']
    
    last_played = "Nunca"
    if account['last_played']:
        last_played_dt = datetime.fromisoformat(account['last_played'])
        last_played = last_played_dt.strftime("%d/%m/%Y %H:%M")
    
    status_message = f"""
📊 **Status da Conta Free Fire**

🎮 **Informações Gerais:**
🔸 Token: `{account['ff_token']}`
🔸 Status: {'🟢 Online' if account['status'] == 'online' else '🔴 Offline'}
🔸 Última partida: {last_played}

📈 **Progressão:**
🔸 Level: {account['level']}
🔸 XP atual: {account['xp']:,}
🔸 XP para próximo level: {xp_needed:,}

🏆 **Estatísticas:**
🔸 Partidas jogadas: {account['matches_played']}
🔸 Vitórias: {account['wins']}
🔸 Taxa de vitória: {win_rate:.1f}%
🔸 Kills totais: {account['kills']}
🔸 K/D médio: {kd_ratio:.2f}

{'🎯 **Sessão ativa!** Bot jogando automaticamente...' if str(user_id) in simulator.running_sessions else '💤 **Conta inativa** - Use /play para começar a jogar'}
    """
    
    await update.message.reply_text(status_message, parse_mode='Markdown')

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /play - Iniciar sessão automática"""
    user_id = update.effective_user.id
    account = simulator.get_account(user_id)
    
    if not account:
        await update.message.reply_text(
            "❌ **Nenhuma conta encontrada!**\n\n"
            "Use `/add <token>` para adicionar sua conta primeiro.",
            parse_mode='Markdown'
        )
        return
    
    if str(user_id) in simulator.running_sessions:
        await update.message.reply_text(
            "⚠️ **Sessão já ativa!**\n\n"
            "Uma sessão automática já está rodando para sua conta.\n"
            "Use `/stop` para parar ou `/status` para verificar o progresso.",
            parse_mode='Markdown'
        )
        return
    
    # Determina número de partidas
    matches_count = 10
    if context.args and context.args[0].isdigit():
        matches_count = min(int(context.args[0]), 50)  # Máximo 50 partidas
    
    await update.message.reply_text(
        f"🚀 **Iniciando sessão automática!**\n\n"
        f"🎮 Jogando {matches_count} partidas clássicas\n"
        f"⚡ Velocidade: Modo turbo ativado\n"
        f"📊 Use `/status` para acompanhar o progresso\n"
        f"🛑 Use `/stop` para parar a qualquer momento",
        parse_mode='Markdown'
    )
    
    # Inicia sessão em background
    asyncio.create_task(simulator.auto_play_session(user_id, matches_count))

async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /stop - Parar sessão automática"""
    user_id = update.effective_user.id
    
    if str(user_id) not in simulator.running_sessions:
        await update.message.reply_text(
            "❌ **Nenhuma sessão ativa!**\n\n"
            "Não há sessão automática rodando para sua conta.",
            parse_mode='Markdown'
        )
        return
    
    del simulator.running_sessions[str(user_id)]
    
    await update.message.reply_text(
        "🛑 **Sessão interrompida!**\n\n"
        "A sessão automática foi parada com sucesso.\n"
        "Use `/status` para ver suas estatísticas finais.",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help - Ajuda"""
    await start_command(update, context)

def main():
    """Função principal do bot"""
    # Cria a aplicação
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Adiciona handlers dos comandos
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("add", add_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("play", play_command))
    application.add_handler(CommandHandler("stop", stop_command))
    application.add_handler(CommandHandler("help", help_command))
    
    # Inicia o bot
    print("🤖 Bot Free Fire iniciado!")
    print("📱 Aguardando comandos...")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

