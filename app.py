from flask import Flask, render_template, request
from helper import get_questions, get_info_from_csv, get_links_from_service

app = Flask(__name__)

@app.route("/")
def form():
    questions = get_questions("questions.txt")
    return render_template("form.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    answers = ""
    req = request.form.get("0", False)
    print(request.form)
    resources_dict = get_info_from_csv("resources.csv")
    links = get_links_from_service(resources_dict, req)
    return render_template("result.html", links=list(links))


def main():
    app.run(debug=True)

if __name__=="__main__":
    main()



answers_to_links = {
    [1 ,2, 3] : "SNAP"
}