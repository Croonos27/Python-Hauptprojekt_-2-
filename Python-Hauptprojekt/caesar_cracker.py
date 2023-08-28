import tkinter as tk

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(ciphertext):
    results = []
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        results.append(f"Shift {shift:02d}: {decrypted_text}")
    return results

def main():
    def test():
        try:
            ciphertext = entry1.get()
            results = brute_force_caesar(ciphertext)
            result_label.config(text="\n".join(results))
        except ValueError:
            result_label.config(text="Ungültige Eingabe")

    # GUI erstellen
    window = tk.Tk()
    window.title("Caesar Brute Force Attack")
    window.geometry('800x600')

    # Eingabefeld
    entry1 = tk.Entry(window)
    entry1.pack()

    # Button erstellen
    translator_button = tk.Button(window, text="Caesar Brute Force Attack", command=test)
    translator_button.pack()

    # Label für Ausgabe
    result_label = tk.Label(window, text="Ergebnis: ")
    result_label.pack()

    # GUI starten
    window.mainloop()

if __name__ == "__main__":
    main()
