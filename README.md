# smart-directory-cleaner
python script to automatically organize files by type (images, documents, etc). perfect for messy folders!

# 📂 Smart Directory Cleaner

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Script Python que organiza automaticamente arquivos em pastas por tipo (.pdf, .jpg, .py, etc). Ideal para limpar diretórios desorganizados.

## 🚀 Como Usar

1. Clone o repositório:
bash
git clone https://github.com/seu-usuario/smart-directory-cleaner.git
cd smart-directory-cleaner


2. Execute o script (substitua pelo seu caminho):
bash
# Linux/Mac
python3 organizer.py --path "~/Downloads"

# Windows
py organizer.py --path "C:\Users\SeuNome\Downloads"


> ⚠ Dica: Teste primeiro com uma cópia da sua pasta!

## 🛠 Tecnologias
- Python 3
- Bibliotecas nativas:
  - os (manipulação de arquivos)
  - shutil (operações de movimentação)

## 📌 Exemplo
Estrutura antes:

Downloads/
├── relatorio.pdf
├── foto.jpg
└── script.py


Estrutura depois:

Downloads/
├── Documents/
│   └── relatorio.pdf
├── Images/
│   └── foto.jpg
└── Scripts/
    └── script.py


## 📄 Licença
Distribuído sob licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.