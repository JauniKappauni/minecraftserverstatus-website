from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def function1():
    output = ""
    if request.method == "POST":
        javaserver = request.form.get("javaserver")
        bedrockserver = request.form.get("bedrockserver")
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)