



from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cadastros = []
@app.route('/', methods=['GET', 'POST'])
def principal():
    if request.method == 'POST':
        if request.form.get("nome") and request.form.get("idade") and request.form.get("email"):
            cadastros.append({
                "nome": request.form.get("nome"),
                "idade": int(request.form.get("idade")), 
                "email": request.form.get("email")
                })
        return redirect(url_for('principal'))
    return render_template('index.html', cadastros=cadastros)

if __name__ == '__main__':
    app.run(debug=True)