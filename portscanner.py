import socket
import concurrent.futures

address = str(input("Enter ip to scan: "))

def scan(ip):
    s = socket.socket()
    s.settimeout(3.5)
    try:
        s.connect((address,ip))
    except:
        return
    print(f"[+] Port {ip} is open")
    return(ip)

def main():
    ports = int(input("Enter max port: "))
    threads = int(input("How Many Threads: "))
    openports = []
    with concurrent.futures.ThreadPoolExecutor(threads) as executor:
        x = executor.map(scan,range(ports))

    for i in x:
        if i != None:
            openports.append(i)
    print(openports)
    
main()
