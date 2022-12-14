import os
import html
from flask import Flask, render_template, request

from _rsa import rsa_encrypt, rsa_decrypt, public_key
from _vigenere import vigenere_encrypt, vigenere_decrypt

app = Flask(__name__)

# ===HOME=========================================================================================


@app.route('/', methods=['get', 'post'])
def home() -> 'html':
    '''Retorna um template que diz ao usuário o objetivo da aplicação'''
    return render_template('_home.html', menu_home='active')


# ===vigenere=====================================================================================


@app.route('/vigenere')
def vigenere() -> 'html':
    '''Retorna um template para que o usuário teste o modelo de criptografia vigenere'''
    return render_template('_vigenere.html', menu_vigenere='active', text='')


@app.route('/vigenere/criptografar', methods=['GET', 'POST'])
def vigenere_criptografar() -> 'html':
    '''Criptografa o texto fornecido pelo usuário'''
    
    key = str(request.form.get('key_encrypt')).upper()
    text = str(request.form.get('decrypt_text')).upper()

    encrypted_text = vigenere_encrypt(text=text, key_word=key)

    return render_template('_vigenere.html', menu_vigenere='active', encrypted_text=encrypted_text, key_word=key)


@app.route('/vigenere/descriptografar', methods=['GET', 'POST'])
def vigenere_descriptografar() -> 'html':
    '''Criptografa o texto fornecido pelo usuário'''
    
    key = str(request.form.get('key_decrypt'))
    text = str(request.form.get('encrypt_text'))

    decrypted_text = vigenere_decrypt(text=text, key_word=key)

    return render_template('_vigenere.html', menu_vigenere='active', decrypted_text=decrypted_text, key_word=key)


# ===RSA===========================================================================================


@app.route('/rsa')
def rsa() -> 'html':
    '''Retorna um template para que o usuário teste o modelo de criptografia RSA'''
    return render_template('_rsa.html', menu_rsa='active')


@app.route('/rsa/criptografar', methods=['GET', 'POST'])
def rsa_criptografar() -> 'html':
    '''Criptografa o texto fornecido pelo usuário'''
    
    text_for_page = ''
    keys = public_key()
    text = str(request.form.get('decrypt_text'))

    encrypted_text = rsa_encrypt(text=text, key_one=keys[0], key_two=keys[1])

    for char in  encrypted_text:
        char = char.replace('[', '')
        char = char.replace(']', '')
        text_for_page += char

    return render_template('_rsa.html', menu_rsa='active', encrypted_text=text_for_page)


@app.route('/rsa/descriptografar', methods=['GET', 'POST'])
def rsa_descriptografar() -> 'html':
    '''DesCriptografa o texto fornecido pelo usuário'''

    keys = public_key()
    text = str(request.form.get('encrypt_text'))

    decrypt_text = rsa_decrypt(text=text, key_one=keys[0])

    return render_template('_rsa.html', menu_rsa='active', decrypted_text=decrypt_text)


# ========================================================================================

if __name__ == "__main__":
    app.run(debug=True)