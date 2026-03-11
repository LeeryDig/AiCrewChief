# Arquitetura do Sistema

O AI Crew Chief foi projetado como um pipeline modular para simular o funcionamento de um engenheiro de corrida.

---

# Pipeline principal

O fluxo do sistema é:

Piloto fala  
↓  
Gravação de áudio  
↓  
Speech-to-text  
↓  
Classificação do problema  
↓  
Busca na base de conhecimento  
↓  
Escolha da correção  
↓  
Resposta por voz  

---

# Camada de voz

Diretório:

voice/

Responsabilidades:

- gravar áudio do microfone
- converter voz em texto
- falar a resposta do engenheiro

Arquivos principais:

- recorder.py
- stt.py
- tts.py

---

# Camada de IA

Diretório:

engine/

Responsabilidades:

- interpretar o problema descrito pelo piloto
- classificar tipo de problema
- selecionar a correção mais adequada

Modelos utilizados:

LLMs locais rodando via Ollama.

---

# Base de conhecimento

Diretório:

knowledge/

Contém regras de engenharia de corrida estruturadas em JSON.

Exemplo de organização:

- oversteer
- understeer
- entry
- mid
- exit

Cada fase possui possíveis correções de setup.

---

# Camada de decisão

O sistema combina:

- interpretação da frase do piloto
- conhecimento da base de setup

para escolher a melhor recomendação.

---

# Telemetria (planejado)

Diretório:

telemetry/

Futuramente essa camada será responsável por:

- leitura de telemetria do simulador
- análise de pneus
- consumo de combustível
- estratégia de corrida