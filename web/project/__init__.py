from flask import Flask
app = Flask(__name__)
model_file_path = os.join(os.path.realpath(__file__), "outputs")
print('loading the output model from the file {}'.format(model_file_path))
loaded_entity_extractor = DictionaryBasedEntityExtractor.load(model_file_path)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame.from_dict(data, orient='columns')
    loaded_entity_extractor.transform(df)
    df.head()
    return jsonify(df)
    