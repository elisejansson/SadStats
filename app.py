from flask import Flask
from flask import render_template #to combine data with html
app = Flask(__name__)

@app.route("/pivottable")
def pivottable():
    template = 'pivottable.html'
    return render_template(template)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
