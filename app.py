from flask import Flask, request #, flash, render_template, request, url_for, redirect
import pandas as pd
app = Flask(__name__)

url = 'https://raw.githubusercontent.com/jtwang1027/contint/master/cleaned.csv'
data = pd.read_csv(url,index_col=0)


@app.route('/', methods=['GET', 'POST']) #get/post generates a request object
def search():
    #post: page generated after data is submitted;
    #you can use .form.get method to variables submitted
    #get: what u see when u access URL directly by typing
    if request.method=="POST":
        symp= request.form.get('symptom') #based on name=
        symp=symp.lower() #lower case
        diag= data.diagnose[data.symptom.str.contains(symp)].unique()

        if len(diag)==0: #no matches found
            return '<h1>Matches not found. Please try again. </h1>'
        else:
           # out= ','.join(diag)
            out= '<br/>'.join(diag)
            return '<h1>The possible diagnoses are:</h1> {}'.format( out)


    return '''<form method="POST">
                  Symptom: <input type="text" name="symptom"><br>
        
                  <input type="submit" value="Submit"><br>
              </form>'''



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
