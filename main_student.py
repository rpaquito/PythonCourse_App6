from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home_student.html")

@app.route("/api/v1/<word>")
def about(word):
    definition = word.upper()
    result_dict = {'word': word, 'definition': definition}
    return result_dict

if __name__ == "__main__":
    app.run(debug=True, port=5001)
