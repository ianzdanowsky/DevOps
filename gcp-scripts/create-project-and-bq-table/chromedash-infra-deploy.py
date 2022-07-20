from googleapiclient import discovery
from oauth2client.client import OAuth2Credentials as creds
from google.cloud import bigquery
import requests



def create_project_bq(request):

    project_name = request.args.get('project')
    dataset_name = request.args.get('dataset')
    table_name = request.args.get('table')


    crm = discovery.build(
        'cloudresourcemanager', 'v3', http=creds.authorize(httplib2.Http()))

    operation = crm.projects().create(
    body={
        'project_id': flags.projectId,
        'name': project_name
    }).execute()

    project_ID = operation['project_id']


    #####################################

    client = bigquery.Client()

    dataset_id = "{}.{}.{}".format(client, project_ID, dataset_name)

    dataset = bigquery.Dataset(dataset_id)

    dataset.location = "US"

    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
   
    #print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

    #####################################

    table_id = "{}.{}".format(dataset_id, table_name)

    schema = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )    


