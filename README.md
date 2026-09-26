<div align="center">

# Port Scanner

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=00FF00&center=true&vCenter=true&width=600&lines=TCP+Port+Scanner;Network+Security+Tool;Built+with+Python" alt="Typing SVG" />

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/TCP-Networking-00A67D?style=for-the-badge">
<img src="https://img.shields.io/badge/Security-Education-8A2BE2?style=for-the-badge">

</div>

*

## About

A lightweight **TCP Port Scanner** built with Python for studying networking, sockets and cybersecurity.

*

## Features

* TCP port scanning
* Custom port ranges
* Common ports scan
* Multithreading
* Configurable timeout
* Service identification
* Banner grabbing
* Basic service detection
* Response time
* Scan progress
* Local test server

-

## Usage

```bash
python scanner.py
```

For local testing:

```bash
python test_server.py
```

Test server:

```text
127.0.0.1:8080
```

*

## Example

```text
[*] Target: 127.0.0.1
[*] Mode: Common Ports
[*] Threads: 20
[*] Timeout: 0.5s

[*] Starting scan...

[+] 135/tcp OPEN | Service: epmap
[+] 445/tcp OPEN | Service: microsoft-ds
[+] 8080/tcp OPEN | Service: HTTP

[*] Scan finished
```

*

## Tech Stack

```text
Python
Socket Programming
TCP/IP
ThreadPoolExecutor
Network Security
```

*

## Structure

```text
Port-Scanner/
├── scanner.py
├── test_server.py
└── README.md
```

*

## Disclaimer

Developed for **educational purposes and authorized security testing only**.

Only scan systems you own or have explicit permission to test.

*

<div align="center">

### Network • Code • Security

**Built by Isaac's code**

</div>
