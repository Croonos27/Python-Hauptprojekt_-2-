import tkinter as tk
def main():
    
    def translator():
        alphabet = {}
        alphabet["a"] = ".-"
        alphabet["b"] = "-..."
        alphabet["c"] = "-.-."
        alphabet["d"] = "-.."
        alphabet["e"] = "."
        alphabet["f"] = "..-."
        alphabet["g"] = "--."
        alphabet["h"] = "...."
        alphabet["i"] = ".."
        alphabet["j"] = ".---"
        alphabet["k"] = "-.-"
        alphabet["l"] = ".-.."
        alphabet["m"] = "--"
        alphabet["n"] = "-."
        alphabet["o"] = "---"
        alphabet["p"] = ".--."
        alphabet["q"] = "--.-"
        alphabet["r"] = ".-."
        alphabet["s"] = "..."
        alphabet["t"] = "-"
        alphabet["u"] = "..-"
        alphabet["v"] = "...-"
        alphabet["w"] = ".--"
        alphabet["x"] = "-..-"
        alphabet["y"] = "-.--"
        alphabet["z"] = "--.."
        alphabet["0"] = "-----"
        alphabet["1"] = ".----"
        alphabet["2"] = "..---"
        alphabet["3"] = "...--"
        alphabet["4"] = "....-"
        alphabet["5"] = "....."
        alphabet["6"] = "-...."
        alphabet["7"] = "--..."
        alphabet["8"] = "---.."
        alphabet["9"] = "-----"
        alphabet["?"] = "..--.."
        alphabet["!"] = "-.-.--"
        alphabet["."] = ".-.-.-"
        alphabet[","] = "--..--"
        alphabet[";"] = "-.-.-."
        alphabet[":"] = "---..."
        alphabet["+"] = ".-.-."
        alphabet["-"] = "-....-"
        alphabet["/"] = "-..-."
        alphabet["="] = "-...-"

        try:
            text1 = str(entry1.get())
            length = entry1.size()
            ausgabe = ""
            speicher = ""
            for i in xrange(0,length):
                if i == 0:
                    active = text1[i:i].lower()
                else:
                    active = text1[i:i].lower()
                
                if active in alphabet:
                  morse = alphabet[active]
                  ausgabe += morse
                else:
                    result_label.config(text="Das Zeichen: "+ active + " ist üngültig!")
                    break
                
                result_label.config(morse)
          #  active = text1[:1]
           
        except ValueError:
            result_label.config(text="Ungültige Eingabe")

    # GUI erstellen
    window = tk.Tk()
    window.title("Translator")
    window.geometry('800x600')

    #Eingabefelder
    entry1 = tk.Entry(window)
    entry1.pack()

    #Button erstellen
    translator_button = tk.Button(window, text="Übersetzen", command=translator)

    #Label für Ausgabe
    result_label = tk.Label(window, text="Ergebnis: ")
    result_label.pack()

    #GUI starten
    window.mainloop()
    
