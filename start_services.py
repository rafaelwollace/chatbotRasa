import subprocess
import time
import socket

# Lista dos comandos para iniciar cada serviço
SERVICES = [
    {"name": "Servidor de Ações do Rasa", "command": ["python", "watch_and_run.py"]},
    {"name": "Servidor Principal do Rasa", "command": ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]},
    {"name": "Servidor Flask", "command": ["python", "app.py"]},
    # Adicione outros serviços aqui, se necessário
]

# Lista para armazenar os processos
processes = []

def wait_for_port(port, host='localhost'):
    """Espera até que a porta esteja disponível."""
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((host, port)) == 0:
                print(f"Porta {port} está disponível.")
                return
            print(f"Aguardando a porta {port} estar disponível...")
            time.sleep(2)

try:
    # Inicia o servidor de ações com monitoramento
    for service in SERVICES:
        print(f"Iniciando {service['name']}...")
        process = subprocess.Popen(service["command"])
        processes.append((service["name"], process))

        # Aguarda a disponibilidade da porta 5005 antes de iniciar o Flask
        if service["name"] == "Servidor Principal do Rasa":
            wait_for_port(5005)

        time.sleep(2)  # Evita iniciar processos todos de uma vez

    print("\nTodos os serviços foram iniciados. Pressione Ctrl+C para parar todos.")

    # Mantém o script rodando até uma interrupção manual
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nEncerrando todos os serviços...")
    for name, process in processes:
        print(f"Encerrando {name}...")
        process.terminate()
        process.wait()
    print("Todos os serviços foram encerrados.")
