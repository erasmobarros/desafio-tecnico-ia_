import os
import json
import hashlib
import time
from datetime import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from prompt_engine.builder import build_prompt


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)


CACHE_DIR = "cache"
HISTORY_FILE = "outputs/history.json"
STUDENTS_FILE = "profiles/Estudantes.json"


os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs("outputs", exist_ok=True)




def get_cache_key(prompt):
    return hashlib.md5(prompt.encode()).hexdigest()

def load_cache(key):
    path = f"{CACHE_DIR}/{key}.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_cache(key, data):
    with open(f"{CACHE_DIR}/{key}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)



def save_history(entry):
    history = []
    
   
    if os.path.exists(HISTORY_FILE):
        if os.path.getsize(HISTORY_FILE) > 0:
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    history = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Aviso: history.json estava vazio ou corrompido. Iniciando novo histórico.")
                history = []

    history.append(entry)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)




def generate_content(prompt, max_tentativas=3):
    for tentativa in range(max_tentativas):
        try:
           
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text

        except errors.ClientError as e:
            if e.code == 404:
                return "Erro 404: O modelo especificado não foi encontrado na API."
            return f"Erro de cliente: {str(e)}"
            
        except errors.ServerError as e:
            if e.code == 503:
                tempo_espera = 2 ** tentativa 
                print(f"⚠️ Servidor ocupado. Tentativa {tentativa + 1} de {max_tentativas}. Aguardando {tempo_espera}s...")
                time.sleep(tempo_espera)
            else:
                return f"Erro no servidor do Google: {str(e)}"
                
        except Exception as e:
            return f"Erro inesperado: {str(e)}"
            
    return "Erro: Não foi possível acessar a API após várias tentativas."




def load_students():
    with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



@app.route("/", methods=["GET", "POST"])
def index():
    students = load_students()
    result = None

    if request.method == "POST":
        student_index = int(request.form["student"])
        topic = request.form["topic"]
        content_type = request.form["content_type"]
        version = request.form["version"]

        student = students[student_index]
        prompt = build_prompt(version, content_type, student, topic)

        cache_key = get_cache_key(prompt)
        cached = load_cache(cache_key)

        if cached:
            print("⚡ Retornando do Cache!")
            result = cached
        else:
            print("🧠 Gerando via API Gemini...")
            result = generate_content(prompt)
            if not result.startswith("Erro"):
                save_cache(cache_key, result)

        save_history({
            "timestamp": str(datetime.now()),
            "student": student,
            "topic": topic,
            "content_type": content_type,
            "version": version,
            "output": result
        })

    return render_template("index.html", students=students, result=result)


if __name__ == "__main__":
    app.run(debug=True)