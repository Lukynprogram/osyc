import os

def main():
    antivirus()
    zmena_hostname()
    tvorba_id_rsa()
    prenos_klice()

def antivirus():
    os.system("sudo apt install clamav -y")
    os.system("sudo apt install clamav-daemon -y")
    
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
        
def tvorba_id_rsa():
    os.system("ssh-keygen")

def prenos_klice():
    uzivatel = input("Prosim zadejte uzivatele pro prihlaseni na SSH: ") 
    ip_addr = input("Vlozte prosim IP adresu serveru: ")
    os.system(f'ssh-copy-id -i /home/$USER/.ssh/id_rsa.pub {uzivatel}@{ip_addr}')

main()
