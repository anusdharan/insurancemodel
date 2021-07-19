from flask import Flask, request, render_template
import pickle as pk
import numpy as np

# Flask constructor
application = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@application.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        age = float(request.form.get("age"))
        # getting input with name = lname in HTML form
        bmi = float(request.form.get("bmi"))
        children = float(request.form.get("children"))
        sex = request.form.get("sex")
        smoker = request.form.get("smoker")
        region= request.form.get("region")
        filename = 'finalized_insurance_model.pk'
        loaded_model = pk.load(open(filename, 'rb'))
        if sex=="female":
            fe=0;
            ma=1;
        else:
            fe = 1;
            ma = 0;

        if smoker == "yes":
            ye=1
        else:
            ye=0

        if region== "northwest":
            northwest=1
            southeast=0
            southwest = 0
        elif region== "southeast":
            northwest=0
            southeast=1
            southwest=0
        elif region== "southwest":
            northwest=0
            southeast=0
            southwest=1
        else :
            northwest = 0
            southeast = 0
            southwest = 0

        predictionresult = loaded_model.predict([[age,bmi,children, fe,ye,northwest,southeast,southwest]])

        return "Insurance charge is " + str(np.round(predictionresult[0],decimals=2)) + "rupees"
    return render_template("index.html")
   
if __name__ == '__main__':
    application.run(debug=True)