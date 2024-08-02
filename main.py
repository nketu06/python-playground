from google.cloud import storage
import labelbox as lb
import json
import os

# ---------------------------------****************-------------------
# Set up GCP credentials and initialize the storage client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nishantketu/Downloads/mykey.json"
storage_client = storage.Client()

# Define the GCS bucket name and the prefix for your JSON files
bucket_name = 'nketu-output-bucket'
directory ='json_files/'

# labelbox and its dataset initialize and configuration
LB_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbHpjZTliZGgwMDQ3MDcwcjN0emJnenBpIiwib3JnYW5pemF0aW9uSWQiOiJjbHpjZTliZGIwMDQ2MDcwcmI4bWMzNjJyIiwiYXBpS2V5SWQiOiJjbHpja3R5NzUwMW05MDd5eWZvcWM3bXRzIiwic2VjcmV0IjoiZDQzNjdmZWI3NDFmOTIyY2UwOWRjY2QxNzEwMWNiYTciLCJpYXQiOjE3MjI1OTU0MTEsImV4cCI6MjM1Mzc0NzQxMX0.puhjPnM00nbfkYVBZe6YVZSKz9DEZE1dt8tUJkixh20'
lb_client = lb.Client(api_key=LB_API_KEY)
dataset_name="dataset_006"



def create_or_get_dataset(client, dataset_name):
    """Create a new dataset or get the existing one."""
    for dataset in client.get_datasets():
        if dataset.name == dataset_name:
            return dataset
    return client.create_dataset(name=dataset_name)

def get_json_files_from_gcs(bucket_name, prefix):
    """Retrieve JSON files from the GCS bucket."""
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)
    return [blob.name for blob in blobs if blob.name.endswith('.json')]


def upload_to_labelbox(data):
    """Upload JSON data to a Labelbox dataset."""
    task = dataset.create_data_rows(data)
    task.wait_till_done()
    print(task.errors)



# Initilize dataset for labelbox
dataset = create_or_get_dataset(lb_client, dataset_name)

# Retrieve JSON files from GCS and upload to Labelbox
json_files = get_json_files_from_gcs(bucket_name, directory)
print(json_files)

for file_name in json_files:
    blob = storage_client.bucket(bucket_name).blob(file_name)
    data = json.loads(blob.download_as_string().decode('utf-8'))
    # print(data,type(data))
    upload_to_labelbox(data)
    




