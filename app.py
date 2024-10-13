from flask import Flask, request, render_template


app = Flask(__name__)

# Route for Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Service page
@app.route('/service')
def service():
    return render_template('service.html')

# Route for sous-pages
@app.route('/plus1')
def plus1():
    return render_template('plus1.html')

@app.route('/plus2')
def plus2():
    return render_template('plus2.html')

@app.route('/plus3')
def plus3():
    return render_template('plus3.html')

@app.route('/allservice')
def allservice():
    return render_template('allservice.html')

# Route for the "Why Us" page (if applicable)
@app.route('/why')
def why_us():
    return render_template('why.html')

#sous-page
@app.route('/plusplus')
def plusplus():
    return render_template('plusplus.html')

# Route for the contact page (if applicable)
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Add more routes as needed

if __name__ == "__main__":
    app.run(debug=True)

