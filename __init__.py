from cryptography.fernet import Fernet
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/encrypt/<string:key>/<string:valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # Charger la clé fournie
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}", 400

@app.route('/decrypt/<string:key>/<string:encrypted_val>')
def decryptage(key, encrypted_val):
    try:
        f = Fernet(key.encode())  # Charger la clé fournie
        encrypted_bytes = encrypted_val.encode()
        decrypted_text = f.decrypt(encrypted_bytes).decode()
        return f"Valeur décryptée : {decrypted_text}"
    except Exception as e:
        return f"Erreur : {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
