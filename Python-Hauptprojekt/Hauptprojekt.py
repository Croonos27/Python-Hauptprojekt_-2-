import tkinter as tk
from pathlib import Path
import json
import RechnerMitGUI
import morsecode_002
import caesar_cracker
import hashlib
import secrets
import base64

ordner_path = Path.joinpath(Path(__file__).parent, 'Benutzer')
path = Path.joinpath(ordner_path, 'benutzer.json')


def generate_salt():
    # Generiere ein 256-Bit-Salt (32 Bytes) mit secrets
    return secrets.token_bytes(32)

def hash_password(password, salt):
    # Überprüfe den Typ des Passworts
    if not isinstance(password, bytes):
        password = password.encode()  # Wandele den Unicode-String in Bytes um

    # Kombiniere Passwort und Salz
    password_with_salt = password + salt

    # Erzeuge einen SHA-256 Hash
    password_hash = hashlib.sha256(password_with_salt).hexdigest()

    return password_hash, salt


def register():
    username = username_entry.get()
    password = password_entry.get()
    
    salt = generate_salt()
    password_hash, salt = hash_password(password, salt)

    # Konvertiere das Salt zu Base64 für die JSON-Speicherung
    salt_base64 = base64.b64encode(salt).decode()

    user_data = {
        'username': username,
        'password_hash': password_hash,
        'salt': salt_base64
    }

    with open(path, 'a') as file:
        json.dump(user_data, file)
        file.write('\n')

    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

def login():
    username = username_entry.get()
    password = password_entry.get()

    with open(path, 'r') as file:
        for line in file:
            user_data = json.loads(line.strip())

            stored_username = user_data.get('username', '')
            stored_password_hash = user_data.get('password_hash', '')
            stored_salt_base64 = user_data.get('salt', '')

            if username == stored_username:
                password_bytes = password.encode()
                
                # Dekodiere das Base64-codierte Salt zurück zu Bytes
                stored_salt = base64.b64decode(stored_salt_base64)

                entered_password_hash, _ = hash_password(password_bytes, stored_salt)

                if entered_password_hash == stored_password_hash:
                    result_label.config(text='Anmeldung erfolgreich', fg='green')
                    window.destroy()
                    open_hauptmenu_window()
                    return

    result_label.config(text='Anmeldung fehlgeschlagen', fg='red')
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')



def open_hauptmenu_window():
    hauptmenu_window = tk.Tk()
    hauptmenu_window.title('Hauptmenü')
    hauptmenu_window.geometry('1920x1080')

    rechner_button = tk.Button(
        hauptmenu_window, text='+-Rechner', command=RechnerMitGUI.main)
    rechner_button.pack()

    morse_button = tk.Button(
        hauptmenu_window, text='MorseCode-Decoder', command=morsecode_002.main)
    morse_button.pack()

    caesar_button = tk.Button(
        hauptmenu_window, text='Caesar-Cracker', command=caesar_cracker.main)
    caesar_button.pack()

    logout_button = tk.Button(
        hauptmenu_window, text='Logout!', command=hauptmenu_window.destroy)
    logout_button.pack()

window = tk.Tk()
window.title('Anmeldung')
window.geometry('800x600')

username_label = tk.Label(window, text='Benutzername:')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text='Passwort:')
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

login_button = tk.Button(window, text='Anmelden', command=login)
login_button.pack()

register_button = tk.Button(window, text='Registrieren', command=register)
register_button.pack()

result_label = tk.Label(window, text='')
result_label.pack()

window.mainloop()
