# Vox - Discord Audio Transcription Bot

Vox é um bot do Discord que transcreve automaticamente arquivos de áudio usando AssemblyAI e fornece análise inteligente com LLM.

## Funcionalidades

### Phase 2 - Implementadas

- ✅ **Story 1.1**: Transcrição automática de áudio com AssemblyAI
  - **Idioma**: Português (PT) otimizado
  - **Identificação de Speakers**: Separa automaticamente diferentes pessoas na conversa
  - **Formatos suportados**: `.mp3`, `.wav`, `.m4a`, `.ogg`
  - **Processamento assíncrono**: Não bloqueia o bot durante transcrição
  - **Limpeza automática**: Remove arquivos após processamento
  - **Divisão inteligente**: Mensagens longas divididas automaticamente
  - **Metadados**: Duração, número de speakers, confiança da transcrição

### Em Desenvolvimento

- 🚧 **Story 1.2**: Processamento com Gemini LLM (análise personalizada com prompts do usuário)
- 🚧 **Story 1.3**: Pipeline assíncrono com concorrência limitada
- 🚧 **Story 1.4**: Camada mock de banco de dados
- 🚧 **Story 1.5**: Error handling avançado e logging

## Instalação

### Pré-requisitos

- Python 3.8+
- Conta no Discord Developer Portal
- Conta no AssemblyAI (gratuita)

### 1. Clonar o Repositório

```bash
git clone <repo-url>
cd Vox
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione suas credenciais:

```env
DISCORD_TOKEN=seu_token_do_discord
ASSEMBLYAI_API_KEY=sua_chave_da_assemblyai
```

#### Como Obter as Credenciais

**Discord Bot Token:**
1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Crie uma nova aplicação ou selecione uma existente
3. Vá para "Bot" no menu lateral
4. Clique em "Reset Token" para gerar um novo token
5. Copie o token para o `.env`

**Bot Permissions necessárias:**
- Read Messages/View Channels
- Send Messages
- Attach Files
- Read Message History

**AssemblyAI API Key:**
1. Acesse [AssemblyAI](https://www.assemblyai.com/)
2. Crie uma conta gratuita
3. Vá para o dashboard
4. Copie sua API key
5. Cole no `.env`

### 4. Executar o Bot

```bash
python bot.py
```

## Uso

### Comandos

#### `!ping`
Testa se o bot está online e responsivo.

```
Usuário: !ping
Vox: 🏓 Pong!
```

#### Transcrição de Áudio com Identificação de Speakers

Envie um arquivo de áudio (`.mp3`, `.wav`, `.m4a`, ou `.ogg`) em qualquer canal onde o bot tenha acesso.

```
Usuário: [Anexa reuniao.mp3]
Vox: 🎙️ Recebi o arquivo `reuniao.mp3`, transcrevendo...

[Processamento assíncrono...]

Vox: 📝 Transcrição Completa (15:32) - 3 pessoas identificadas - Confiança: 91.2%
```
**[A]**
Iniciei a gravação também, ainda vou tacar mais um loom...

**[B]**
O Fathom tá falando que tá entrando na call aqui.

**[A]**
Trabalha mesmo.

**[C]**
Depois entra no Slack, mano...
```
```

**Nota**:
- O processamento é assíncrono. O bot continua respondendo a outros comandos enquanto transcreve.
- Speakers são identificados automaticamente como A, B, C, etc.
- O bot mostra duração do áudio, número de pessoas e confiança da transcrição.

## Estrutura do Projeto

```
Vox/
├── bot.py                      # Bot principal do Discord
├── services/                   # Camada de serviços
│   ├── __init__.py
│   └── assemblyai_service.py  # Integração com AssemblyAI
├── requirements.txt            # Dependências Python
├── .env                        # Configurações (não commitado)
├── .env.example                # Template de configuração
├── README.md                   # Este arquivo
├── audios/                     # Armazenamento temporário de áudio (criado automaticamente)
└── docs/                       # Documentação do projeto
    ├── prd/                    # Product Requirements Document
    └── architecture/           # Arquitetura técnica
```

## Desenvolvimento

### Padrões de Código

- **Style**: PEP 8
- **Type Hints**: Obrigatórios para todas as funções
- **Docstrings**: Google-style para funções públicas
- **Async**: Todas operações I/O devem usar `async`/`await`

### Logging

O bot usa o módulo `logging` do Python. Níveis de log:

- `INFO`: Operações normais (startup, transcrições iniciadas/concluídas)
- `WARNING`: Serviço não disponível (API keys não configuradas)
- `ERROR`: Erros na transcrição ou processamento

### Integração com Discord

O bot usa `discord.py` 2.6.4 com async/await pattern. O processamento de áudio é feito em background tasks para não bloquear o event loop do Discord.

## Troubleshooting

### Bot não inicia

**Erro**: `DISCORD_TOKEN not found in environment variables!`
- **Solução**: Configure `DISCORD_TOKEN` no arquivo `.env`

### Transcrição falha

**Erro**: `Serviço de transcrição não está configurado`
- **Solução**: Configure `ASSEMBLYAI_API_KEY` no arquivo `.env`

**Erro**: `Transcription failed: [erro]`
- **Possíveis causas**:
  - Arquivo de áudio corrompido
  - Formato não suportado (use .mp3, .wav, .m4a, .ogg)
  - Limite de taxa da API AssemblyAI excedido
  - Conexão de rede instável

### Bot não responde a áudios

1. Verifique se o bot tem permissões corretas no servidor Discord
2. Confirme que o formato do arquivo é suportado
3. Verifique os logs do bot para erros

## Referências

- [Documentação do Discord.py](https://discordpy.readthedocs.io/)
- [Documentação da AssemblyAI](https://www.assemblyai.com/docs)
- [PRD completo](docs/prd/vox-phase2-prd.md)
- [Arquitetura](docs/architecture/vox-phase2-architecture.md)

## Licença

[Adicionar licença aqui]

## Contribuindo

[Adicionar guidelines de contribuição]

---

**Status**: Phase 2 Story 1.1 ✅ Implementada
**Próximo**: Story 1.2 - Gemini LLM Processing Integration
