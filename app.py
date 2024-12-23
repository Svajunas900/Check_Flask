from flask import Flask, render_template, request, redirect, url_for
import json
from functions.fibonacci import fibonacci
from forms.forms import SimpleRouteForm, OddRouteForm
import os
from dotenv import load_dotenv

app = Flask(__name__)


# Parsing .env file and loading variable as environment variables
load_dotenv()


app.secret_key = os.environ.get("SECRETKEY")


# Route for handling form submition and redirecting to coresponding route
@app.route("/", methods=["GET", "POST"])
def home() -> None:
    simple_form = SimpleRouteForm()
    odd_form = OddRouteForm()
    if request.method == "POST":
        if "simple_submit" in request.form:
            simple_user_number = simple_form.user_input.data
            return redirect(url_for("simple", number=simple_user_number))
        elif "odd_submit" in request.form:
            odd_user_number = odd_form.user_input.data
            return redirect(url_for("odd", number=odd_user_number))

    data = {"simple": simple_form, "odd": odd_form}
    return render_template("index.html", data=data)


# Based on user input calculate fibonacci number and return it as json object
@app.get("/simple/<int:number>")
def get_fibonacci_number(number: int) -> None:
    fibonacci_number = fibonacci(number)
    json_obj = {"User number": number,
                "Fibonacci number": fibonacci_number}
    return json.dumps(json_obj)


# Based on user input calculate fibonacci number and return only a string which describes if a number is odd or not
@app.get("/odd/<int:number>")
def is_odd(number: int) -> None:
    fibonacci_number = fibonacci(number)
    odd = ""
    if fibonacci_number % 2 == 0:
        odd = "Not in the sequence"
    else:
        odd = "In the sequence"
    json_obj = {"User number": number,
                "Result": odd}
    return json.dumps(json_obj)


if __name__ == "__main__":
    app.run(debug=True)
