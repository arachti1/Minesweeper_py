import sys
from Minesweeper import Minesweeper
from X import Xenv

def check_args() -> dict:
	if len(sys.argv) == 1:
		return None
	d = {}
	if len(sys.argv) >= 3:
		d.update({"width":int(sys.argv[1]), "height":int(sys.argv[2])})
	if len(sys.argv) == 2 or len(sys.argv) == 4:
		d.update({"n_mines": int(sys.argv[-1])} if sys.argv[-1].isnumeric() else {"difficulty": sys.argv[-1]})
	print(d)
	return d

xenv = Xenv()
xenv.create_window(1000, 1000)

msp = Minesweeper(**check_args())
print(msp)

while 1:
	xenv.handle_event()
