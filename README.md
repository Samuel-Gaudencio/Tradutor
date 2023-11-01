# Tradutor de Texto para Fala

Este é um aplicativo de tradução de texto para fala desenvolvido em Python usando a biblioteca Tkinter e a API de tradução de texto da RapidAPI. O aplicativo permite que você insira um texto em português, traduza-o para inglês e reproduza o texto traduzido como fala.

## Requisitos

- Python 3.x
- Biblioteca Tkinter
- Biblioteca requests
- Biblioteca playsound
- Biblioteca gTTS (Google Text-to-Speech)
- Conta na RapidAPI para obter uma chave de API para o serviço de tradução de texto

## Configuração da Chave da API

Antes de executar o aplicativo, obtenha uma chave de API da RapidAPI para o serviço de tradução de texto. Substitua a variável `key` no código pelo seu próprio valor de chave.

## Como Usar

1. **Executar o Aplicativo**:
   - Execute o script Python em um ambiente que tenha acesso à internet e a uma chave de API válida.

2. **Inserir Texto**:
   - Digite o texto em português que você deseja traduzir na caixa de entrada.

3. **Clique em "Traduzir"**:
   - Clique no botão "Traduzir" para traduzir o texto para inglês. O texto traduzido será exibido na tela.

4. **Reproduzir Texto Traduzido**:
   - Clique no botão de volume para reproduzir o texto traduzido como fala.

5. **Resetar**:
   - Clique no botão "Resetar" para limpar o campo de entrada e os arquivos temporários de áudio.

## Interface Gráfica

O aplicativo possui uma interface gráfica simples com um campo de entrada para inserir o texto, um botão para traduzir, um botão para reproduzir a fala e um botão para resetar.

---

**Nota**: Certifique-se de ter uma conexão à internet ativa ao executar o aplicativo para acessar o serviço de tradução de texto. Certifique-se também de que a chave de API da RapidAPI esteja configurada corretamente no código para obter os dados da tradução de texto.

Para mais detalhes sobre a biblioteca Tkinter, consulte a [documentação oficial](https://docs.python.org/3/library/tk.html). Para obter informações sobre a API de tradução de texto da RapidAPI, consulte [Text Translator](https://rapidapi.com/text-translator/text-translator-api).

