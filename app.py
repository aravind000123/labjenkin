from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def register():
    return render_template("register_form_devops.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  # Allow external access in Docker
