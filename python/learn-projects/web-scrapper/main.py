import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from google.cloud import bigquery

# # Construct a BigQuery client object and store the table adress

client = bigquery.Client()
table_id = "active-cosine-317912.webscrapperlinks.webscrapperlinks-tables"


# url = str(input('Insira a URL manualmente')).split()

linksInput = """https://canaltech.com.br/negocios/google-cloud-oferece-creditos-por-2-anos-em-programa-de-apoio-a-startups-208469/
https://www1.folha.uol.com.br/tec/2021/10/intel-e-google-cloud-se-unem-para-desenvolver-chip-para-data-centers.shtml"""

url = linksInput.split('\n')

for lines in url:

    html = urllib.request.urlopen(lines).read()       # Read the html as a block, not looping through lines
    soup = BeautifulSoup(html, 'html.parser')       # BeautifulSoup knows about bytes and UTF-8. Adjust results to receive queries.

    for link in soup.find_all('a'):
        linkLines = str(link.get('href'))
        if linkLines.startswith('http'):
            # print(lines, linkLines)

            rows_to_insert = [
                {u"link_fonte": lines, u"link_scrapper": linkLines},
            ]

            errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.

            if errors == []:
                print("New rows have been added.")
            else:
                print("Encountered errors while inserting rows: {}".format(errors))