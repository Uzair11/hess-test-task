# SearchSmartly PoI Data Ingestion Service
# Design Overview

The SearchSmartly PoI Data Ingestion Service employs a modular and extensible design to efficiently process and import Point of Interest (PoI) data from various sources into our database. This section provides an overview of the design and architectural choices made to address the data ingestion challenge.

# File Readers: 
The application utilizes specialized file readers for each supported data format (CSV, JSON, XML), encapsulated within the ingest_utils/readers directory. These readers are responsible for parsing files, extracting relevant PoI data, and standardizing the output into a uniform format for database ingestion.
# Data Ingestor: 
A central DataIngestor class orchestrates the ingestion process. It interfaces with the file readers to receive processed data and inserts it into the database using Django's ORM. This approach decouples data reading from data storage, enhancing maintainability and scalability.
# Factory Pattern: 
To dynamically select the appropriate file reader based on the input file type, the application employs the Factory Method design pattern. This is implemented in ingest_utils/factories.py, which instantiates and returns the correct file reader object.
# Ingestion Strategy
# Command-Line Interface (CLI): 
The ingestion process is initiated through a Django management command (ingestdata), allowing for flexible, scriptable data imports directly from the command line.
# Batch Processing: 
To optimize performance, especially with large datasets, the application employs batch processing techniques. This minimizes the number of database transactions, significantly reducing ingestion time and resource consumption.
# Error Handling: 
Robust error handling mechanisms are integrated throughout the ingestion pipeline. This ensures the process is resilient, with detailed logging to aid in diagnosing and resolving issues.
# Extensibility: 
The design allows for easy addition of new file formats and data sources. Adding support for another file type involves creating a new reader class and registering it with the factory.



# Building and running your application


Place your data files (e.g., data.csv, data.json, data.xml) in a known directory within the Docker container, such as /app/.
In the Dockerfile I have added the migrate command to run the ingestiondata
When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)