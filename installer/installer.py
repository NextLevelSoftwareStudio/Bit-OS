#!/usr/bin/env python3
import locale, platform, sys, os, subprocess, math
from pathlib import Path
# lang = 'pt_PT', encoding = 'UTF-8'
encoding = locale.getencoding()
lang, _ = locale.getlocale()
cpu_architecture = platform.machine()
portuguese = ["português", "portuguese", "portugiesisch"]
english = ["inglês", "english", "englisch"]
german = ["alemão", "german", "deutsch"]
filesystems = ["ext4", "brtfs", "gpfs"]
nproc = os.cpu_count()

if encoding != "UTF-8":
    print("\nYour system's encoding is not UTF-8. Please change it to UTF-8 to continue.\n")
    sys.exit(1)

caminho_modelo = '/proc/device-tree/model'
if os.path.exists(caminho_modelo): # Verifica se o arquivo existe (sistemas x86 comuns não têm essa árvore de dispositivos)
    try:
        with open(caminho_modelo, 'r') as f:
            modelo = f.read().strip()
            if "Raspberry Pi 5" in modelo and cpu_architecture == "aarch64":
                RASPBERRY = True
            # If not a Raspberry Pi 5 and not aarch64, exit with code 1
            elif ("Raspberry Pi 5" in modelo is False) and (cpu_architecture == "aarch64") is False:
                sys.exit(1)
    except Exception:
        print("\nCould not read the device model.\n")

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
        entrada = input("\nQue idioma deseja definir com padrão? \n").lower()
        if entrada == "":
            entrada = "portuguese"
        elif entrada in portuguese:
            entrada = "portuguese"
        language("pt_PT.UTF-8 UTF-8")
        break
    elif lang == "en_US":
        print("Language detected: English")
        entrada = input("\nWhat language would you like to set as default? \n").lower()
        if entrada == "":
            entrada = "english"
        elif entrada in english:
            entrada = "english"
        language("en_US.UTF-8 UTF-8")
        break
    elif lang == "de_DE":
        print("Sprache erkannt: Deutsch")
        entrada = input("\nWelche Sprache möchten Sie als Standard festlegen? \n").lower()
        if entrada == "":
            entrada = "german"
        elif entrada in german:
            entrada = "german"
        language("de_DE.UTF-8 UTF-8")
        break
    else:
        print("\nLanguage doesn'y exists or ins't available.\n")


message = {
    "portuguese": "\nDeseja configurar o Portage automaticamente? (y/n)\n",
    "english": "\nDo you want to configure Portage automatically? (y/n)\n",
    "german": "\nMöchten Sie Portage automatisch konfigurieren? (y/n)\n"
}
pergunta = input(message[entrada])
if pergunta.lower() == "n":
    message = {
        "portuguese": "\nInsira o conteúdo desejado para o arquivo /etc/portage/make.conf:\n",
        "english": "\nInsert the desired content for the /etc/portage/make.conf file:\n",
        "german": "\nGeben Sie den gewünschten Inhalt für die Datei /etc/portage/make.conf ein:\n"
    }
    makeconf = input(message[entrada])
    with open('/etc/portage/make.conf', 'w') as f:
        f.write(makeconf)
elif pergunta.lower() == "y":
    lista_l10n_temp = []
    with open(localegenfile, 'w') as f:
        linhas = f.readlines()
        for i in linhas:
            if i.startswith("#") or i.strip() == "":
                continue
            else:
                lista_l10n_temp.append(i)
    # make.conf variables
    l10n = " ".join(lista_l10n_temp)
    cores = math.ceil(os.cpu_count() / 100 * 75)
    videocards = ""
