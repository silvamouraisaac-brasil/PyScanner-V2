# ⚠️ AVISOS — PORT SCANNER V2

## LEIA ANTES DE UTILIZAR

Este repositório contém código relacionado a **Red Team, reconhecimento de rede e pesquisa em cibersegurança**.

O material disponibilizado publicamente foi **intencionalmente limitado**.

O objetivo deste projeto é apresentar conceitos de desenvolvimento de ferramentas de segurança sem transformar o repositório em um guia operacional para atividades ofensivas.

---

## 🔴 USO AUTORIZADO

Qualquer ferramenta de segurança deve ser utilizada somente dentro de um ambiente em que exista autorização adequada.

Isso inclui, por exemplo:

* infraestrutura própria;
* ambientes de teste controlados;
* laboratórios de segurança;
* atividades profissionais com escopo autorizado;
* avaliações de segurança devidamente aprovadas.

**Não utilize o projeto contra sistemas ou redes de terceiros sem autorização.**

---

## ⚠️ RECONHECIMENTO NÃO É INVASÃO

Uma distinção importante:

> Encontrar uma porta aberta não significa encontrar uma vulnerabilidade.

Uma porta aberta pode simplesmente indicar que existe um serviço aguardando conexões.

Da mesma forma:

> Identificar um serviço não significa que ele possa ser explorado.

Resultados de ferramentas de reconhecimento precisam ser interpretados dentro do contexto do ambiente analisado.

---

## 🧠 POR QUE O CÓDIGO É LIMITADO?

As versões publicadas neste repositório possuem restrições deliberadas.

Isso é intencional.

O projeto procura demonstrar conceitos de programação e segurança sem disponibilizar uma ferramenta genérica voltada para reconhecimento de terceiros.

Por esse motivo, determinadas funcionalidades podem estar:

```text
[!] limitadas
[!] removidas
[!] simplificadas
[!] restritas ao ambiente local
```

A ausência dessas funcionalidades não representa necessariamente uma limitação técnica do conceito estudado.

É uma decisão de segurança para a versão pública.

---

## 🔐 SOBRE O HEX SERVER

O `HexServer` é uma demonstração local de comunicação através de sockets TCP.

Ele existe para representar, de maneira simples, a relação:

```text
CLIENTE
   │
   │ conexão TCP
   ▼
SERVIDOR
   │
   │ resposta
   ▼
CLIENTE
```

A implementação pública permanece limitada ao `localhost`.

Ela não deve ser interpretada como servidor de produção ou como implementação destinada à exposição pública.

---

## 🔎 SOBRE O PORT SCANNER

O Port Scanner v2 representa conceitos associados ao reconhecimento de serviços TCP.

Entre os conceitos envolvidos estão:

```text
TCP
Sockets
Portas
Timeout
Concorrência
Serviços de rede
Reconhecimento
```

O projeto não pretende ensinar invasão, exploração ou evasão de mecanismos de segurança.

---

## 🚫 O QUE ESTE REPOSITÓRIO NÃO É

Este projeto não é:

* um manual de invasão;
* um guia de exploração;
* um curso de Red Team;
* um conjunto de instruções para atacar terceiros;
* uma ferramenta destinada a contornar controles de segurança;
* uma autorização para testar qualquer infraestrutura.

---

## 📋 ESCOPO

A autorização deve existir **antes** da utilização da ferramenta.

Não é suficiente descobrir depois que determinado teste era permitido.

O responsável pelo teste deve conhecer previamente:

```text
ALVO
ESCOPO
PERMISSÃO
PERÍODO
REGRAS DE ENGAJAMENTO
LIMITAÇÕES
```

---

## ⚖️ RESPONSABILIDADE

O usuário é responsável por verificar as leis, contratos, políticas internas e regras aplicáveis ao ambiente em que qualquer ferramenta de segurança será utilizada.

O autor não assume responsabilidade por utilização indevida do código.

O fato de uma ferramenta estar disponível publicamente não significa que qualquer utilização seja permitida.

---

## 🛡️ PRINCÍPIO DO PROJETO

A filosofia deste repositório é simples:

> **Segurança ofensiva exige autorização.**

> **Conhecimento técnico não substitui permissão.**

> **Ferramentas devem ser utilizadas dentro de um escopo definido.**

> **Sem autorização, não teste.**

---

## 📌 AVISO FINAL

Se você não possui autorização explícita para analisar determinado sistema ou rede:

**não realize o teste.**

Use ambientes próprios, laboratórios controlados ou avaliações nas quais o escopo tenha sido formalmente definido.

---

<div align="center">

### `PORT SCANNER V2`

**Red Team · Security Research · Authorized Testing**

`Código público limitado por design.`

</div>
