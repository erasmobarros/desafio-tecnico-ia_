# 🎓 EduPrompt - Plataforma Educativa com IA

Este é o repositório do **EduPrompt**, um sistema desenvolvido para o Desafio Técnico de Estágio em IA e Engenharia de Prompt. A plataforma gera materiais educativos altamente personalizados com base no perfil do aluno (idade, nível, estilo de aprendizado) utilizando a API do Google Gemini.

## 🚀 Funcionalidades e Diferenciais Técnicos

Além dos requisitos mínimos do desafio, este projeto implementa funcionalidades voltadas para robustez e desempenho em produção:

* **Motor de Engenharia de Prompt Avançado:** Implementação de testes A/B (v1 básica vs v2 otimizada) utilizando *Persona Prompting*, *Chain-of-Thought* e *Output Formatting*.
* **Sistema de Cache Inteligente:** Utiliza *hashing* MD5 para armazenar respostas da IA localmente, evitando chamadas duplicadas à API e economizando recursos.
* **Resiliência de Conexão (Exponential Backoff):** Tratamento de erros avançado (incluindo tratamento para status 404 e 503), garantindo que picos de uso do servidor do Google não quebrem a aplicação.
* **Interface Web Dinâmica:** Interface gráfica construída em Flask para facilitar a seleção de perfis e visualização do conteúdo.
* **Histórico de Auditoria:** Salvamento automático de todas as gerações no arquivo `outputs/history.json`.

---

## 📁 Estrutura do Projeto

```text
/
├── app.py                      # Aplicação principal (Flask e Integração API)
├── prompt_engine/
│   ├── builder.py              # Lógica de injeção de contexto
│   └── templates.py            # Modelos de prompts (v1 e v2)
├── profiles/
│   └── Estudantes.json         # Perfis de alunos pré-configurados
├── outputs/
│   └── history.json            # Histórico geral de requisições
├── cache/                      # Armazenamento em cache via MD5
├── samples/                    # Exemplos de outputs gerados para o desafio
├── templates/
│   └── index.html              # Interface web
├── .env.example                # Exemplo de variáveis de ambiente
├── requirements.txt            # Dependências do Python
├── PROMPT_ENGINEERING_NOTES.md # Justificativas técnicas de IA
└── README.md                   # Esta documentação
```
## ⚙️ Instruções de Setup e Execução
Para rodar este projeto localmente, siga os passos abaixo:

1. Pré-requisitos
Python 3.10 ou superior instalado.

Uma chave de API válida do Google AI Studio.

2. Clonar o Repositório e Preparar o Ambiente
Abra o seu terminal e execute:

Bash
# Clone o repositório (substitua pela sua URL caso faça o git clone)
# git clone <url-do-seu-repositorio>
# cd <nome-da-pasta>

# Crie um ambiente virtual para isolar as dependências
python -m venv venv

# Ative o ambiente virtual (Windows)
venv\Scripts\activate
# Para Linux/Mac use: source venv/bin/activate
3. Instalar Dependências
Com o ambiente ativado, instale as bibliotecas necessárias:

Bash
pip install -r requirements.txt
4. Configurar Variáveis de Ambiente
Renomeie o arquivo .env.example para .env (ou crie um novo arquivo .env).

Adicione a sua chave de API do Gemini no arquivo:

Plaintext
GEMINI_API_KEY=sua_chave_secreta_aqui
5. Executar a Aplicação
Inicie o servidor Flask executando:

Bash
python app.py
Acesse http://127.0.0.1:5000 no seu navegador para utilizar a plataforma.
```
## 🧠 Engenharia de Prompt
Para uma análise detalhada das estratégias de estruturação de prompts, Chain-of-Thought e Context Setting utilizadas neste projeto, consulte o arquivo PROMPT_ENGINEERING_NOTES.md.

## 👨‍💻 Autoria
Desenvolvido por Erasmo.