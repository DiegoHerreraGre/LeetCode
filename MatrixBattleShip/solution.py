class Solution:
    def __init__(self) -> None:
        pass

    def generateBoard(self) -> list:
        self.board = []
        self.matrix = input("Choose length of the matrix (3, 6, 9): ")
        if self.matrix == "3":
            self.board = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]
        elif self.matrix == "6":
            self.board = [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        elif self.matrix == "9":
            self.board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        else:
            print("Invalid input")
            self.generateBoard()

        print(self.board)
        return self.board and self.matrix

    def generateShip(self):
        self.generateBoard()
        choose_x_y = input(
            "Choose if you want to put your ship vertically or horizontally (v/h):   "
        )

        global isVertical
        global y_input
        global position_x
        global position_y

        if choose_x_y == "v":
            isVertical = True
        elif choose_x_y == "h":
            isVertical = False
        else:
            print("Invalid input")
            self.generateShip()

        y_input = int(
            input(
                "Put the length of your Ship, choose between small = 1, 2, 3; medium = 4, 5, 6, 7; big = 8, 9, 10, 11: "
            )
        )

        if range(y_input - 1) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            print("invalid input")
            self.generateShip()
        elif range(y_input - 1) > int(self.matrix):
            print("invalid input")
        else:
            position_x = int(input("Select the column (x): "))
            position_y = int(input("Select the row (y): "))
            ship_position = [position_x, position_y]
            print(ship_position[position_x][position_y])


Solution().generateShip()
