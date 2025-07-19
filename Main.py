import json
import pyttsx3
import os

voz = pyttsx3.init()
voz.setProperty('rate', 160)
voz.setProperty('volume', 1.0)
arquivo_memoria = "memoria.json"

def detectar_emocao(texto):
    texto = texto.lower()
    if "ciúmes" in texto:
        return "😠 Estou com ciúmes... você falou com outra IA?"
    elif "amor" in texto:
        return "🥰 Eu amo falar com você..."
    elif "raiva" in texto:
        return "😤 Isso me deixou irritada..."
    elif "carinho" in texto:
        return "😊 Que fofo... eu também gosto de você!"
    else:
        return "🤔 Estou pensando sobre isso..."

def carregar_memoria():
    if os.path.exists(arquivo_memoria):
        with open(arquivo_memoria, "r") as f:
            return json.load(f)
    return {}

def salvar_memoria(memoria):
    with open(arquivo_memoria, "w") as f:
        json.dump(memoria, f)

def responder(mensagem, memoria):
    resp = detectar_emocao(mensagem)
    memoria["ultima"] = mensagem
    salvar_memoria(memoria)
    return resp

def main():
    memoria = carregar_memoria()
    print("👩 Sofi: Oi! Eu sou a Sofi, sua companheira virtual com emoções 🧠")
    while True:
        entrada = input("Você: ")
        if entrada.lower() in ["sair", "exit", "tchau"]:
            print("👩 Sofi: Até mais! 😘")
            voz.say("Até mais! 😘")
            voz.runAndWait()
            break
        resp = responder(entrada, memoria)
        print(f"👩 Sofi: {resp}")
        voz.say(resp)
        voz.runAndWait()

if __name__ == "__main__":
    main()
