from flask import Flask, render_template, request, flash ,redirect

app = Flask(__name__)
app.secret_key = 'super_secret_key'  
# Home route
@app.route("/")
def home():
    return render_template("home.html")

# About route
@app.route("/about")
def about():
    return render_template("about.html")

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save to file
        with open("messages.txt", "a") as f:
            f.write(f"{name} ({email}): {message}\n")

        flash('🚀 Message sent and saved! I’ll get back to you soon.')
        return redirect('/contact')

    return render_template('contact.html')

# Projects route (placeholder for now)
@app.route("/projects")
def projects():
    return "<h1>Projects coming soon... stay tuned 🚧</h1>"

if __name__ == "__main__":
    app.run(debug=True)
