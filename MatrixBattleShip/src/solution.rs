fn counter_battle_ship(board: Vec<Vec<char>>) -> i32 {
  let mut counter: i32 = 0;

  for i in 0..board.len() {
    for j in 0..board[i].len() {
      if board[i][j] == 'X' && (i == 0 || board[i - 1][j] == '.') && (j == 0 || board[i][j - 1] == '.') {
        counter += 1;
      }
    }
  }
  counter
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_counter_battle_ship() {
        let board1 = vec![vec!['X', '.', '.'], vec!['.', 'X', '.'], vec!['.', '.', 'X']];
        assert_eq!(counter_battle_ship(board1), 3);

        let board2 = vec![vec!['X', '.', 'X'], vec!['.', '.', '.'], vec!['X', '.', 'X']];
        assert_eq!(counter_battle_ship(board2), 4);

        let board3 = vec![vec!['.', '.', '.'], vec!['.', '.', '.'], vec!['.', '.', '.']];
        assert_eq!(counter_battle_ship(board3), 0);

        let board4 = vec![vec!['X', 'X', 'X'], vec!['X', 'X', 'X'], vec!['X', 'X', 'X']];
        assert_eq!(counter_battle_ship(board4), 1);

        let board5 = vec![vec!['X', '.', 'X'], vec!['.', 'X', '.'], vec!['X', '.', 'X']];
        assert_eq!(counter_battle_ship(board5), 5);
    }
}

fn main() {
    let board = vec![vec!['X', '.', '.'], vec!['.', 'X', '.'], vec!['.', '.', 'X']];
    println!("{:?}", counter_battle_ship(board));
}
