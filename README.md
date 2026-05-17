Bit-OS

O **Bit-OS** é uma distribuição Linux personalizada baseada em Gentoo, desenvolvida para oferecer a máxima performance, controlo e simplicidade. Funciona sob o modelo **Rolling Release** com atualizações totalmente **opcionais**, garantindo que o utilizador tem a decisão final sobre quando e o que atualizar no seu sistema.

A identidade da distribuição assenta no **BPM (Bit-OS Package Manager)**, um gestor de pacotes híbrido criado especificamente para este ecossistema. O Bit-OS utiliza exclusivamente o **OpenRC** como sistema de inicialização e oferece suporte oficial para a arquitetura `amd64` (PCs modernos) e para o mini-computador **Raspberry Pi 5** (`arm64`).

---

## 🚀 Características Principais

* **BPM (Bit-OS Package Manager):** Um orquestrador de pacotes único capaz de descarregar e gerir software a partir do Portage (Gentoo), do Pip (Python) e de repositórios com uma estrutura própria nativa do Bit-OS.
* **Modelo Rolling Release Controlado:** O sistema disponibiliza pacotes continuamente atualizados, mas as atualizações são 100% opcionais.
* **Foco no OpenRC:** Sistema de inicialização leve, tradicional, rápido e livre das complexidades do systemd.
* **Controlo de Versão por Commits:** Como a estrutura da distro assenta no Git, utilizadores avançados têm a flexibilidade de retroceder o estado global do sistema para commits específicos do repositório.
* **Suporte Multi-Plataforma:** Compatibilidade total com PCs de 64 bits (`amd64`) e otimização dedicada para o **Raspberry Pi 5**.

---

## 🌐 Idiomas Suportados

Para garantir consistência e uma tradução otimizada das ferramentas nativas e do instalador, o Bit-OS suporta exclusivamente os seguintes locales:

* **Português (Portugal)** — `pt_PT`
* **Deutsch (Deutschland)** — `de_DE`
* **English (United States)** — `en_US`

---

## 🖥️ Edições e Ambientes de Trabalho

Por padrão, o Bit-OS instala um sistema puramente focado em **Modo Terminal (CLI)**. No entanto, oferece suporte oficial para a instalação dos seguintes ambientes gráficos:

* **KDE Plasma:** Versão padrão (*vanilla*) ou a **versão modificada customizada para o Bit-OS**.
* **GNOME:** Versão padrão (*vanilla*) ou a **versão modificada customizada para o Bit-OS**.

---

## ⚙️ Requisitos do Sistema

Devido ao fluxo de compilação de pacotes herdado do Gentoo e gerido pelo BPM, são recomendados os seguintes requisitos de hardware:

* **Armazenamento:** No mínimo **80 GB** de espaço livre.
* **Tipo de Disco:** Altamente recomendado o uso de um **SSD (Solid State Drive)** para acelerar os tempos de leitura/escrita durante as compilações.

---

## 🛠️ Como Instalar

1. Baixe o Gentoo Minimal Installation CD (openrc).
2. Crie uma mídia de armazenamento bootável, usando preferêncialmente o comando dd do Linux.
3. Bootar o seu dispositivo pela mídia.
4. Faça login como root.
5. Rode os seguintes comandos:
```bash
emerge --ask dev-vcs/git dev-lang/python
mkdir -p /root/Bit-OS/temporario
git -C /root/Bit-OS/temporario init
git -C /root/Bit-OS/temporario remote add origin https://github.com/NextLevelSoftwareStudio/Bit-OS.git
git -C /root/Bit-OS/temporario config core.sparseCheckout true
echo "installer/" >> /root/Bit-OS/temporario/.git/info/sparse-checkout
git -C /root/Bit-OS/temporario pull origin main
mv /root/Bit-OS/temporario/installer /root/Bit-OS/
rm -rf /root/Bit-OS/temporario
python /root/Bit-OS/installer/installer.py
```