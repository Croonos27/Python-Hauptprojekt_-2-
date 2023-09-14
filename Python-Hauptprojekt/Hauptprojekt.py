import tkinter as tk
import RechnerMitGUI
import morsecode_002
import caesar_cracker
import hashlib

path = r"C:\Users\Sim.Hibbeln\Documents\Python\Python-Hauptprojekt_-2-\Python-Hauptprojekt\Benutzer\benutzer.txt"
def register():
    username = username_entry.get()

    password = password_entry.get()
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    with open(path, 'a') as file:
        file.write(f'{username}:{password_hash}\n')

    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


def login():
    username = username_entry.get()
    password = password_entry.get()
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    with open(path, 'r') as file:
        for line in file:
            stored_username, stored_password_hash = line.strip().split(':')
            if username == stored_username and password_hash == stored_password_hash:
                result_label.config(text='Anmeldung erfolgreich', fg='green')
                window.destroy()  # Schließt das Anmeldefenster
                open_hauptmenu_window()
                return

    result_label.config(text='Anmeldung fehlgeschlagen', fg='red')
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


def open_hauptmenu_window():
    hauptmenu_window = tk.Tk()
    hauptmenu_window.title('Hauptmenü')
    hauptmenu_window.geometry('1920x1080')

    # Hier kannst du den Code für das Hauptmenü-Fenster einfügen
    # Füge die weiteren Buttons, Labels usw. hinzu, die du benötigst
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
        hauptmenu_window, text='Logout!', command=exit)
    logout_button.pack()


# GUI initialisieren
window = tk.Tk()
window.title('Anmeldung')
window.geometry('800x600')

# Benutzername-Eingabefeld
username_label = tk.Label(window, text='Benutzername:')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Passwort-Eingabefeld
password_label = tk.Label(window, text='Passwort:')
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

# Anmelde-Button
login_button = tk.Button(window, text='Anmelden', command=login)
login_button.pack()

# Registrieren-Button
register_button = tk.Button(window, text='Registrieren', command=register)
register_button.pack()

# Ergebnis-Anzeige
result_label = tk.Label(window, text='')
result_label.pack()

# GUI starten
window.mainloop()
