# Guia Rápido de Hospedagem Gratuita na Nuvem (Acesso pelo Telemóvel / Navegador)

Este projeto já está 100% configurado e pronto para ser hospedado gratuitamente na nuvem (**Render** ou **PythonAnywhere**), gerando um link público seguro (`https://...`) que pode ser aberto diretamente no navegador de qualquer telemóvel, tablet ou computador.

---

## Opção 1: Hospedar no Render.com (Recomendado — Automático)

O **Render** lê automaticamente os ficheiros `render.yaml`, `Procfile` e `requirements.txt` do projeto.

### Passo 1: Subir o projeto para o GitHub
1. Crie uma conta gratuita em [github.com](https://github.com) (caso ainda não tenha).
2. Crie um novo repositório (ex: `sistema-relatorios-concrejato`) e envie todos os ficheiros desta pasta para lá.

### Passo 2: Conectar ao Render
1. Aceda a [render.com](https://render.com) e crie uma conta gratuita (pode entrar com a sua conta do GitHub).
2. No painel do Render, clique no botão **"New +"** e selecione **"Web Service"**.
3. Conecte o repositório do GitHub onde guardou o projeto.
4. Preencha (ou confirme) as configurações abaixo:
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
   - **Instance Type**: `Free` (Gratuito)
5. Clique em **"Create Web Service"**.

### Passo 3: Aceder pelo Telemóvel
- Aguarde cerca de 2 a 3 minutos enquanto o Render instala as dependências.
- Assim que aparecer o estado **Live**, o Render mostrará o seu link no topo do ecrã (exemplo: `https://sistema-relatorios-concrejato.onrender.com`).
- Basta enviar esse link por WhatsApp ou abrir no navegador do telemóvel!

---

## Opção 2: Hospedar no PythonAnywhere (Sem precisar do GitHub)

Se preferir enviar os ficheiros diretamente sem usar o GitHub:

1. Crie uma conta gratuita (**Beginner**) em [pythonanywhere.com](https://www.pythonanywhere.com).
2. Compacte a pasta do projeto num ficheiro `.zip`, vá até ao menu **Files** do PythonAnywhere, faça o upload do `.zip` e extraia numa consola **Bash** (`unzip projeto.zip -d sistema_relatorios`).
3. Na consola **Bash**, instale as dependências:
   ```bash
   cd ~/sistema_relatorios
   pip install --user -r requirements.txt
   ```
4. Vá até ao menu **Web** -> **Add a new web app** -> escolha **Manual configuration** -> **Python 3.10+**.
5. Em **Code -> Source code**, indique `/home/SEU_USUARIO/sistema_relatorios`.
6. Clique no ficheiro **WSGI configuration file** e deixe apenas:
   ```python
   import sys
   path = '/home/SEU_USUARIO/sistema_relatorios'
   if path not in sys.path:
       sys.path.append(path)

   from run import app as application
   ```
7. Clique no botão verde **Reload** no topo da aba **Web** e aceda ao link `https://SEU_USUARIO.pythonanywhere.com` pelo telemóvel!

---

## Credenciais Padrão (Criadas Automaticamente no 1º Acesso)

- **Administrador**:
  - **Utilizador**: `admin`
  - **Palavra-passe**: `admin123`
- **Operador de Campo**:
  - **Utilizador**: `operador`
  - **Palavra-passe**: `operador123`
