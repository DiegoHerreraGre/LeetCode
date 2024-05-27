function counterBattleShips(board) {
  let counter = 0;

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === "X") {
        if ((i === 0 || board[i - 1][j] === ".") && (j === 0 || board[i][j - 1] === ".")) {
          counter++;
        }
      }
    }
  }
  return counter;
}

// Tests
console.log(counterBattleShips(["X..X", "...X", "...X"])); // Debería imprimir 2
console.log(counterBattleShips(["X..", "..X", "X.."])); // Debería imprimir 3
console.log(counterBattleShips(["...", "...", "..."])); // Debería imprimir 0
console.log(counterBattleShips(["XXX", "XXX", "XXX"])); // Debería imprimir 1
console.log(counterBattleShips(["X.X", ".X.", "X.X"])); // Debería imprimir 5
