# Sistema Digital de Relatórios Empresariais (v0.2)

Aplicação web desenvolvida em Python (Flask) para digitalizar, armazenar, gerar em PDF de alta fidelidade e enviar por e-mail os relatórios operacionais:
1. **Controle Prévio ao Início dos Trabalhos** (Frente & Verso)
2. **Diário de Atividades de Manutenção** (Com atividades dinâmicas e múltiplas assinaturas)

---

## Funcionalidades Implementadas (v0.2)

- **Aba 1 — Controle Prévio ao Início dos Trabalhos**:
  - Formulário digital cobrindo 100% dos campos das fotos de referência (Frente e Verso).
  - Preenchimento rápido de data e hora atual.
  - Seleção múltipla para Tipos de Trabalho, Riscos Previstos e Proteções/EPIs.
  - Seleção de Condições Ambientais (Área, Tráfego, Meteorologia e Condições Especiais).
  - Verificação visual de Ferramentas e Condições Psicofísicas.
  - Campo amplo de Observações e Comentários.
  - Declaração de responsabilidade e quadro de **assinatura digital na tela** (Touchscreen no celular/tablet e mouse no desktop).

- **Aba 2 — Diário de Atividades de Manutenção**:
  - Cabeçalho (Empresa, Equipe, Executante e Data).
  - **Estrutura Dinâmica de Atividades**: Adicione quantas atividades forem necessárias através do botão `[ + Adicionar Atividade ]` ou remova antes de finalizar.
  - Campos completos de cada atividade: Descrição, O.S., Cliente (Industrial/Residencial), Tipo (Manutenção/Emergência), Período Improdutivo, Horários de Início e Fim, Nº, Deslocamento, Local, Município, Bairro e Observações.
  - **4 Quadros de Assinaturas Contratadas**: Executante, Responsável, Supervisão e GN SPS.

- **Relatórios Salvos e Consulta**:
  - Painel com filtros avançados por Tipo de Documento, Status, Data, Usuário e busca textual.
  - Ações para cada relatório: **Visualizar**, **Editar**, **Gerar PDF**, **Baixar PDF** e **Enviar por E-mail**.

- **Geração de PDF (ReportLab)**:
  - Geração de arquivos PDF diagramados com máxima fidelidade aos formulários físicos originais, com bordas, caixas `[X]`, numeração de páginas oficial e inclusão das assinaturas digitais desenhadas.
  - Nomenclatura organizada: `CONTROLE_PREVIO_AAAA-MM-DD_<id>.pdf` e `DIARIO_MANUTENCAO_AAAA-MM-DD_<id>.pdf`.

- **Módulo de Envio por E-mail**:
  - Disparo de e-mail com anexo automático do PDF gerado.
  - Suporte a SMTP real e **Modo de Simulação Seguro** (para testes em desenvolvimento sem necessidade imediata de credenciais de e-mail reais).
  - Histórico de auditoria e log de envios de e-mail no banco de dados.

- **Controle de Acessos e Usuários**:
  - Usuários com senhas criptografadas (PBKDF2).
  - Níveis de acesso: **ADMINISTRADOR** e **OPERADOR**.
  - Painel administrativo para cadastrar, editar e ativar/desativar usuários.

---

## Como Executar o Sistema

### 1. Pré-requisitos
- Python 3.10 ou superior instalado.

### 2. Instalação das Dependências
No terminal, na pasta raiz do projeto, execute:
```bash
pip install -r requirements.txt
```

### 3. Execução da Aplicação
Execute o comando:
```bash
python run.py
```
O banco de dados SQLite será inicializado automaticamente na primeira execução e o servidor estará disponível em:
👉 **http://127.0.0.1:5000**

---

## Credenciais de Acesso Inicial

| Papel | Usuário | Senha | Descrição |
| :--- | :--- | :--- | :--- |
| **Administrador** | `admin` | `admin123` | Acesso total, gerenciamento de usuários e auditoria |
| **Operador** | `operador` | `operador123` | Preenchimento, salvamento e exportação de relatórios |

---

## Estrutura do Projeto

```
Sistema_Digital_Relatorios/
│
├── app/
│   ├── __init__.py              # Factory da aplicação Flask
│   ├── config.py                # Configurações do sistema e variáveis de ambiente
│   ├── models/                  # Modelos de banco de dados (SQLAlchemy)
│   │   ├── user.py              # Usuários e papéis
│   │   ├── controle_previo.py   # Modelo do Controle Prévio
│   │   ├── diario.py            # Modelo do Diário e Atividades Dinâmicas
│   │   └── audit.py             # Histórico e logs de e-mail
│   ├── routes/                  # Rotas da aplicação (Blueprints)
│   │   ├── auth.py              # Login e logout
│   │   ├── main.py              # Dashboard e listagem de relatórios
│   │   ├── controle_previo.py   # CRUD e ações do Controle Prévio
│   │   ├── diario.py            # CRUD e ações do Diário
│   │   ├── admin.py             # Administração de usuários e logs
│   │   └── api.py               # Endpoints REST
│   ├── services/                # Regras de negócio
│   │   ├── pdf_generator.py     # Gerador de PDF de alta fidelidade
│   │   ├── email_service.py     # Envio de e-mail com anexo e simulação
│   │   └── audit_service.py     # Registro de auditoria
│   ├── static/                  # CSS e JavaScript customizados
│   └── templates/               # Templates HTML responsivos (Bootstrap 5)
│
├── documentos_referencia/       # Imagens originais dos documentos físicos
├── instance/                    # Banco SQLite local
├── generated_pdfs/              # Armazenamento de PDFs e JPGs gerados
├── run.py                       # Ponto de entrada (Local e Nuvem / WSGI)
├── Procfile                     # Configuração de servidor web na nuvem (Gunicorn)
├── render.yaml                  # Blueprint de deploy automático no Render.com
├── GUIA_DEPLOY_NUVEM.md         # Guia rápido passo a passo para hospedar na nuvem
└── requirements.txt             # Dependências completas do sistema
```

---

## Hospedagem Gratuita na Nuvem (Acesso pelo Telemóvel)

O projeto já está configurado com `Procfile`, `render.yaml`, `gunicorn` e escuta em `0.0.0.0` com porta dinâmica (`PORT`).
Consulte o guia passo a passo completo em **[GUIA_DEPLOY_NUVEM.md](GUIA_DEPLOY_NUVEM.md)** para publicar gratuitamente no **Render** ou **PythonAnywhere** em poucos minutos.

