import numpy as np
import pandas as pd

def create_and_filter_data():
    """
    1) Wygeneruj tablicę numpy z losowymi liczbami całkowitymi.
    2) Umieść je w DataFrame (np. kolumny ['A', 'B']).
    3) Odfiltruj wiersze, w których kolumna 'A' spełnia pewien warunek (np. > 50).
    4) Zwróć przefiltrowany DataFrame.
    """
    # Ustaw ziarno losowości dla powtarzalności wyników
    np.random.seed(123)
    
    # Wygeneruj tablicę NumPy z losowymi liczbami całkowitymi (10 wierszy, 2 kolumny, wartości 0-100)
    arr = np.random.randint(0, 101, size=(10, 2))
    
    # Utwórz DataFrame z nazwami kolumn ['A', 'B']
    df = pd.DataFrame(arr, columns=['A', 'B'])
    
    # Odfiltruj wiersze, gdzie wartość w kolumnie 'A' > 50
    filtered_df = df[df['A'] > 50]
    
    # Zwróć przefiltrowany DataFrame
    return filtered_df

if __name__ == '__main__':
    # Przykładowe wywołanie
    result_df = create_and_filter_data()
    print("Otrzymany DataFrame (A > 50):")
    print(result_df)