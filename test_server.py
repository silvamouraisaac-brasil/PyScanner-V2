import socket

# ============================================================
# HEX SERVER
# DEMONSTRAÇÃO LOCAL DE SOCKET TCP
# ============================================================
#
# AVISO:
# Este código é apenas uma demonstração conceitual.
#
# O servidor está restrito ao localhost para impedir que a
# versão pública seja utilizada como serviço de rede genérico.
#
# O objetivo é visualizar o conceito de:
#   - socket
#   - conexão TCP
#   - cliente e servidor
#   - resposta simples
#
# Não é um servidor de produção.
# Não foi desenvolvido para exposição pública.
# ============================================================

HOST = "127.0.0.1"
PORT = 8080

print("=" * 50)
print("              HEX SERVER")
print("=" * 50)

print("\n[!] AVISO")
print("[!] Demonstração exclusivamente local.")
print("[!] O servidor permanece limitado ao localhost.")
print("[!] Não utilize este código para expor serviços.")
print("[!] Código educacional e deliberadamente limitado.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"\n[*] Serviço local: {HOST}:{PORT}")
print("[*] Aguardando conexão...\n")

while True:
    client, address = server.accept()

    print("[+] Conexão local recebida.")

    # Resposta mínima apenas para demonstrar comunicação TCP.
    client.sendall(b"OK")

    client.close()

    print("[*] Conexão encerrada.")