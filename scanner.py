import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================
# PORT SCANNER V2
# RED TEAM  SECURITY RESEARCH
# ============================================================
#
# AVISO
# Esta versão pública foi limitada ao localhost.
#
# O objetivo é demonstrar conceitos de reconhecimento TCP,
# não fornecer um scanner genérico para uso contra terceiros.
#
# Porta aberta não significa vulnerabilidade.
# Significa apenas que existe um serviço aceitando conexão.
#
# Banner também não é prova absoluta da identidade do serviço.
# Informações de rede podem ser ocultadas, alteradas ou imprecisas.
#
# Qualquer atividade de segurança fora de um ambiente autorizado
# exige permissão prévia e escopo claramente definido.
# ============================================================

TARGET = 127.0.0.1
TIMEOUT = 0.5
THREADS = 20

PORTS = [
    21, 22, 23, 25, 53, 80, 110, 135, 139, 143,
    443, 445, 3306, 5432, 6379, 8080
]


def service_name(port)
    try
        return socket.getservbyport(port, tcp)
    except OSError
        return Desconhecido


def scan(port)
    started = time.perf_counter()

    try
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock
            sock.settimeout(TIMEOUT)

            if sock.connect_ex((TARGET, port)) != 0
                return None

            elapsed = (time.perf_counter() - started)  1000

            return {
                port port,
                service service_name(port),
                time elapsed,
            }

    except (socket.timeout, socket.error, OSError)
        return None


def main()
    print(=  60)
    print(                 PORT SCANNER V2)
    print(=  60)

    print(n[!] AVISO DE USO)
    print([!] Esta versão pública funciona SOMENTE em localhost.)
    print([!] Ferramentas de reconhecimento devem ser usadas)
    print([!] somente em alvos para os quais exista autorização.)
    print([!] O projeto não deve ser utilizado para varredura)
    print([!] não autorizada de sistemas ou redes de terceiros.)

    print(n[] CONCEITO)
    print([] O scanner verifica se uma porta TCP aceita conexão.)
    print([] Uma porta aberta indica um serviço acessível.)
    print([] Isso, isoladamente, NÃO significa que exista)
    print([] uma vulnerabilidade no serviço.)

    print(n[] Alvo, TARGET)
    print([] Portas, len(PORTS))
    print([] Threads, THREADS)
    print([] Timeout, TIMEOUT, s)

    print(n[] Iniciando análise local...n)

    started = time.perf_counter()
    results = []

    with ThreadPoolExecutor(max_workers=THREADS) as executor
        tasks = [executor.submit(scan, port) for port in PORTS]

        for task in as_completed(tasks)
            result = task.result()

            if result
                results.append(result)

    results.sort(key=lambda item item[port])

    elapsed = time.perf_counter() - started

    if results
        print(n[+] PORTAS ENCONTRADASn)

        for result in results
            print(
                f[+] {result['port']}tcp OPEN
                f  Serviço {result['service']}
                f  Resposta {result['time'].2f} ms
            )
    else
        print(n[] Nenhuma porta aberta encontrada.)

    print(n[] CONCEITOS IMPORTANTES)
    print([] TCP utiliza uma conexão para verificar disponibilidade.)
    print([] Timeout define quanto tempo aguardamos uma resposta.)
    print([] Threads permitem processar várias verificações)
    print([] simultaneamente, reduzindo o tempo total da operação.)
    print([] O resultado deve sempre ser interpretado dentro)
    print([] do contexto do ambiente analisado.)

    print(n[!] LEMBRETE)
    print([!] Reconhecimento é uma atividade sensível.)
    print([!] Autorização e escopo vêm antes da ferramenta.)
    print([!] Sem autorização, não teste.)

    print(n + =  60)
    print(f[] Portas abertas {len(results)})
    print(f[] Tempo total {elapsed.2f}s)
    print([] Análise finalizada)
    print(=  60)


if __name__ == __main__
    main()