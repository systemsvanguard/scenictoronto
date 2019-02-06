# starthere.py ~ start of our food checklist deiderata app
from flask import Flask, render_template 

app = Flask(__name__, static_url_path='/static')



# -------------------------->
# app routing
@app.route('/')
def home():
    return render_template('index.html')
    # return render_template('tpl.home.html')
    # return "Welcome to Scenic Toronto!"

@app.route('/tours/')
def tours():
    return render_template('tours.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/contact/')    
def contact():
    return render_template('contact.html')
	# ----->


@app.route('/cntower/')
def cntower():
    return render_template('sights_cntower.html')

@app.route('/highpark/')
def highpark():
    return render_template('sights_highpark.html')

@app.route('/cityhall/')
def cityhall():
    return render_template('sights_cityhall.html')

@app.route('/torontoislands/')
def torontoislands():
    return render_template('sights_torontoislands.html')
@app.route('/casaloma/')
def casaloma():
    return render_template('sights_casaloma.html')

@app.route('/rogerscentre/')
def rogerscentre():
    return render_template('sights_rogerscentre.html')

@app.route('/ago/')
def ago():
    return render_template('sights_ago.html')

@app.route('/rom/')
def rom():
    return render_template('sights_rom.html')	
# -------------------------->    



if __name__ == '__main__':
    app.run(debug=True)
    # remember to set debug above to False in production!! 

