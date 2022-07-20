# To deploy as a function (Cloud Functions):

# Requirements: google-cloud-resource-manager
# Service Account selected in Cloud Function should have Folder Admin and Owner Roles at Folder level.
# Enable Cloud Resource Manager API
# After deployed, you can call through Cloud SDK - 'gcloud functions call function_name'

from google.cloud import resourcemanager_v3

def sample_list_projects(request):
    # Create a client
    client = resourcemanager_v3.ProjectsClient()

    # Initialize request argument(s)
    request = resourcemanager_v3.ListProjectsRequest(
        parent="folders/158477777255",
    )

    # Make the request
    page_result = client.list_projects(request=request)

    # Handle the response
    for response in page_result:
        if response.project_id != "cool-encoder-356312":
            delRequest = resourcemanager_v3.DeleteProjectRequest(name=response.name)
            delOperation = client.delete_project(request=delRequest)

            print("Deletando o projeto, aguarde...")

            delResponse = delOperation.result()

            print(delResponse)
    
    return "Todos os projetos foram deletados."