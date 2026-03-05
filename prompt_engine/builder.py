from prompt_engine.templates import (
    explanation_template,
    examples_template,
    reflection_template,
    visual_summary_template
)

def build_prompt(version, content_type, student, topic):
    
    context = f"""
Aluno:
Nome: {student['nome']}
Idade: {student['idade']}
Nível: {student['nivel']}
Estilo: {student['estilo_aprendizado']} 

Tópico: {topic}
"""

   
    if content_type == "explicacao":
        return explanation_template(version, context)

    if content_type == "exemplos":
        return examples_template(version, context)

    if content_type == "reflexao":
        return reflection_template(version, context)

    if content_type == "resumo_visual":
        return visual_summary_template(version, context)
    
    return ""