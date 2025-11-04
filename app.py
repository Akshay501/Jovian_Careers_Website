from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Jovian Careers</title>
        </head>
        <body>
            <h1>Welcome to Jovian Careers</h1>
            <p>This is a career website for Jovian.</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
