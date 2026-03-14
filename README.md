# AI Crew Chief

AI Crew Chief é um engenheiro de corrida com IA rodando localmente para simuladores de corrida.

A ideia do projeto é permitir que o piloto converse com um engenheiro durante a sessão e receba sugestões de setup do carro de forma parecida com uma comunicação de rádio real.

O sistema escuta o piloto, interpreta o problema de comportamento do carro e sugere mudanças de setup baseadas em uma base de conhecimento.

---

# Funcionalidades atuais

- Push-to-talk (rádio)
- Reconhecimento de voz usando Whisper
- Classificação de problemas de handling usando IA
- Base de conhecimento de setup
- Respostas por voz (TTS)
- Execução totalmente local

Exemplo de uso:

Piloto fala:

Car is understeering on entry

Engenheiro responde:

Soften front anti-roll bar by 1 click.  
Increase front toe-out slightly.

---

# Estrutura do projeto

AiCrewChief
│
├── main.py
│
├── ai
│   └── engineer.py
│
├── engine
│   ├── problem_classifier.py
│   ├── knowledge_loader.py
│   └── fix_selector.py
│
├── knowledge
│   ├── oversteer.json
│   ├── understeer.json
│
├── voice
│   ├── recorder.py
│   ├── stt.py
│   └── tts.py
│
└── telemetry
    ├── ams2_reader.py
    └── telemetry_snapshot.py

---

# Requisitos

Python 3.10+

Instalar dependências:

pip install -r requirements.txt

Principais bibliotecas usadas:

- whisper
- ollama
- keyboard
- sounddevice
- scipy
- pyttsx3

Também é necessário instalar:

- Ollama
- FFmpeg

---

# Instalar Ollama

Baixe em:

https://ollama.com

Depois rode um modelo:

ollama run phi3

Modelos recomendados:

- phi3
- mistral

---

# Instalar FFmpeg

Whisper depende de FFmpeg.

Baixar em:

https://www.gyan.dev/ffmpeg/builds/

Depois adicionar a pasta bin ao PATH.

Testar com:

ffmpeg -version

---

# Executando o projeto

Rodar o projeto (o Ollama é iniciado automaticamente se necessário):

python main.py

Pressione **V** para falar com o engenheiro.

---

# Como funciona

1. O piloto pressiona a tecla de rádio
2. O sistema grava o áudio
3. O áudio é transcrito
4. A IA interpreta o problema
5. A base de conhecimento é consultada
6. Um ajuste de setup é escolhido
7. O engenheiro responde por voz

---

# Roadmap

Funcionalidades planejadas:

- interpretação melhor de linguagem natural
- estratégia de corrida
- análise de telemetria
- integração com Automobilista 2
- histórico de mudanças de setup
- memória de sessão
- filtro de rádio para voz
