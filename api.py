from flask import Flask, json, request

api = Flask(__name__)

@api.route('/sum', methods=['GET'])
def birthday():
    vms=request.args.get('birthday')
    return json.dumps(list(vms))
    
@api.route('/about', methods=['GET'])
def hi():
    return "This is simple api, copyright @lehuyhuan @V_1.0.0"

@api.route('/', methods=['GET'])
def index():
    return "This is simple api, copyright @lehuyhuan @V_1.0.0"

if __name__ == '__main__':
    api.run(host='0.0.0.0',port=5000)
