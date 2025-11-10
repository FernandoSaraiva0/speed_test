# 🚀 Speed Test
Um utilitário interativo de teste de velocidade de internet, desenvolvido em Python usando speedtest-cli.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Características

- 🎯 **Seleção automática de servidor** com barra de progresso em tempo real
- 📊 **Métricas detalhadas** de download, upload e ping
- 🎨 **Interface interativa** com indicadores visuais usando tqdm
- 📍 **Informações completas** do servidor (ISP, localização, país)
- ⚡ **Conversão automática** de bytes para Mbps
- 🔄 **Threading** para não bloquear a interface durante os testes

## 📋 Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/FernandoSaraiva0/speed_test.git
cd speed_test
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como usar

Execute o script principal:
```bash
python speed_test.py
```

O programa irá:
1. 🔍 Selecionar automaticamente o melhor servidor
2. ⬇️ Medir a velocidade de download
3. ⬆️ Medir a velocidade de upload
4. 📡 Capturar o ping da rede
5. 📊 Exibir um relatório completo com todas as métricas

## 📊 Exemplo de saída
```
Selecionando o melhor servidor...
100%|████████████████████████████████| 00:03
Melhor servidor selecionado: Vivo em São Paulo, BR

Captando velocidade de Download...
100%|████████████████████████████████| 00:05

Captando velocidade de Upload...
100%|████████████████████████████████| 00:07

Captando ping da rede...
100%|████████████████████████████████| 00:00

Ping: 12.45 ms
Velocidade de Download: 150.32 Mbps
Velocidade de Upload: 75.18 Mbps
```

## 🛠️ Estrutura do projeto
```
speed_test/
│
├── speed_test.py          # Script principal
├── requirements.txt       # Dependências do projeto
├── README.md             # Este arquivo
└── LICENSE               # Licença do projeto (opcional)
```

## 📦 Dependências

- **speedtest-cli**: Biblioteca para realizar testes de velocidade
- **tqdm**: Biblioteca para criar barras de progresso elegantes

## 🔍 Funcionalidades Técnicas

### Conversão de Velocidade
O script inclui uma função personalizada `bytes_to_mb()` que converte automaticamente os valores de bytes retornados pela API para Mbps (Megabits por segundo), facilitando a leitura dos resultados.

### Threading
Todas as operações de teste são executadas em threads separadas para manter a interface responsiva e permitir que as barras de progresso sejam atualizadas em tempo real.

### Seleção Inteligente de Servidor
O programa seleciona automaticamente o melhor servidor baseado em:
- Proximidade geográfica
- Latência
- Disponibilidade

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 🐛 Problemas conhecidos

Se você encontrar o erro `ModuleNotFoundError`, certifique-se de ter instalado todas as dependências:
```bash
pip install -r requirements.txt
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Fernando Saraiva**

- GitHub: [@FernandoSaraiva0](https://github.com/FernandoSaraiva0)
- Especialista em Network e Telecom Engineering

## 🙏 Agradecimentos

- [speedtest-cli](https://github.com/sivel/speedtest-cli) - Biblioteca principal utilizada para os testes
- [tqdm](https://github.com/tqdm/tqdm) - Biblioteca para barras de progresso
- Comunidade Python pela documentação e suporte

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões:
- Abra uma [issue](https://github.com/FernandoSaraiva0/speed_test/issues)
- Entre em contato através do GitHub

## 💡 Dicas de uso

### Teste rápido
```bash
python speed_test.py
```

### Executar múltiplas vezes
```bash
for i in {1..5}; do python speed_test.py; sleep 60; done
```

### Salvar resultado em arquivo
```bash
python speed_test.py > resultado_$(date +%Y%m%d_%H%M%S).txt
```

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!

**Desenvolvido com ❤️ usando Python**
