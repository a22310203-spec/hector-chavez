import json
import os

# Archivo donde guardaremos la base de conocimiento
BASE_FILE = "conocimiento.json"

# Base inicial precargada
base_inicial = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Muy bien, gracias. ¿Y tú?",
    "de que te gustaria hablar": "Podemos hablar de tecnología, ciencia o lo que quieras."
}

# Cargar conocimiento previo o crear archivo
if os.path.exists(BASE_FILE):
    with open(BASE_FILE, "r", encoding="utf-8") as f:
        base_conocimiento = json.load(f)
else:
    base_conocimiento = base_inicial
    with open(BASE_FILE, "w", encoding="utf-8") as f:
        json.dump(base_conocimiento, f, indent=4, ensure_ascii=False)

print("🤖 Chatbot iniciado. Escribe 'salir' para terminar.\n")

while True:
    pregunta = input("Tú: ").lower().strip()
    
    if pregunta == "salir":
        print("🤖 Chatbot: ¡Hasta luego!")
        break
    
    if pregunta in base_conocimiento:
        print("🤖 Chatbot:", base_conocimiento[pregunta])
    else:
        print("🤖 Chatbot: No sé la respuesta. ¿Qué debería responder?")
        nueva_respuesta = input("Enséñame: ")
        
        # Guardar en la base de conocimiento
        base_conocimiento[pregunta] = nueva_respuesta
        with open(BASE_FILE, "w", encoding="utf-8") as f:
            json.dump(base_conocimiento, f, indent=4, ensure_ascii=False)
        
        print("🤖 Chatbot: ¡Gracias! He aprendido algo nuevo.")
