from flask import Flask, render_template, request, redirect, url_for
import json
from functions.fibonacci import fibonacci
from forms.forms import SimpleRouteForm, OddRouteForm

app = Flask(__name__)

app.secret_key = "superSecretKey"

@app.route("/", methods=["GET", "POST"])
def home():
    simple_form = SimpleRouteForm()
    odd_form = OddRouteForm()

    if request.method == "POST":
        simple_user_number = simple_form.user_input.data
        return redirect(url_for("simple", number=simple_user_number))

    # odd_user_number = odd_form.user_input.data
    # return redirect(url_for("odd", number=odd_user_number))
    
    data = {"simple": simple_form, "odd": odd_form}
    return render_template("index.html", data=data)


@app.get("/simple/<int:number>")
def simple(number):
    fibonacci_number = fibonacci(number)
    json_obj = {"User number": number,
                "Fibonacci number": fibonacci_number}
    return json.dumps(json_obj)



@app.get("/odd/<int:number>")
def odd(number):
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


# 4. Route 'odd' should receive the user params with GET operation and return JSON object with the explanation
#    that the return number in the ODD sequence or not:
#    {"user number": 5,
#     "result": if odd - "in sequence", if not odd "not in sequence"}