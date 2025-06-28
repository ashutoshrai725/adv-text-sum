from flask import Flask, render_template, request
from summarizer import generate_summary
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['input_text']
    max_len = int(request.form.get('max_len', 130))
    min_len = int(request.form.get('min_len', 30))
    summary = generate_summary(input_text, max_len, min_len)
    return render_template('index.html', summary=summary, input_text=input_text, max_len=max_len, min_len=min_len)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
