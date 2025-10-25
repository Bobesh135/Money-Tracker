from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super-tajny-klic' 

# Heslo zůstává stejné
CORRECT_PASSWORD = "1234"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        if password == CORRECT_PASSWORD:
            # Po správném zadání hesla přesměrujeme na novou funkci 'dashboard'
            return redirect(url_for('dashboard'))
        else:
            error = "Nesprávné heslo, zkus to znovu."
            
    return render_template('index.html', error=error)

@app.route('/dashboard')
def dashboard():
    # Zde si připravíme fiktivní data pro zobrazení na stránce.
    # Později je nahradíme daty z databáze.
    transaction_data = {
        'owned': 29375,
        'landed': 4000,
        'owe': 1135
    }
    # Načteme nový HTML soubor a předáme mu data
    return render_template('dashboard.html', data=transaction_data)

if __name__ == '__main__':
    app.run(debug=True)