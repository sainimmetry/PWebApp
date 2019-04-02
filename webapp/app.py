from flask import Flask, render_template,redirect, url_for, request

from employee import Employee

employees = []

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def students_page():
    if request.method == "POST":
        new_employee_id = request.form.get("employee-id","")
        new_employee_name = request.form.get("name","")
        new_employee_last_name = request.form.get("last-name","")
        new_employee_designation = request.form.get("designation","")


        new_employee = Employee(name=new_employee_name,last_name=new_employee_last_name,designation=new_employee_designation, employee_id=new_employee_id)
        print(new_employee)
        employees.append(new_employee)

        return redirect(url_for("students_page"))

    return render_template("index.html", employees=employees)


if __name__ == "__main__":
    app.run(debug=True)

