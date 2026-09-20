import numpy as np

def generate_resonance_field(grid_size, source_a, source_b, frequency):
    """
    Generuje mapę przestrzennego rezonansu pola dla dwóch punktów źródłowych.
    """
    x = np.linspace(-10, 10, grid_size)
    y = np.linspace(-10, 10, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Odległości od źródeł A i B
    dist_a = np.sqrt((X - source_a)**2 + (Y - source_a)**2)
    dist_b = np.sqrt((X - source_b)**2 + (Y - source_b)**2)
    
    # Interferencja fal rezonansu przestrzennego
    field_a = np.sin(frequency * dist_a) / (dist_a + 1e-5)
    field_b = np.sin(frequency * dist_b) / (dist_b + 1e-5)
    
    # Pole rezonansu sprzężonego (splątanego)
    resonance_field = field_a * field_b
    return resonance_field

if __name__ == "__main__":
    # Inicjalizacja parametrów symulacji układu kwantowego
    GRID_SIZE = 100
    SOURCE_A = (-4, 0)
    SOURCE_B = (4, 0)
    FREQ = 2.5
    
    grid = generate_resonance_field(GRID_SIZE, SOURCE_A, SOURCE_B, FREQ)
    print(f"Pomyślnie wygenerowano siatkę pola rezonansowego o wymiarach {grid.shape}.")
    print(f"Maksymalna amplituda sprzężenia: {np.max(grid):.4f}")
