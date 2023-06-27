from flask import Flask
from translation import translation_blueprint
from translation_ngabe import translation_ngabe_blueprint

app = Flask(__name__)

app.register_blueprint(translation_blueprint)
app.register_blueprint(translation_ngabe_blueprint)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
