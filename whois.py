from lxml import html
import requests
import sys

def check_minimum_python_version():
    """
    Verifica a versão mínima do python
    """
    MIN_PYTHON = (3, 8)
    if sys.version_info < MIN_PYTHON:
        print("Expecting at least python 3.10")
        exit(1)

def check_command_line_args():
    """
    Verifica os argumentos da linha de comando
    """
    args = sys.argv
    expected_args = 2
    if len(args) != expected_args:
        print("You must pass 1 argument as a domain: python whois.py google.com")
        exit(1)

def get_domain_on_args():
    """
    Obtém o domínio via argumentos da linha de comando
    """
    domain_arg_index = 1
    domain = sys.argv[domain_arg_index]
    if domain == "":
        print("You must pass 1 argument as a domain: python whois.py google.com")
        exit(1)    

def get_whois_page(domain: str) -> str:
    """
    Obtém a página em HTML do whois dado o domínio recebido
    """
    url = f'https://www.whois.com/whois/{domain}'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("received a non 200 status code")
    html_content = html.fromstring(response.content)
    return html_content

def extract_data_from_html(html: str) -> str:
    """
    Extrai os dados do HTML usando XPaths
    """
    data_list = html.xpath('//pre[@class="df-raw"]/text()')
    return ' '.join(data_list)

def print_data(domain: str, data: str):
    """
    Imprime as informações formatando o texto
    """
    print(f"---------------------- {domain} ----------------------\n")
    formatted_data = data.replace("\\n","\n")
    print(formatted_data)

if __name__ ==  "__main__":
    check_minimum_python_version()
    check_command_line_args()
    domain = get_domain_on_args()    
    try:
        html_content = get_whois_page(domain)
        data = extract_data_from_html(html_content)
        print_data(domain, data)
    except Exception as e:
        print(f"Something wrong while processing whois consult to {domain}: {e}")
        exit(1)
