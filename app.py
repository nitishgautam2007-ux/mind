from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    msg = request.form.get('Body')
    
    print("User message:", msg)

    reply = "Batcheet 🤖: Message received 👍"

    return f"<Response><Message>{reply}</Message></Response>"

if __name__ == '__main__':
    app.run(debug=True)
