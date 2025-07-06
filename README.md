# 🎮 Bot Free Fire Automático

Bot do Telegram que simula conexão com contas do Free Fire para automatizar partidas e aumentar level.

## 🚀 Características

- ✅ Conexão automática com contas Free Fire via token
- ✅ Simulação de partidas clássicas em modo turbo
- ✅ Sistema de ganho de XP e level up automático
- ✅ Estatísticas detalhadas de progresso
- ✅ Interface amigável via Telegram
- ✅ Sessões automáticas configuráveis

## 📋 Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `/start` | Mensagem de boas-vindas e instruções |
| `/add <token>` | Adicionar conta Free Fire pelo token |
| `/status` | Verificar progresso e estatísticas da conta |
| `/play [número]` | Iniciar sessão automática (padrão: 10 partidas) |
| `/stop` | Parar sessão automática em andamento |
| `/help` | Mostrar ajuda e comandos |

## 🛠️ Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip3

### Passos de Instalação

1. **Clone ou baixe os arquivos do bot**
```bash
# Se você tem os arquivos, navegue até a pasta
cd freefire_bot
```

2. **Instale as dependências**
```bash
pip3 install -r requirements.txt
```

3. **Execute o bot**
```bash
# Opção 1: Usando o script
./start_bot.sh

# Opção 2: Diretamente
python3 bot.py
```

## 📱 Como Usar

### 1. Iniciar Conversa
- Abra o Telegram
- Procure pelo bot usando o token: `7862652022:AAG22CFcGrGavgTnMKbWjkq_qAqzVHVKjPo`
- Envie `/start` para ver a mensagem de boas-vindas

### 2. Adicionar Conta Free Fire
```
/add FF123456789
```
- Substitua `FF123456789` pelo token da sua conta Free Fire
- O bot confirmará a conexão e mostrará informações iniciais

### 3. Verificar Status
```
/status
```
Mostra:
- Level atual e XP
- Estatísticas de partidas
- Taxa de vitória
- Status da sessão (ativa/inativa)

### 4. Iniciar Automação
```
/play
```
ou
```
/play 20
```
- Inicia sessão automática de partidas
- Padrão: 10 partidas
- Máximo: 50 partidas por sessão

### 5. Parar Automação
```
/stop
```
- Para a sessão automática imediatamente
- Salva o progresso atual

## ⚙️ Configurações

### Arquivo `config.py`
- `BOT_TOKEN`: Token do bot Telegram
- `GAME_CONFIG`: Configurações de simulação do jogo
- `FILES_CONFIG`: Configurações de arquivos
- `MESSAGES`: Mensagens personalizadas do bot

### Personalização
Você pode editar o arquivo `config.py` para:
- Ajustar tempo de partidas
- Modificar ganho de XP
- Alterar probabilidade de vitória
- Personalizar mensagens

## 📊 Sistema de Simulação

### Mecânicas do Jogo
- **Duração das partidas**: 10-30 segundos (modo demonstração)
- **XP por partida**: 50-200 pontos
- **Bônus de vitória**: +50 XP
- **Chance de vitória**: 33%
- **Kills por partida**: 0-15
- **XP para level up**: Level × 1000

### Estatísticas Rastreadas
- Level e XP atual
- Partidas jogadas
- Vitórias e derrotas
- Total de kills
- Taxa de vitória (%)
- K/D médio
- Última partida jogada

## 📁 Estrutura de Arquivos

```
freefire_bot/
├── bot.py              # Arquivo principal do bot
├── config.py           # Configurações
├── requirements.txt    # Dependências Python
├── start_bot.sh       # Script de inicialização
├── README.md          # Esta documentação
└── accounts.json      # Dados das contas (criado automaticamente)
```

## 🔒 Segurança

- Os tokens das contas são armazenados localmente
- Nenhuma informação é enviada para servidores externos
- O bot funciona apenas como simulação
- Dados são salvos em `accounts.json`

## ⚠️ Avisos Importantes

1. **Este é um bot de simulação** - Não se conecta realmente ao Free Fire
2. **Apenas para demonstração** - Simula o comportamento de automação
3. **Tokens fictícios** - Use qualquer string como token para teste
4. **Dados locais** - Todas as informações ficam no seu computador

## 🐛 Solução de Problemas

### Bot não inicia
```bash
# Verifique se as dependências estão instaladas
pip3 install -r requirements.txt

# Execute diretamente
python3 bot.py
```

### Erro de token
- Verifique se o token do bot está correto no arquivo `config.py`
- Certifique-se de que o bot foi criado no @BotFather

### Comandos não funcionam
- Verifique se o bot está rodando
- Reinicie o bot se necessário
- Verifique os logs no terminal

## 📞 Suporte

Se encontrar problemas:
1. Verifique os logs no terminal
2. Confirme que todas as dependências estão instaladas
3. Reinicie o bot
4. Verifique a conexão com a internet

## 🎯 Exemplo de Uso Completo

```
Usuário: /start
Bot: [Mensagem de boas-vindas]

Usuário: /add MINHACONTA123
Bot: ✅ Conta adicionada com sucesso!

Usuário: /status
Bot: [Mostra estatísticas iniciais]

Usuário: /play 15
Bot: 🚀 Iniciando sessão automática! Jogando 15 partidas...

[Bot joga automaticamente]

Usuário: /status
Bot: [Mostra progresso atualizado]

Usuário: /stop
Bot: 🛑 Sessão interrompida!
```

---

**Desenvolvido para demonstração de automação de bots Telegram** 🤖

