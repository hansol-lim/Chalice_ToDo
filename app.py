from chalice import Chalice

app = Chalice(app_name='mytodo')


@app.route('/')
def index():
    return {'hello': 'world'}

#Gets a list of all Todo's
@app.route('/todos', methods=['GET'])
def list():

#Create a new Todo
@app.route('/todos', methods=['POST'])
def list():

#Gets a specific Todo
@app.route('/todos/{id}', methods=['GET'])
def list():

#Deletes a specific Todo
@app.route('/todos/{id}', methods=['DELETE'])
def list():

#Updates the state of a Todo
@app.route('/todos/{id}', methods=['PUT'])
def list():