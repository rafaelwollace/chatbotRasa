from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL do servidor Rasa (ajuste a porta conforme necessário)
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    # Dados para enviar ao Rasa
    payload = {
        "sender": "user",
        "message": user_message
    }
    
    try:
        print(f"Enviando mensagem ao Rasa: {payload}")
        rasa_response = requests.post(RASA_URL, json=payload)
        rasa_response.raise_for_status()
        response_data = rasa_response.json()
        
        # Exibir a resposta completa do Rasa no log para diagnóstico
        print(f"Resposta recebida do Rasa: {response_data}")

        if response_data and "text" in response_data[0]:
            bot_response = response_data[0]["text"]
        else:
            bot_response = "Desculpe, não entendi sua pergunta."
        
        return jsonify({"response": bot_response})
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao comunicar com o Rasa: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
