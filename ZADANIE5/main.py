import tkinter as tk

def create_app():
    """
    Tworzy i zwraca główne okno Tkinter z prostym interfejsem.
    1) Etykieta: "Wpisz coś:"
    2) Pole Entry
    3) Przycisk "Pokaż", który wyświetli wpisany tekst w innej etykiecie
    """
    # Utwórz główne okno
    root = tk.Tk()
    root.title("Prosta aplikacja Tkinter")

    # Etykieta z instrukcją
    label_instruct = tk.Label(root, text="Wpisz coś:")
    label_instruct.pack(pady=10)

    # Pole tekstowe
    entry_text = tk.Entry(root, width=30)
    entry_text.pack(pady=10)

    # Etykieta wynikowa (początkowo pusta)
    label_result = tk.Label(root, text="")
    label_result.pack(pady=10)

    # Funkcja wywoływana po kliknięciu przycisku
    def show_text():
        text = entry_text.get()  # Pobierz tekst z pola Entry
        label_result.config(text=f"Wpisałeś: {text}")  # Wyświetl tekst w etykiecie wynikowej

    # Przycisk
    button_show = tk.Button(root, text="Pokaż", command=show_text)
    button_show.pack(pady=10)

    return root

if __name__ == '__main__':
    # Uruchom aplikację
    app = create_app()
    app.mainloop()