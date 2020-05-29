from chalice import Chalice

app = Chalice(app_name='mytodo')


@app.route('/')
def index():
    return {'hello': 'world'}

#Gets a list of all Todo's
@app.route('/todos', methods=['GET'])
def get_list():
    return {'hello': 'world'}

#Create a new Todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = app.current_request.json_body
    return get_app_db().add_item(
        description=body['description'],
        metadata=body.get('metadata')
    )

#Gets a specific Todo
@app.route('/todos/{id}', methods=['GET'])
def get_todo():
    return {'hello': 'world'}

#Deletes a specific Todo
@app.route('/todos/{id}', methods=['DELETE'])
def del_todo():
    return {'hello': 'world'}

#Updates the state of a Todo
@app.route('/todos/{id}', methods=['PUT'])
def update_tod():
    return {'hello': 'world'}