from flask import *

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")


@app.route("/success/<float:marks>")
def success(marks):
    return render_template(
        "result.html",
        result="Success",
        marks=marks
    )


@app.route("/fail/<float:marks>")
def fail(marks):
    return render_template(
        "result.html",
        result="Fail",
        marks=marks
    )


@app.route("/submit", methods=["POST"])
def submit():

    science = float(request.form["science"])
    maths = float(request.form["maths"])
    physics = float(request.form["physics"])
    biology = float(request.form["biology"])

    total_score = (science + maths + physics + biology) / 4

    if total_score >= 50:
        return redirect(url_for("success", marks=total_score))
    else:
        return redirect(url_for("fail", marks=total_score))


if __name__ == "__main__":
    app.run(debug=True)