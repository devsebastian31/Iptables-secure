import sys
import os
import subprocess

os.system("clear")

print("\033[34m .___        __        ___.   .__                  \033[0m")
print("\033[34m |   |______/  |______ \_ |__ |  |   ____   ______ \033[0m")
print("\033[34m |   \____ \   __\__  \ | __ \|  | _/ __ \ /  ___/ \033[0m")
print("\033[34m |   |  |_> >  |  / __ \| \_\ \  |_\  ___/ \___ \  \033[0m")
print("\033[34m |___|   __/|__| (____  /___  /____/\___  >____  > \033[0m")
print("\033[34m     |__|             \/    \/          \/     \/  \033[0m")


def proteger_syn_flood():
    # Lógica para la protección contra ataques SYN flood
    os.system("iptables -A INPUT -p tcp --syn -m limit --limit 5/s -j ACCEPT")
    os.system("iptables -A INPUT -p tcp --syn -j DROP")
    print("\nProtección contra ataques SYN flood activada")



def limitar_acceso_ssh():
    # Lógica para limitar el acceso SSH
    ip_address = input("\n[+] Ingrese la IP de confianza: ")
    # Comando para bloquear la dirección IP utilizando iptables
    command = f"iptables -A INPUT -p tcp --dport 22 -s {ip_address} -j ACCEPT"
    # Ejecutar el comando utilizando el módulo subprocess
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
    os.system("iptables -A INPUT -p tcp --dport 22 -j DROP")
    print("\nAcceso SSH limitado")



def prevenir_ataques_dos():
    # Lógica para prevenir ataques DoS
    os.system("\niptables -A INPUT -p tcp --syn --dport 80 -m connlimit --connlimit-above 20 -j DROP")
    os.system("iptables -A INPUT -p tcp --dport 80 -m limit --limit 50/minute --limit-burst 30 -j ACCEPT")
    print("\nPrevención de ataques DoS activada")



def evitar_escaneo_de_puertos():
    # Lógica para evitar el escaneo de puertos
    os.system("\niptables -N SCANNER_PROTECTION")
    os.system("iptables -A SCANNER_PROTECTION -p tcp --tcp-flags ALL NONE -j DROP")
    os.system("iptables -A SCANNER_PROTECTION -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP")
    print("\nPrevención de escaneo de puertos activada")



def bloquear_IP():
    # Lógica para bloquear IP
    ip_address = input("\n[+] Ingrese la IP que desea bloquear: ")
    
    # Comando para bloquear la dirección IP utilizando iptables
    command = f"iptables -A INPUT -s {ip_address} -j DROP"
    
    # Ejecutar el comando utilizando el módulo subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"\n[+] La dirección IP {ip_address} ha sido bloqueada exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")



def menu_principal():
    while True:
        print("\n[1] Protección contra ataques SYN flood")
        print("[2] Limitar el acceso SSH")
        print("[3] Prevenir ataques DoS")
        print("[4] Evitar escaneo de puertos")
        print("[5] Bloquear IP")
        print("[6] Salir")
        
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        
        if opcion == "1":
            proteger_syn_flood()
        elif opcion == "2":
            limitar_acceso_ssh()
        elif opcion == "3":
            prevenir_ataques_dos()
        elif opcion == "4":
            evitar_escaneo_de_puertos()
        elif opcion == "5":
            bloquear_IP()
        elif opcion == "6":
            os.system("clear")
            print("[+] Saliendo del programa.")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_principal()