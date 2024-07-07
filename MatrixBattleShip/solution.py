import unittest


class Solution:
	def countBattleships(self, board: list[list[str]]) -> int:
		count = 0

		for i, row in enumerate(board):
			for j, cell in enumerate(row):
				if cell == "X":
					if (i == 0 or board[i - 1][j] == ".") and (
						j == 0 or board[i][j - 1] == "."
					):
						count += 1
		return count


class TestSolution(unittest.TestCase):
	def test_countBattleships(self):
		sol = Solution()
		self.assertEqual(sol.countBattleships(["X..X", "...X", "...X"]), 2)
		self.assertEqual(sol.countBattleships(["X..", "..X", "X.."]), 3)
		self.assertEqual(sol.countBattleships(["...", "...", "..."]), 0)
		self.assertEqual(sol.countBattleships(["XXX", "XXX", "XXX"]), 1)
		self.assertEqual(sol.countBattleships(["X.X", ".X.", "X.X"]), 5)


if __name__ == '__main__':
	unittest.main()
