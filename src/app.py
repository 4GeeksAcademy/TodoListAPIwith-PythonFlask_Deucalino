from flask import Flask, jsonify
todos = [
    { "label": "Don´t kiss Jenni Hermmosillo in the mouth when Spain wins the Feminine football Worldcup", "done": False },
    { "label": "Don´t believe the hype..do..don´t..don´t...", "done": True }
    ]

app = Flask(__name__)
@app.route('/todos', methods=['GET'])
def hello():
  json_text=jsonify(todos)
  return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)