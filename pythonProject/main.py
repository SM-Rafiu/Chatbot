import flask
import google.generativeai as gen_ai









# frotnend
app = flask.Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    # Here you'll call your Python chatbot function with user_input
    # Replace 'your_chatbot_function' with your actual function
    bot_response = chatbot1(user_input)

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)


