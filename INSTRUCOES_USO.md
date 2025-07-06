# 🎮 INSTRUÇÕES DE USO - Bot Free Fire Telegram

## ⚡ INÍCIO RÁPIDO

### 1. Executar o Bot
```bash
cd freefire_bot
python3 bot.py
```

### 2. No Telegram
- Procure pelo bot usando o token: `7862652022:AAG22CFcGrGavgTnMKbWjkq_qAqzVHVKjPo`
- Envie: `/start`

### 3. Adicionar Conta
```
/add MEUTOKEN123
```

### 4. Começar a Jogar
```
/play
```

### 5. Verificar Progresso
```
/status
```

---

## 📋 COMANDOS COMPLETOS

| Comando | Exemplo | Descrição |
|---------|---------|-----------|
| `/start` | `/start` | Mensagem de boas-vindas |
| `/add` | `/add FF123456` | Adiciona conta Free Fire |
| `/status` | `/status` | Mostra estatísticas |
| `/play` | `/play 15` | Joga 15 partidas (padrão: 10) |
| `/stop` | `/stop` | Para automação |
| `/help` | `/help` | Mostra ajuda |

---

## 🎯 EXEMPLO DE USO COMPLETO

```
👤 Usuário: /start
🤖 Bot: [Mensagem de boas-vindas com instruções]

👤 Usuário: /add MINHACONTA123
🤖 Bot: ✅ Conta adicionada com sucesso!
      🎮 Level inicial: 5, XP: 750

👤 Usuário: /status
🤖 Bot: 📊 Status da Conta Free Fire
      🔸 Level: 5
      🔸 XP atual: 750
      🔸 Partidas: 0
      💤 Conta inativa

👤 Usuário: /play 20
🤖 Bot: 🚀 Iniciando sessão automática!
      🎮 Jogando 20 partidas clássicas
      ⚡ Velocidade: Modo turbo ativado

[Bot joga automaticamente por alguns minutos]

👤 Usuário: /status
🤖 Bot: 📊 Status da Conta Free Fire
      🔸 Level: 7 (subiu 2 levels!)
      🔸 XP atual: 1,250
      🔸 Partidas: 20
      🔸 Vitórias: 7
      🔸 Taxa de vitória: 35.0%
      🔸 Kills totais: 89
      🎯 Sessão ativa! Bot jogando...

👤 Usuário: /stop
🤖 Bot: 🛑 Sessão interrompida!
      Use /status para ver estatísticas finais.
```

---

## ⚙️ CONFIGURAÇÕES AVANÇADAS

### Editar Velocidade das Partidas
No arquivo `config.py`:
```python
GAME_CONFIG = {
    'min_match_duration': 10,  # segundos
    'max_match_duration': 30,  # segundos
    # ...
}
```

### Alterar Ganho de XP
```python
GAME_CONFIG = {
    'xp_per_match_min': 50,
    'xp_per_match_max': 200,
    'win_bonus_xp': 50,
    # ...
}
```

### Modificar Chance de Vitória
```python
GAME_CONFIG = {
    'win_probability': 0.33,  # 33% chance
    # ...
}
```

---

## 🔧 SOLUÇÃO DE PROBLEMAS

### ❌ Bot não inicia
```bash
# Instalar dependências
pip3 install -r requirements.txt

# Executar diretamente
python3 bot.py
```

### ❌ Erro "Token inválido"
- Verifique se o token do bot está correto
- Confirme que o bot foi criado no @BotFather

### ❌ Comandos não respondem
- Verifique se o bot está rodando no terminal
- Reinicie o bot se necessário

### ❌ Erro de permissão
```bash
chmod +x start_bot.sh
./start_bot.sh
```

---

## 📊 RECURSOS DO SISTEMA

### 🎮 Simulação Realística
- Partidas com duração variável
- Sistema de kills e headshots
- Diferentes armas e mapas
- Cálculo de dano e sobrevivência

### 📈 Progressão Avançada
- Sistema de XP e level up
- Ranks competitivos
- Missões diárias
- Recompensas por conquistas

### 💎 Sistema de Recompensas
- Diamantes e moedas
- Itens raros e épicos
- Skins de armas
- Pets especiais

### 📊 Estatísticas Detalhadas
- Taxa de vitória
- K/D ratio
- Arma favorita
- Mapa mais jogado
- Tempo total de jogo

---

## ⚠️ AVISOS IMPORTANTES

1. **🔒 SEGURANÇA**: Este é um bot de simulação, não se conecta ao Free Fire real
2. **💾 DADOS**: Todas as informações ficam armazenadas localmente
3. **🎯 PROPÓSITO**: Criado para demonstração de automação de bots
4. **🔧 PERSONALIZAÇÃO**: Código totalmente editável e customizável

---

## 📞 SUPORTE TÉCNICO

### Logs do Sistema
```bash
# Ver logs em tempo real
tail -f bot.log

# Ver últimas 50 linhas
tail -50 bot.log
```

### Backup de Dados
```bash
# Fazer backup das contas
cp accounts.json accounts_backup.json

# Restaurar backup
cp accounts_backup.json accounts.json
```

### Reset Completo
```bash
# Apagar todos os dados
rm accounts.json
rm bot.log

# Reiniciar bot
python3 bot.py
```

---

**🎮 Divirta-se com seu Bot Free Fire Automático! 🚀**

