import json
import asyncio
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import websockets

app = Flask(__name__)
CORS(app)

async def send_to_websocket(text):
    async with websockets.connect("ws://localhost:1865/ws") as websocket:
        print(f'Sending text to WebSocket: {text}')
        await websocket.send(json.dumps({'text': text}))
        response = json.loads(await websocket.recv())
        print(f'Received response from WebSocket: {response}')
        return response.get('content', 'No content found in response')

@app.route('/send_text', methods=['POST'])
def send_text():
    text = request.form.get('text')
    print(f'Received text from user: {text}')
    content = asyncio.run(send_to_websocket(text))
    print(f'Sending content to user: {content}')
    return jsonify({'content': content})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500, debug=True)
