# Projeto de Coleta de Informações de atividades proximas do Kroton (anhanguera)

Este projeto visa automatizar a coleta de informações sobre atividades e datas de vencimento em uma plataforma de aula utilizando Python e Selenium.

## Pré-requisitos

- Python 3.x instalado
- Selenium WebDriver para Python instalado (`pip install selenium`)
- Chrome WebDriver baixado e configurado (ou outro WebDriver de sua preferência)

## Instalação e Configuração

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Baixe o Chrome WebDriver (ou WebDriver correspondente ao seu navegador) e adicione-o ao PATH do sistema.

3. Edite o arquivo `coleta_informacoes.py`:

   - Substitua `"seu login"` e `"sua senha"` pelas suas credenciais de acesso à plataforma.

## Utilização

Execute o script `coleta_informacoes.py` para iniciar a coleta de informações:

```bash
python coleta_informacoes.py
```

## Funcionamento do Código

1. Abre uma janela do navegador Chrome.
2. Acessa a página de login da plataforma.
3. Insere as credenciais de login.
4. Navega até a seção de estudos.
5. Coleta informações sobre atividades e datas de vencimento.
6. Imprime os resultados na tela.
7. Encerra a execução.

## Notas

- lembre de alterar o login e senha da plataforma
