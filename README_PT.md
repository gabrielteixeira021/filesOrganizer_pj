# Organizador de Arquivos

Uma aplicação Python simples que organiza automaticamente arquivos baixados por tipo em pastas apropriadas.

## O que faz

- Monitora arquivos baixados
- Classifica arquivos por extensão (ex: .mp4 → pasta Vídeos)
- Move arquivos para pastas organizadas automaticamente

## Como usar

Execute a aplicação:

```bash
python src/main.py
```

## Estrutura do Projeto

```
organizador_arquivos/          # Pasta raiz do projeto
│
├── src/                       # Código fonte principal
│   ├── __init__.py           # Para tornar src um pacote Python
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── core/                 # Módulos centrais do sistema
│   │   ├── __init__.py
│   │   ├── file_monitor.py   # Monitoramento de arquivos
│   │   ├── file_classifier.py # Classificação de arquivos
│   │   └── file_mover.py     # Movimentação de arquivos
│   ├── utils/                # Utilitários e helpers
│   │   ├── __init__.py
│   │   ├── config_manager.py # Gerenciamento de configurações
│   │   ├── logger.py         # Sistema de logging
│   │   └── helpers.py        # Funções auxiliares
│   └── gui/                  # Interface gráfica
│       ├── __init__.py
│       ├── main_window.py    # Janela principal
│       ├── settings_dialog.py # Diálogo de configurações
│       └── components/       # Componentes de UI reutilizáveis
│           ├── __init__.py
│           ├── file_list.py  # Lista de arquivos
│           └── log_viewer.py # Visualizador de logs
│
├── tests/                    # Testes automatizados
│   ├── __init__.py
│   ├── test_core/           # Testes dos módulos centrais
│   │   ├── __init__.py
│   │   ├── test_file_monitor.py
│   │   ├── test_file_classifier.py
│   │   └── test_file_mover.py
│   ├── test_utils/          # Testes dos utilitários
│   │   ├── __init__.py
│   │   ├── test_config_manager.py
│   │   └── test_logger.py
│   └── test_gui/            # Testes da interface
│       ├── __init__.py
│       └── test_main_window.py
│
├── docs/                    # Documentação do projeto
│   ├── index.md            # Página principal da documentação
│   ├── vision.md           # Documento de visão
│   ├── requirements.md     # Requisitos do sistema
│   ├── setup.md           # Guia de instalação
│   ├── usage.md           # Guia de uso
│   └── images/            # Imagens para documentação
│       └── architecture.png
│
├── data/                   # Dados do aplicativo
│   ├── config/             # Configurações
│   │   └── settings.json   # Arquivo de configurações
│   ├── categories/         # Definições de categorias
│   │   └── default_categories.json
│   └── logs/               # Logs da aplicação
│       └── app.log         # Arquivo de log
│
├── scripts/               # Scripts auxiliares
│   ├── install.py         # Script de instalação
│   ├── build.py           # Script de build (para futuro)
│   └── deploy.py          # Script de deploy (para futuro)
│
├── requirements.txt       # Dependências do projeto
├── README.md             # Documentação principal (inglês)
├── README_PT.md          # Documentação em português (este arquivo)
├── LICENSE               # Licença do projeto
└── .gitignore           # Arquivos a serem ignorados pelo Git
```

## Funcionalidades para Adicionar Depois

- [ ] Monitorar pasta Downloads automaticamente
- [ ] Categorias de tipos de arquivo configuráveis
- [ ] Interface gráfica
- [ ] Funcionalidade de desfazer
- [ ] Destinos de pasta personalizados
- [ ] Tratamento de arquivos duplicados
- [ ] Monitoramento de arquivos em tempo real
- [ ] Configuração através da interface gráfica
- [ ] Logging e histórico
- [ ] Monitoramento de múltiplos diretórios

## Instalação

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute a aplicação: `python src/main.py`

## Contribuindo

Este projeto segue uma abordagem de ambiente de desenvolvimento Python simples e minimalista, perfeita para contribuições amigáveis para iniciantes.

## Licença

[Adicione informações da sua licença aqui]
