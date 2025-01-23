import numpy as np
import matplotlib.pyplot as plt

def draw_scatter_plot():
    """
    1) Wygeneruj dane x, y (np. np.arange(10) i jakieś y losowe).
    2) Rysuj wykres punktowy (scatter).
    3) Ustaw etykiety osi, tytuł, legendę.
    4) Zwróć obiekt Figure.
    """
    np.random.seed(123)
    
    # Wygeneruj dane x i y
    x = np.arange(10)
    y = np.random.random(10) * 10  # Losowe wartości w zakresie 0-10
    
    # Utwórz obiekt Figure i Axes
    fig, ax = plt.subplots()
    
    # Narysuj wykres punktowy
    ax.scatter(x, y, color='blue', label='Random Data', alpha=0.7)
    
    # Ustaw etykiety osi i tytuł
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_title("Scatter Plot Example")
    
    # Dodaj legendę
    ax.legend()
    
    # Zwróć obiekt Figure
    return fig

if __name__ == '__main__':
    fig = draw_scatter_plot()
    plt.show()