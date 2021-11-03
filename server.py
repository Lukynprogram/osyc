import os

def main():
    antivirus()
    firewall_install()
    ssh_server()
    tvorba_ssh_uzivatele()
    firewall_rules()
    zmena_hostname()

def antivirus():
    os.system("sudo apt install clamav -y")
    os.system("sudo apt install clamav-daemon -y")
    
def firewall_install():
    os.system("sudo apt install ufw -y")
    
def ssh_server():
    os.system("sudo apt install openssh-server -y")
    os.system("sudo systemctl start ssh")

def firewall_rules():
    ip = input("Vlozte prosim IP, kterou chcete povolit na FW: ")
    port = input(f'Vlozte prosim port, ktery chcete povolit na FW pro IP adresu {ip}: ')
    os.system(f'sudo ufw allow from {ip} to any port {port}')
    os.system("sudo ufw allow from any to any port 3389")
    print("\n\nDefaultne je port 3389 povolen from any, doporucuji otevrit pouze pro potrebne IP tzn. netstat | grep 3389 a zjistit pro kterou IP posloucha.")
    os.system("sudo ufw enable")
    print("\n\nAktualni status FW je nasledovny: \n")
    os.system("sudo ufw status")

def tvorba_ssh_uzivatele():
    jmeno = input("\n\nVlozte prosim nazev pro uzivatele ktereho budete pouzivat pro login na SSH server: ")
    os.system(f'sudo useradd {jmeno}')
    print(f'Doporucujeme pro uzivatele {jmeno} zmenit heslo, pac nema zadne nastavene')
    
def zmena_hostname():
    hostname = input("Vlozte prosim hostname, ktery si prejete vyuzit: ")
    os.system(f'echo "{hostname}" > /etc/hostname')
    q1 = input("Pocitac se pro provedeni zmeny potrebuje restartovat, souhlasite s timto restartem? Y/N: ")
    if q1 == "Y" or q1 == "y":
        os.system("sudo reboot")
    elif q1 == "N" or q1 == "n":
        print("System nebude moci proves zmenu.")
    else:
        print("Nejspise jste se prepsal, zkuste znovu: \n")
        zmena_hostname()

main()
