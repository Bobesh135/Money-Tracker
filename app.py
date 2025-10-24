from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Tento 'secret_key' je potřeba pro zobrazení zpráv (flash messages)
app.secret_key = 'super-tajny-klic' 

# Prozatím nastavíme heslo přímo v kódu.
# POZOR: Toto není bezpečné pro reálnou aplikaci!
CORRECT_PASSWORD = "1234"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # Získáme heslo, které uživatel zadal do formuláře
        password = request.form.get('password')
        
        if password == CORRECT_PASSWORD:
            # Pokud je heslo správné, přesměrujeme ho na hlavní stránku
            return redirect(url_for('dashboard'))
        else:
            # Pokud je heslo špatné, zobrazíme chybovou hlášku
            error = "Nesprávné heslo, zkus to znovu."
            
    return render_template('index.html', error=error)

@app.route('/dashboard')
def dashboard():
    # Toto je zatím jen dočasná hlavní stránka po přihlášení
    return "<h1>Vítej na hlavní stránce!</h1><p>Tady bude tvůj money tracker.</p>"

if __name__ == '__main__':
    app.run(debug=True)