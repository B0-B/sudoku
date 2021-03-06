```
╟───┼───┼───╫───┼───┼───╫
║ S │ U │ D ║ O │ K │ U ║
╟───┼───┼───╫───┼───┼───╫
```
# Start
## Install
Pull the repository and run in the root directory
```bash
~../sudoku$ pip3 install .
```

## Usage

```python
puzzle = np.array([
    [5, 8, 0, 6, 0, 2, 4, 3, 0],
    [0, 0, 2, 0, 4, 3, 0, 5, 1],
    [3, 6, 0, 5, 0, 1, 7, 8, 0],
    [0, 3, 8, 0, 5, 0, 2, 0, 6],
    [2, 5, 0, 1, 8, 4, 9, 7, 0],
    [1, 7, 9, 3, 0, 6, 0, 4, 5],
    [8, 0, 5, 2, 1, 0, 3, 0, 7],
    [0, 1, 0, 7, 0, 8, 0, 2, 4],
    [6, 0, 7, 4, 0, 5, 1, 0, 8]])

# load the puzzle into sudoku object
from sudoku import sudoku

sdk = sudoku(puzzle)
# or sdk.insert(puzzle)
sdk.solve()
sdk.show()
```
```bash
            ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
            ║ 5 │ 8 │ 1 ║ 6 │ 7 │ 2 ║ 4 │ 3 │ 9 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ 7 │ 9 │ 2 ║ 8 │ 4 │ 3 ║ 6 │ 5 │ 1 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ 3 │ 6 │ 4 ║ 5 │ 9 │ 1 ║ 7 │ 8 │ 2 ║
            ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
            ║ 4 │ 3 │ 8 ║ 9 │ 5 │ 7 ║ 2 │ 1 │ 6 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ 2 │ 5 │ 6 ║ 1 │ 8 │ 4 ║ 9 │ 7 │ 3 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ 1 │ 7 │ 9 ║ 3 │ 2 │ 6 ║ 8 │ 4 │ 5 ║
            ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
            ║ 8 │ 4 │ 5 ║ 2 │ 1 │ 9 ║ 3 │ 6 │ 7 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ 9 │ 1 │ 3 ║ 7 │ 6 │ 8 ║ 5 │ 2 │ 4 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ 6 │ 2 │ 7 ║ 4 │ 3 │ 5 ║ 1 │ 9 │ 8 ║
            ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
```

## Generate

```python
sdk.new(fill=0.4)
sdk.show()
```
```bash
            ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
            ║   │   │ 1 ║   │   │   ║ 8 │ 4 │   ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║   │   │   ║ 7 │   │   ║   │ 2 │ 1 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║   │ 9 │ 8 ║   │   │   ║ 5 │   │   ║
            ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
            ║ 4 │ 1 │ 7 ║ 6 │ 5 │ 3 ║   │   │ 9 ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║   │   │   ║   │ 8 │   ║ 4 │   │   ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║   │   │ 9 ║   │ 2 │   ║   │ 1 │   ║
            ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
            ║ 7 │   │   ║   │ 3 │   ║   │ 9 │   ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║   │   │   ║   │   │ 2 ║ 6 │   │   ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║   │   │ 4 ║   │   │ 6 ║ 7 │   │ 2 ║
            ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
```

pull out numpy array out of ```sudoku``` instance

```python
sudoku_array = sdk.panel
```
