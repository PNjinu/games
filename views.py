from application import app, render_template
from models import Question

@app.route("/")
def index():
    firstquestion = Question.query.first()
    return render_template("index.html", firstquestion=firstquestion.question)

