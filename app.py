from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    article = data.get('text')

    summary = summarizer(article, max_length=1500, min_length=30, do_sample=False)[0]['summary_text']

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)

