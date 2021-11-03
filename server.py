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

def zmena_sshconf():
    jmeno = input("Zadejte prosim jmeno uzivatele, ktery se bude moct prihlasovat pres SSH")
    os.system(f'''sudo echo "#       $OpenBSD: sshd_config,v 1.103 2018/04/09 20:41:22 tj Exp $

# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.

# This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin

# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.

Include /etc/ssh/sshd_config.d/*.conf

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
#HostKey /etc/ssh/ssh_host_ed25519_key

# Ciphers and keying
#RekeyLimit default none

# Logging
#SyslogFacility AUTH
#LogLevel INFO

# Authentication:

#LoginGraceTime 2m
PermitRootLogin yes
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10

#PubkeyAuthentication yes

# Expect .ssh/authorized_keys2 to be disregarded by default in future.
#AuthorizedKeysFile     .ssh/authorized_keys .ssh/authorized_keys2

#AuthorizedPrincipalsFile none

#AuthorizedKeysCommand none
#AuthorizedKeysCommandUser nobody

# For this to work you will also need host keys in /etc/ssh/ssh_known_hosts
#HostbasedAuthentication no
# Change to yes if you don't trust ~/.ssh/known_hosts for
# HostbasedAuthentication
#IgnoreUserKnownHosts no
# Don't read the user's ~/.rhosts and ~/.shosts files
#IgnoreRhosts yes

# To disable tunneled clear text passwords, change to no here!
PasswordAuthentication no
#PermitEmptyPasswords no

# Change to yes to enable challenge-response passwords (beware issues with
# some PAM modules and threads)
ChallengeResponseAuthentication no

# Kerberos options
#KerberosAuthentication no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes
#KerberosGetAFSToken no

# GSSAPI options
#GSSAPIAuthentication no
#GSSAPICleanupCredentials yes
#GSSAPIStrictAcceptorCheck yes
#GSSAPIKeyExchange no

# Set this to 'yes' to enable PAM authentication, account processing,
# and session processing. If this is enabled, PAM authentication will
# be allowed through the ChallengeResponseAuthentication and
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication via ChallengeResponseAuthentication may bypass
# the setting of "PermitRootLogin without-password".
# If you just want the PAM account and session checks to run without
# PAM authentication, then enable this but set PasswordAuthentication
# and ChallengeResponseAuthentication to 'no'.
UsePAM yes

#AllowAgentForwarding yes
#AllowTcpForwarding yes
#GatewayPorts no
X11Forwarding yes
#X11DisplayOffset 10
#X11UseLocalhost yes
#PermitTTY yes
PrintMotd no
#PrintLastLog yes
#TCPKeepAlive yes
#PermitUserEnvironment no
#Compression delayed
#ClientAliveInterval 0
#ClientAliveCountMax 3
#UseDNS no
#PidFile /var/run/sshd.pid
#MaxStartups 10:30:100
#PermitTunnel no
#ChrootDirectory none
#VersionAddendum none

# no default banner path
#Banner none

# Allow client to pass locale environment variables
AcceptEnv LANG LC_*

# override default of no subsystems
Subsystem       sftp    /usr/lib/openssh/sftp-server

# Example of overriding settings on a per-user basis
#Match User anoncvs
#       X11Forwarding no
#       AllowTcpForwarding no
#       PermitTTY no
#       ForceCommand cvs server
AllowUsers {jmeno}" > /etc/ssh/sshd_config''')
    os.system("sudo systemctl restart sshd")


main()

