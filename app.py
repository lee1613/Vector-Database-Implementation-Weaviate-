from flask import Flask, request, jsonify, render_template
import weaviate
import pandas as pd
from weaviate.classes.query import MetadataQuery
import os

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ingest', methods=['POST','GET'])
def Ingestion_Endpoint():
    if request.method == "POST":
        sentence = request.form["st"] 
        client = weaviate.connect_to_local(
                headers={
                "X-HuggingFace-Api-Key" : "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" #os.getenv("huggingface_api_key")
                }
                )
        if client.is_ready():
            sqx = client.collections.get("SquareX")
            sqx.data.insert(properties={"text" : sentence})
        else:
            return jsonify({"error": "Cannot connect to vector DB"})
        return "<h1>Data Ingested</h1>"
    else:
        return render_template("ingest.html")


@app.route('/query', methods=['POST','GET'])
def Query_Endpoint():
    if request.method == "POST":
        sentence = request.form["st"] 
        k = int(request.form["k"])
        client = weaviate.connect_to_local(
                headers={
                "X-HuggingFace-Api-Key" : "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" #os.getenv("huggingface_api_key")
                }
                )
        if client.is_ready():
            sqx = client.collections.get("SquareX")
            response = sqx.query.near_text(query=sentence
                                , limit = k,
                                return_metadata=MetadataQuery(distance=True),
                                )
            print(response)
            result = pd.DataFrame({o.properties['text']: [o.metadata.distance] for o in response.objects}, index = ["Distance Metric"]).transpose()
            return render_template("result.html", html = result.to_html())
        else:
            return jsonify({"error": "Cannot connect to vector DB"})
    else:
        return render_template("query.html")

if __name__ == '__main__':
    app.run(debug=True)


