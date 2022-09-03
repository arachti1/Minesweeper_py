import random

class Minesweeper:
	
	def __init__(self, width: int = 10, height: int = 10, difficulty: str = "Hard", n_mines: int = None) -> None:
		print(width, height, difficulty, n_mines)
		self.width, self.height, self.difficulty = width, height, difficulty
		self.n_mines = n_mines if n_mines else int((self.width * self.height) * {"Easy":10, "Medium": 25, "Hard": 40}[difficulty] // 100)
		self.grid = [[dict({"hidden" : True, "mine": False, "weight" : 0, "flag": False, "mark": False}) for x in range(width)] for y in range(height)]
		i = 0
		while i < self.n_mines:
			x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
			if self.grid[y][x]["mine"] != True:
				self.grid[y][x]["mine"] = True
				i += 1
				for h in range(x - 1, x + 2):
					for v in range(y - 1, y + 2):
						if 0 <= h < self.width and 0 <= v < self.height and not self.grid[v][h]["mine"]:
							self.grid[v][h]["weight"] += 1
				
	def __str__(self) -> str:
		return '\n'.join(' '.join("¤" if self.grid[y][x]["mine"] else (str(self.grid[y][x]["weight"] if self.grid[y][x]["weight"] else '.')) for x in range(self.width)) for y in range(self.height))
	
		# print(sum([[self.grid[y][x]["mine"] for x in range(self.width)].count(True) for y in range(self.height)]))
	