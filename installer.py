#!/usr/bin/env python3
import locale, platform, sys, os, subprocess
from pathlib import Path
# lang = 'pt_PT', encoding = 'UTF-8'
encoding = locale.getencoding()
lang, _ = locale.getlocale()
cpu_architecture = platform.machine()
portuguese = ["português", "portuguese", "portugiesisch"]
english = ["inglês", "english", "englisch"]
german = ["alemão", "german", "deutsch"]
filesystems = ["ext4", "brtfs", "gpfs"]

if encoding != "UTF-8":
    print("Your system's encoding is not UTF-8. Please change it to UTF-8 to continue.")
    sys.exit(1)

caminho_modelo = '/proc/device-tree/model'
if os.path.exists(caminho_modelo): # Verifica se o arquivo existe (sistemas x86 comuns não têm essa árvore de dispositivos)
    try:
        with open(caminho_modelo, 'r') as f:
            modelo = f.read().strip()
            if "Raspberry Pi 5" in modelo and cpu_architecture == "aarch64":
                RASPBERRY = True
            # If not a Raspberry Pi 5 and not aarch64, exit with code 1
            elif "Raspberry Pi 5" in modelo is False and (cpu_architecture == "aarch64") is False:
                sys.exit(1)
    except Exception:
        print("Could not read the device model.")

localegenfile = Path('/etc/locale.gen')
def language(data):
    with open(localegenfile, 'a') as f:
        f.write(data)
    subprocess.run(['locale-gen'])

while True:
    with open(localegenfile, 'w') as f: # apagando o conteúdo do arquivo para apagar locales antigos
        pass
    if lang == "pt_PT":
        print("Idioma detectado: Português")
        entrada = input("Que idioma deseja definir com padrão? ").lower()
        if entrada == "":
            entrada = "portuguese"
        elif entrada in portuguese:
            entrada = "portuguese"
        language("pt_PT.UTF-8 UTF-8")
        break
    elif lang == "en_US":
        print("Language detected: English")
        entrada = input("What language would you like to set as default? ").lower()
        if entrada == "":
            entrada = "english"
        elif entrada in english:
            entrada = "english"
        language("en_US.UTF-8 UTF-8")
        break
    elif lang == "de_DE":
        print("Sprache erkannt: Deutsch")
        entrada = input("Welche Sprache möchten Sie als Standard festlegen? ").lower()
        if entrada == "":
            entrada = "german"
        elif entrada in german:
            entrada = "german"
        language("de_DE.UTF-8 UTF-8")
        break
    else:
        print("Language doesn'y exists or ins't available.")


message = {
    "portuguese": "Deseja configurar o portage manualmente ou automaticamente? (y/n)",
    "english": "Do you want to configure portage manually or automatically? (y/n)",
    "german": "Möchten Sie Portage manuell oder automatisch konfigurieren? (y/n)"
}
pergunta = input(message[entrada])










# wget use flags configuration
wgetuseflagsfile = Path('/etc/portage/package.use/net-misc/wget')
with open(wgetuseflagsfile, 'w') as f:
    f.write('net-misc/wget ssl idn nls verify-sig metalink libproxy cookie-check')
try:
    subprocess.run(['emerge', '--sync'], check=True)
    subprocess.run(['emerge', '--ask', 'net-misc/curl'], check=True)
except subprocess.CalledProcessError:
    print("Error occurred while installing wget.")