# Importa os pacotes necessários para executar o programa. Urllib é um módulo para trabalhar com URLs (abrir, ler, etc)
# O BeuatifulSoup é uma biblioteca para realizar queries em HTML.
# Da biblioteca do Google Cloud, importamos o módulo do BigQuery para ingerir os dados do scrapping
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from google.cloud import bigquery



# Construir o cliente do BQ e atribuir a variável com o path da table que será utilizada
client = bigquery.Client()
table_id = "active-cosine-317912.webscrapperlinks.webscrapperlinks-tables"



# Input do script. Links que serão utilizados para fazer o scrapping.
linksInput = """https://canaltech.com.br/negocios/google-cloud-oferece-creditos-por-2-anos-em-programa-de-apoio-a-startups-208469/
https://www1.folha.uol.com.br/tec/2021/10/intel-e-google-cloud-se-unem-para-desenvolver-chip-para-data-centers.shtml"""



# Faz o split dos links do input transformando-os em uma Lista.
url = linksInput.split('\n')


# Faz um loop nos itens da lista de links
for lines in url:

    html = urllib.request.urlopen(lines).read()       # Abre cada um dos URLs da lista e faz a leitura em bloco
    soup = BeautifulSoup(html, 'html.parser')       # "Inicia" a instância do BeautifulSoup e referência a URL (html) que será lida

    for link in soup.find_all('a'):                 # Busca por todas as tags <a> do HTML
        linkLines = str(link.get('href'))           # Para cada tag <a>, captura o href (link) de referência
        if linkLines.startswith('http'):            # Se o link começar com HTTP (for válido)

            rows_to_insert = [
                {u"link_fonte": lines, u"link_scrapper": linkLines},      # Prepara o JSON para inserir os links da fonte e do scrapping na tabela do BQ
            ]

            errors = client.insert_rows_json(table_id, rows_to_insert)  # Faz uma chamada de API para inserir o JSON na table, já atribuindo erros a uma variável

            if errors == []:                           # Faz uma verificação de erros e printa se deu tudo certo ou não
                print("New rows have been added.")
            else:
                print("Encountered errors while inserting rows: {}".format(errors))