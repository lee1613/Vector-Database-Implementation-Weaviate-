<h1> Proof of Concept for Self-hosted Vector Database (Weaviate) </h1>

## Prerequisite:
- Python libraries: flask, pandas
- Install Weaviate Client in the environment, refer to this [link](https://weaviate.io/developers/academy/py/starter_custom_vectors/setup_weaviate/client) for detail instruction
- Possess at least a Hugging Face account with valid API Key. Create one [here](https://huggingface.co/) if you haven't had one.
- Docker Desktop 


## Setup
1. Set environment variables in your computer terminal with `huggingface_api_key='your hugging face api key'`

2. Clone the whole repository into your working environment

3. Open Docker Desktop

4. At the directory where the project located, run the docker with the command `docker compose up -d`

5. If applicable, use Jupyter notebook to run the [setup.ipynb](setup.ipynb) to ensure the flow of setup process. Alternatively, copy all the code into a python file to run all at once

## Interact with the Vector Database
1. Run the python file [app.py](app.py)

2. Open up the local host on browser http://127.0.0.1:5000

3. You may choose to Ingest Data or Query data from the API

4. Ingest Data type involves any sentence that has to be stored in the database

5. Query is allowed to find top **k** results in the database that is closest to the query sentence