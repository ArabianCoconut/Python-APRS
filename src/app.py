from flask import Flask, render_template, request
from aprspass import aprspass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the index.html template and generates an APRS passcode if a POST request is received.

    Returns:
        If a POST request is received, returns the rendered index.html template with the generated APRS passcode.
        Otherwise, returns the rendered index.html template without a passcode.
    """
    if request.method == 'POST':
        call=request.form.get('call_sign')
        passcode = aprspass(call)
        return render_template('index.html', passcode=passcode)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
