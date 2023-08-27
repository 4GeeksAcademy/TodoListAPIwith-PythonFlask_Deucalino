from flask import Flask,jsonify,request
app=Flask(__name__)
todos = [
    { "label": "Don´t kiss Jenni Hermmosillo in the mouth when Spain wins the Feminine football Worldcup", "done": False },
    { "label": "Don´t believe the hype..do..don´t..don´t...", "done": True }
    ]
@app.route('/todos', methods=['GET'])
def hello_world():
   return jsonify(todos)
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print(request_body)
    todos.append(request_body)
    return jsonify(todos)
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.remove(todos[position])
    print("This is the position to delete: ",position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)