from flask import Flask, redirect, render_template, request,url_for
from aprspass import aprspass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        call=request.form.get('call_sign')
        passcode = aprspass(call)
        return render_template('result.html', call=call, passcode=passcode)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
