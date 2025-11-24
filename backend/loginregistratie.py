from flask import Flask, render_template, request, redirect, url_for

# Flask app met juiste paden naar frontend
app = Flask(
    __name__,
    template_folder="../frontend/templates",  # locatie van HTML-bestanden
    static_folder="../frontend/static"       # locatie van CSS/JS
)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Login route voorbeeld
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Hier kun je backend logica toevoegen
        return f"Welkom, {username}!"
    return render_template("login.html")

# Registratie route voorbeeld
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Hier kun je backend logica toevoegen
        return redirect(url_for("home"))
    return render_template("register.html")

# Start de server in debug mode
if __name__ == "__main__":
    app.run(debug=True)
