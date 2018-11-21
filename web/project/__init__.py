from flask import Flask
import os
from tatk.pipelines.entity_extraction.dictionary_based_entity_extractor import DictionaryBasedEntityExtractor
from pathlib import Path
from flask import request, jsonify
import pandas as pd
import pickle
import nltk
nltk.download('punkt')


p = Path(__file__).resolve().parents[2]
p = "/usr/src/app"
app = Flask(__name__)
#model_file_path = os.path.join(p, "outputs", "sabre_model.pkl")
#print('loading the output model from the file {}'.format(model_file_path))
#loaded_entity_extractor = DictionaryBasedEntityExtractor.load(model_file_path)
model_file_path = os.path.join("/usr/src/app/", "outputs", "sabre_model.pkl")
pkl_model = open(model_file_path, 'rb')
loaded_entity_extractor = pickle.load(pkl_model)




@app.route('/')
def hello_world():
    return 'Hello World! - Prediction for Gunicorn!!!'


@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    #print(data["values"][0]["data"])
    output = {
        "values": []
    }
    for rec in data["values"]:
        str = rec["data"]["text"]
        valarr = str.split("\n")
        print(valarr)
        df = pd.DataFrame({'col':valarr})
        
        df.columns = ["description"]
        #print (df)
        loaded_entity_extractor.transform(df)
        print(df.head())
        record =  {
            "recordId": rec["recordId"],
            "data": {
                "text": df["label"].tolist()
            },
            "errors": [],
            "warnings": []
        }
        output["values"].append(record)
    #return jsonify(df.to_json())
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
