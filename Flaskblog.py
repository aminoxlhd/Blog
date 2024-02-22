from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'autor': 'Leonel Messi',
        'title': 'Win world Cup',
        'content': 'Fist Post Content',
        'date_posted': 'December 18, 2022'
    },
    {
        'autor': 'Alx amine',
        'title': 'Complet Alx SE',
        'content': 'Second Post Content',
        'date_posted': 'July 22, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
if __name__ == "__main__":
    app.run(debug=True)