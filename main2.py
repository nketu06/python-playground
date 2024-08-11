import labelbox
import json

# Initialize Labelbox client
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbHpjZTliZGgwMDQ3MDcwcjN0emJnenBpIiwib3JnYW5pemF0aW9uSWQiOiJjbHpjZTliZGIwMDQ2MDcwcmI4bWMzNjJyIiwiYXBpS2V5SWQiOiJjbHpja3R5NzUwMW05MDd5eWZvcWM3bXRzIiwic2VjcmV0IjoiZDQzNjdmZWI3NDFmOTIyY2UwOWRjY2QxNzEwMWNiYTciLCJpYXQiOjE3MjI1OTU0MTEsImV4cCI6MjM1Mzc0NzQxMX0.puhjPnM00nbfkYVBZe6YVZSKz9DEZE1dt8tUJkixh20'
client = labelbox.Client(api_key=API_KEY)


# Create a new dataset
dataset = client.create_dataset(name="Mail Data Dataset")

# Prepare your data
data = [
    {
        "row_data": "gs://nketu-output-bucket/base.html",
        "global_key": "example-html-0002",
        "metadata_fields": [
            {
                "schema_id": "cko8s9r5v0002h2dk9elqdidi",
                "value": "my tag"
            },
            {
                "schema_id": "cko8s9r5v0003h2dk9elqdidj",
                "value": "nketu@gmail"
            },
            {
                "schema_id": "cko8s9r5v0004h2dk9elqdidk",
                "value": ["first", "second"]
            },
            {
                "schema_id": "cko8s9r5v0005h2dk9elqdidl",
                "value": {
                    "first": True,
                    "isdraft": False
                }
            },
            {
                "schema_id": "cko8s9r5v0006h2dk9elqdidm",
                "value": [
                    {
                        "c1": True,
                        "c2": None
                    }
                ]
            }
        ]
    }
]

# Convert the data to JSON
data_json = json.dumps(data)

# Upload the data rows to the dataset
upload_task = dataset.create_data_rows(data)

# Monitor the task to completion
upload_task.wait_till_done()

print(f"Data upload task status: {upload_task.status}")

# Create a project and link it to the dataset
project = client.create_project(name="Mail Data Project")
project.datasets.connect(dataset)

# Define the ontology (this step will vary based on your specific schema)
ontology = {
    "tools": [
        {
            "tool": "bbox",
            "name": "Label",
            "color": "red"
        }
    ],
    "classifications": [
        {
            "type": "text",
            "name": "tag",
            "schema_id": "cko8s9r5v0002h2dk9elqdidi"
        },
        {
            "type": "text",
            "name": "email",
            "schema_id": "cko8s9r5v0003h2dk9elqdidj"
        },
        {
            "type": "checkbox",
            "name": "header",
            "schema_id": "cko8s9r5v0004h2dk9elqdidk"
        },
        {
            "type": "checkbox",
            "name": "flags",
            "schema_id": "cko8s9r5v0005h2dk9elqdidl"
        },
        {
            "type": "checkbox",
            "name": "checking",
            "schema_id": "cko8s9r5v0006h2dk9elqdidm"
        }
    ]
}

project.setup_editor(ontology=ontology)

print(f"Project {project.name} is ready for annotations.")

