# Estratégias de Engenharia de Prompt - EduPrompt

Este documento detalha as técnicas avançadas de Engenharia de Prompt utilizadas no desenvolvimento da plataforma, justificando as escolhas arquiteturais e demonstrando a evolução da qualidade do conteúdo gerado.

## 1. Abordagem de Teste A/B (Versão 1 vs. Versão 2)
Para demonstrar o impacto de um prompt bem estruturado, a aplicação foi projetada para suportar múltiplas versões de prompts (`v1` e `v2`).
* **Versão 1 (Baseline):** Utiliza prompts diretos e genéricos (Zero-shot padrão). Ex: *"Você é um professor. Explique o tópico X para o aluno Y."* O resultado costuma ser prolixo, pouco adaptado à idade e com formatação imprevisível.
* **Versão 2 (Otimizada):** Aplica uma combinação de técnicas avançadas para domar a LLM, forçando saídas altamente personalizadas e estruturadas.

## 2. Técnicas Avançadas Aplicadas (Versão 2)

### A. Context Setting (Injeção de Contexto Dinâmico)
Em todos os templates da `v2`, injetamos variáveis rigorosas sobre o perfil do usuário antes da instrução principal.
* **Implementação:** O sistema lê os dados do `Estudantes.json` (Nome, Idade, Nível e Estilo de Aprendizado) e os coloca no topo do prompt.
* **Por que funciona:** LLMs operam prevendo o próximo token com base no contexto anterior. Ao estabelecer regras como "Aluno de 14 anos com estilo visual" logo no início, o modelo recalibra seu vocabulário e exemplos para se adequar a essa realidade dimensional, evitando jargões acadêmicos desnecessários para iniciantes.

### B. Persona Prompting Avançado
Não basta dizer "aja como professor". A `v2` atribui personas altamente específicas para cada tipo de conteúdo.
* **Explicador:** *"Você é um professor especialista em pedagogia construtivista com 15 anos de experiência."*
* **Reflexão:** *"Atue como um facilitador socrático experiente, focado em desenvolver o pensamento crítico profundo."*
* **Por que funciona:** Personas específicas ativam *clusters* semânticos mais refinados no modelo, alterando o tom de voz e a profundidade da resposta.

### C. Chain-of-Thought (CoT) Restrito
Na geração de explicações conceituais, foi implementada uma variação da técnica de "Pensar Passo a Passo".
* **Implementação:** O prompt exige que a IA preencha um campo `[Raciocínio]:` antes de gerar a explicação final.
* **Por que funciona:** Forçar o modelo a verbalizar seu planejamento (*"Escreva aqui brevemente seu processo de pensamento sobre como ensinar isso"*) aumenta drasticamente a coerência e a lógica da resposta final, reduzindo alucinações.

### D. Output Formatting & Constraints (Restrições de Saída)
LLMs tendem a ser conversacionais ("Aqui está o seu exemplo..."). Para integrar a IA a um sistema de software, a saída precisa ser previsível.
* **Implementação:** Uso de seções como `FORMATO DE SAÍDA OBRIGATÓRIO:` e `RESTRIÇÕES RIGOROSAS:`.
* **Exemplo Extremo (Resumo Visual):** O prompt de mapa mental proíbe expressamente o uso de texto fora de um bloco de código ASCII, forçando a IA a atuar puramente como um gerador de diagramas lógicos, sem "falar" com o usuário.

## 3. Conclusão
A arquitetura modular de templates (`templates.py`) aliada ao motor de montagem (`builder.py`) permite que novas técnicas de prompt sejam implementadas e testadas isoladamente sem alterar a lógica de negócios da aplicação web.