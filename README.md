# Matrix BattleShip

## Descripción
Este proyecto implementa un juego de Batalla Naval donde el usuario puede generar un tablero de juego y posicionar barcos en él. El tamaño del tablero y la orientación y tamaño de los barcos son configurables.

## Uso
1. **Generar Tablero**: El usuario elige el tamaño del tablero (3x3, 6x6, 9x9).
2. **Posicionar Barcos**: El usuario decide la orientación del barco (vertical u horizontal) y su tamaño.

## Instalación
Clonar el repositorio y ejecutar el archivo `solution.py` para iniciar el juego.

## Métodos Principales
- `generateBoard()`: Genera el tablero de juego basado en la entrada del usuario.
- `generateShip()`: Permite al usuario posicionar un barco en el tablero.

## Ejemplo de Uso

```python
solution = Solution()
solution.generateShip()
```


Este comando inicializa el juego, genera un tablero y permite al usuario posicionar un barco.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, asegúrese de actualizar los tests según corresponda.

## Licencia
Distribuido bajo la licencia MIT.
