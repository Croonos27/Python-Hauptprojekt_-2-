import tkinter as tk
def main():
    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = num1 + num2  # Ändern Sie diese Zeile, um die Verrechnung zu ändern
            result_label.config(text="Ergebnis: " + str(result))
        except ValueError:
            result_label.config(text="Ungültige Eingabe")

    # GUI erstellen
    window = tk.Tk()
    window.title("Rechner")
    window.geometry('800x600')

    # Eingabefelder erstellen
    entry1 = tk.Entry(window)
    entry1.pack()

    entry2 = tk.Entry(window)
    entry2.pack()

    # Button erstellen
    calculate_button = tk.Button(window, text="Berechnen", command=calculate)
    calculate_button.pack()

    # Label für das Ergebnis erstellen
    result_label = tk.Label(window, text="Ergebnis: ")
    result_label.pack()

    # GUI starten
    window.mainloop()
