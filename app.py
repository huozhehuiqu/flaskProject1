from flask import Flask, jsonify, json, render_template, send_file, make_response, Response, Blueprint
from flask import request
from flask import session

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template("index.html", **{"name": "joke"})
    return "Hello world !"

@app.route("/methods", methods=["GET"])
def methods():
    return "Only allow GET request types"

@app.route("/params/url")
def params_url():
    print(request.args)
    print(request.args.get("name"))
    return ""

@app.route("/params/rest/", defaults={'id': '1'})
@app.route("/params/rest/<id>")
def params_rest(id):
    return jsonify({"id": id})

@app.route("/params/body", methods=['POST'])
def params_body():
    print(request.content_type)
    if request.content_type == 'application/json':
        print(json.loads(request.data))
    return ""

@app.route("/params/form", methods=['POST'])
def params_form():
    print(request.form)
    print(request.form['name'])
    return ""

@app.route("/params/file", methods=['POST'])
def params_file():
    file = request.files['file']
    # get file type
    print(file.content_type)
    # get file name
    print(file.filename)
    # save file by bytes
    with open(file.filename, 'wb') as f:
        f.write(file.stream.read())
    return ""

@app.route("/params/json", methods=['GET'])
def params_json():
    return jsonify({"name": "joke"})


@app.route("/download", methods=['GET'])
def download():
    return send_file("test.gif", as_attachment=True)

@app.route("/response", methods=['GET'])
def response_test():
    data = {
        "test": "123"
    }
    res = Response(data, status=500, headers={'Content-Type': 'application/json'})
    res.set_cookie("test_key", "test_value", max_age=20)
    return res;


@app.route("/delete/response", methods=['GET'])
def response_delete():
    data = {
        "test": "123"
    }
    res = Response(data, status=500, headers={'Content-Type': 'application/json'})
    res.delete_cookie("test_key")
    return "success"


v1_blueprint = Blueprint("v1", __name__, url_prefix="/api/v1")
@v1_blueprint.route("/", defaults={'id': '1'})
@v1_blueprint.route("/<id>")
def show_id(id):
    return jsonify({'id': id})


# register blueprint
app.register_blueprint(blueprint=v1_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)