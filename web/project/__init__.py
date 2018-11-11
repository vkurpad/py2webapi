from flask import Flask
import os
from tatk.pipelines.entity_extraction.dictionary_based_entity_extractor import DictionaryBasedEntityExtractor
from pathlib import Path
from flask import request, jsonify
import pandas as pd

p = Path(__file__).resolve().parents[2]

app = Flask(__name__)
model_file_path = os.path.join(p, "outputs", "sebra_model.zip")
print('loading the output model from the file {}'.format(model_file_path))
loaded_entity_extractor = DictionaryBasedEntityExtractor.load(model_file_path)

@app.route('/')
def hello_world():
    return 'Hello World! - Prediction for Vinod'


@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    print(data["values"][0]["data"])
    for rec in data["values"]:
        df = pd.DataFrame({'col':rec["data"]["text"]})
        
        df.columns = ["description"]
        print (df)
        loaded_entity_extractor.transform(df)
        df.head()
    
    return jsonify(df.to_json())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    