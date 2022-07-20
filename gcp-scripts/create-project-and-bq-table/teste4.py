# É necessário criar uma SA com a role projectcreator no parent resource (pasta ou organização) do projeto.

from googleapiclient import discovery
from google.oauth2 import service_account
from google.cloud import bigquery # pip install google-cloud-bigquery
import requests


project_id = 'teste-proj-integration-2022-4'
dataset_name = 'teste_proj_integration_2022_2_dataset'
table_name = 'teste_proj_integration_2022_2_table'

credentials = service_account.Credentials.from_service_account_file('C:\\Users\\ianzd\\DevOps\\gcp-scripts\\test-intregation-bq-1a5f99ee365d.json')

# scoped_credentials = credentials.with_scopes(
#     ['https://cloudresourcemanager.googleapis.com/v1'])


service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
project_body = {
    'name': project_id,
    'projectId': project_id,
    'parent': {'type':'folder', 'id':'84591264540'}
}
request = service.projects().create(body=project_body)
request.execute()
print(request)



# HABILITAR A API DO BIGQUERY POR SCRIPT



client = bigquery.Client()

dataset_id = "{}.{}".format(project_id, dataset_name)
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"

dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.

