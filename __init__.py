from cryptography.fernet import Fernet
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Clé de chiffrement/déchiffrement
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route pour chiffrer une valeur
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Nouvelle route pour déchiffrer une valeur
@app.route('/decrypt/', methods=['POST'])
def decrypt():
    try:
        # Récupérer les données JSON envoyées dans le corps de la requête
        data = request.json
        encrypted_text = data.get('encrypted_text', '')
        
        # Vérification que le champ existe
        if not encrypted_text:
            return jsonify({"error": "No encrypted_text provided"}), 400
        
        # Déchiffrement de la valeur
        decrypted_text = f.decrypt(encrypted_text.encode()).decode()
        return jsonify({"decrypted_text": decrypted_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
