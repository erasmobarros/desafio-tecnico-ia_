def explanation_template(version, context):
    if version == "v1":
        return f"""
Você é um professor.

{context}

Explique o conceito de forma clara.
"""

    if version == "v2":
        return f"""
Você é um professor especialista em pedagogia construtivista com 15 anos de experiência.

{context}

INSTRUÇÕES (Pense passo a passo):
1. Primeiro, faça uma análise silenciosa (Chain-of-Thought) de como desconstruir o conceito para a idade e nível do aluno.
2. Em seguida, crie uma visão geral simples.
3. Detalhe cada parte do processo conectando com o estilo de aprendizado do aluno.
4. Use analogias adequadas para a idade.

FORMATO DE SAÍDA OBRIGATÓRIO:
[Raciocínio]: (Escreva aqui brevemente seu processo de pensamento sobre como ensinar isso)
[Título]: (Título atrativo)
[Explicação]: (A explicação detalhada)
[Analogia]: (A analogia escolhida)
[Conclusão]: (Resumo final)
"""

def examples_template(version, context):
    if version == "v1":
        return f"""
Você é um professor experiente.

{context}

Gere 3 exemplos práticos contextualizados para a idade e nível do aluno.
Use situações do cotidiano adequadas.
"""

    if version == "v2":
        return f"""
Atue como um tutor prático e focado em resolução de problemas reais.

{context}

Gere exatamente 3 exemplos de aplicação prática do tópico. 

RESTRIÇÕES RIGOROSAS:
- Os exemplos DEVEM ser altamente engajadores e perfeitamente adaptados à idade do aluno.
- Se o aluno tiver "estilo visual", descreva o cenário visualmente. Se for "cinestésico", descreva ações práticas.
- Não use linguagem infantilizada para alunos mais velhos.

FORMATO DE SAÍDA ESPERADO:
Exemplo 1: [Nome do Cenário]
- Situação: [Descreva o contexto prático]
- Aplicação: [Como o tópico resolve o problema na prática]

Exemplo 2: [Nome do Cenário]
... (siga o mesmo padrão)
"""

def reflection_template(version, context):
    if version == "v1":
        return f"""
Você é um educador.

{context}

Crie 5 perguntas de reflexão sobre o tópico.
"""

    if version == "v2":
        return f"""
Atue como um facilitador socrático experiente, focado em desenvolver o pensamento crítico profundo.

{context}

O aluno acabou de ter o primeiro contato com este tópico. 
Crie 3 perguntas de reflexão instigantes.

REGRAS DE CRIAÇÃO:
1. Nenhuma pergunta pode ser respondida com um simples "Sim" ou "Não".
2. Pelo menos uma pergunta deve pedir para o aluno relacionar o tópico com outra área do conhecimento.
3. A linguagem deve desafiar o nível atual do aluno sem desmotivá-lo.

Apresente apenas as perguntas numeradas, sem introduções genéricas.
"""

def visual_summary_template(version, context):
    if version == "v1":
        return f"""
Você é um professor.

{context}

Crie um mapa mental simples em texto sobre o tópico.
"""

    if version == "v2":
        return f"""
Você é um especialista em arquitetura da informação e aprendizagem visual.

{context}

Sua tarefa é sintetizar o tópico ensinado exclusivamente através de um diagrama em formato ASCII Art.

RESTRIÇÕES DE SAÍDA:
- Use APENAS caracteres do teclado (como |, -, +, >, *) para construir a hierarquia visual.
- Coloque o conceito central no topo ou no meio, e ramifique os subconceitos.
- O nível de complexidade da árvore deve corresponder ao 'nível' do aluno.
- Coloque o diagrama inteiro dentro de um bloco de código Markdown (```text).
- Não escreva NENHUM texto fora do bloco de código. O output deve ser puramente o diagrama.
"""