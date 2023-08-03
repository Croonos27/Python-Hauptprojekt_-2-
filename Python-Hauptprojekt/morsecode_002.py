import tkinter as tk
def main():
    def translator():
        alphabet = {
            "a": "•-", "b": "-•••", "c": "-•-•", "d": "-••", "e": "•", "f": "••-•", "g": "--•",
            "h": "••••", "i": "••", "j": "•---", "k": "-•-", "l": "•-••", "m": "--", "n": "-•",
            "o": "---", "p": "•--•", "q": "--•-", "r": "•-•", "s": "•••", "t": "-", "u": "••-",
            "v": "•••-", "w": "•--", "x": "-••-", "y": "-•--", "z": "--••",
            "0": "-----", "1": "•----", "2": "••---", "3": "•••--", "4": "••••-", "5": "•••••",
            "6": "-••••", "7": "--•••", "8": "---••", "9": "-----",
            "?": "••--••", "!": "-•-•--", "•": "•-•-•-", ",": "--••--", ";": "-•-•-•", ":": "---•••",
            "+": "•-•-•", "-": "-••••-", "/": "-••-•", "=": "-•••-", " ": " / ",
        }

        try:
            text1 = entry1.get()
            length = len(text1)
            morse_code = ""
            for i in range(length):
               # print(i)
                active = text1[i].lower()
                if active in alphabet:
                 #   print(active)
                    morse = alphabet[active]
                    morse_code += morse + " "
                if active not in alphabet:
                 #   print(active)
                    result_label.config(text=active + "kann nicht in MorseCode übersetzt werden")
                    

            result_label.config(text="Ergebnis: " + morse_code)
        
        except ValueError:
            result_label.config(text="Ungültige Eingabe")

    # GUI erstellen
    window = tk.Tk()
    window.title("Translator")
    window.geometry('800x600')

    # Eingabefeld
    entry1 = tk.Entry(window)
    entry1.pack()

    # Button erstellen
    translator_button = tk.Button(window, text="Übersetzen", command=translator)
    translator_button.pack()

    # Label für Ausgabe
    result_label = tk.Label(window, text="Ergebnis: ")
    result_label.pack()

    # GUI starten
    window.mainloop()
