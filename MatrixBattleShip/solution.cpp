#include <vector>
#include <iostream>
using namespace std;

template <typename T>
class Solution {
public:
  int counterBattleShips(const vector<vector<T>> &board) { // Cambio realizado aquí
    int counter = 0;
    for (int i = 0; i < board.size(); i++)
 
      for (int j = 0; j < board[i].size(); j++)
 
        if (board[i][j] == 'X')
 
          if ((i == 0 || board[i - 1][j] == '.') && (j == 0 || board[i][j - 1] == '.'))
 
            counter++;
          }
        }
      }
    }
    return counter;
  }
};

int main()
 
  Solution<char> solution;
  vector<vector<char>> board1 = {{'X', '.', '.', 'X'}, {'.', '.', '.', 'X'}, {'.', '.', '.', 'X'}};
  vector<vector<char>> board2 = {{'X', '.', '.'}, {'.', '.', 'X'}, {'X', '.', '.'}};
  vector<vector<char>> board3 = {{'.', '.', '.'}, {'.', '.', '.'}, {'.', '.', '.'}};
  vector<vector<char>> board4 = {{'X', 'X', 'X'}, {'X', 'X', 'X'}, {'X', 'X', 'X'}};
  vector<vector<char>> board5 = {{'X', '.', 'X'}, {'.', 'X', '.'}, {'X', '.', 'X'}};

  cout << solution.counterBattleShips(board1) << endl;
  cout << solution.counterBattleShips(board2) << endl;
  cout << solution.counterBattleShips(board3) << endl;
  cout << solution.counterBattleShips(board4) << endl;
  cout << solution.counterBattleShips(board5) << endl;

  return 0;
}