"Gabriel Eduardo Duarte Llanes"

import numpy as np

def giro_x(a: float, b: float, c: float, ang: float) -> np.ndarray:
    
    """
    Rotación en el eje X: Esta función calcula la posición de un vector después de girarlo
    alrededor del eje X. Se hace mediante una matriz de rotación 
    estándar qUe actua solo sobre los componentes Y y Z, ya que el valor en X no cambia.

    La fórmula que use es la siguiente:
        [x']   [ 1      0           0    ] [x]
        [y'] = [ 0   cos(θ)   -sin(θ) ] [y]
        [z']   [ 0   sin(θ)    cos(θ) ] [z]

    Parámetros:
   
    a, b, c : float
        Coordenadas originales del vector.
    ang : float
        Ángulo de rotación en radianes.

    La funcion retorna:
   
    np.ndarray
        Vector rotado en el formato [x', y', z'].
    """
    v = np.array([a, b, c])
    mat_x = np.array([
        [1, 0, 0],
        [0, np.cos(ang), -np.sin(ang)],
        [0, np.sin(ang),  np.cos(ang)]
    ])
    return mat_x @ v


def giro_y(a: float, b: float, c: float, ang: float) -> np.ndarray:
   
    """
    Rotación en el eje Y: En este caso, el giro afecta únicamente a los componentes X y Z,
    mientras que la coordenada Y permanece sin alterarse, la matriz de rotación
    correspondiente es:

        [x']   [ cos(θ)   0   sin(θ) ] [x]
        [y'] = [   0      1     0    ] [y]
        [z']   [-sin(θ)   0   cos(θ) ] [z]

    Los parámetros que usa:
    
    a, b, c : float
        Coordenadas originales del vector.
    ang : float
        Ángulo de rotación en radianes.

    Retorna:
    
    np.ndarray
        Vector resultante después de la rotación.
    """
    v = np.array([a, b, c])
    mat_y = np.array([
        [np.cos(ang), 0, np.sin(ang)],
        [0, 1, 0],
        [-np.sin(ang), 0, np.cos(ang)]
    ])
    return mat_y @ v


def giro_z(a: float, b: float, c: float, ang: float) -> np.ndarray:
    
    """
    Rotación en el eje Z: Este giro modifica las coordenadas X y Y del vector, mientras que la componente
    Z se mantiene constante. La matriz de rotación aplicada es:

        [x']   [ cos(θ)  -sin(θ)   0 ] [x]
        [y'] = [ sin(θ)   cos(θ)   0 ] [y]
        [z']   [   0        0      1 ] [z]

    Los parámetros son:
   
    a, b, c : float
        Coordenadas originales del vector.
    ang : float
        Ángulo de rotación en radianes.

    Retorna:
 
    np.ndarray
        Vector transformado con la rotación aplicada.
    """
    v = np.array([a, b, c])
    mat_z = np.array([
        [np.cos(ang), -np.sin(ang), 0],
        [np.sin(ang),  np.cos(ang), 0],
        [0, 0, 1]
    ])
    return mat_z @ v


def rotar_vector(a: float, b: float, c: float, ang: float, eje: str) -> np.ndarray:
    
    """
    Función general de rotación. Dependiendo del eje indicado ('x', 'y' o 'z'), esta función selecciona
    la matriz de rotación adecuada y calcula el nuevo vector. 
    En caso de recibir un eje inválido se va a lanzar un error.

    Parámetros:
    
    a, b, c : float
        Coordenadas originales del vector.
    ang : float
        Ángulo de rotación en radianes.
    eje : str
        Eje de giro, puede ser 'x', 'y' o 'z' (no importa mayúscula o minúscula).

    Retorna:
    
    np.ndarray
        Vector rotado como [x', y', z'].
    """
    eje = eje.lower()
    if eje == "x":
        return giro_x(a, b, c, ang)
    elif eje == "y":
        return giro_y(a, b, c, ang)
    elif eje == "z":
        return giro_z(a, b, c, ang)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'.")


if __name__ == "__main__":
 
    entrada = input("Escribe el vector por ejemplo: '1 5.2 3': ")
    a, b, c = map(float, entrada.split())
    eje_rot = input("Escribe el eje de giro (X, Y o Z): ")
    ang_grados = float(input("Introduce el ángulo en grados: "))

    # Conversión de grados a radianes
    ang_rad = np.radians(ang_grados)

    vec_rot = rotar_vector(a, b, c, ang_rad, eje_rot)
    print(f"\nEl vector rotado {ang_grados}° alrededor del eje {eje_rot.upper()} es:\n{vec_rot}")
