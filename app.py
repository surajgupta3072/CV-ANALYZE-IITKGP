from flask import Flask, render_template, jsonify, request
import config
import openai
import aiapi
import pdfplumber
import requests


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/api/refine-cv', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
      file = request.files['file']
      if file.filename.endswith('.pdf'):
          # Extract text content from the PDF
          with pdfplumber.open(file) as pdf:
              text_content = ""
              for page in pdf.pages:
                  text_content += page.extract_text()

          # Pass the extracted text to the GPT model
          answer = aiapi.generateChatResponse(text_content)
          res = {}
          res['answer'] = answer
          return jsonify(res), 200
      else:
          return "Invalid file format. Please upload a PDF file."
      

    return render_template('index.html', **locals())
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

    
