## Domain-info

Contém um script que dado um domínio via argumento na linha de comando, obtém as informações deste determinado domínio usando o https://www.whois.com.

---

### Preparando o ambiente

É necessário no mínimo o python `3.8` para rodar o script, então certifique-se de que sua versão atende esse requisito.

Verifique sua versão através do comando:

```shell
$ python --version
```

Com o ambiente preparado, é recomendado que se crie um novo ambiente virtual para a instalação das dependências e execução do código.

Para isso, basta executar esses comandos:

1. Criar um novo ambiente virtual:
    ```shell
    $ python -m venv venv
    ```

1. Ativar o novo ambiente virtual:
    ```shell
    $ source venv/bin/activate
    ```

1. Realizar o download das dependências
    ```shell
    $ python -m pip install -r requirements.txt
    ```

---

### Execução do código

Para executar o código, basta executar o script `whois.py` informando o domínio como um argumento na linha de comando, dessa forma: `python whois <domínio>`

Exemplo com o domínio `google.com.br`:

```shell
$ python whois google.com.br
```