from multiprocessing.synchronize import Event
import sys
from Xlib import X, display, Xutil, xobject
from Xlib.xobject.drawable import Window
from Xlib.protocol import event

class Xenv:
	def __init__(self) -> X:
		self.d = display.Display()
		self.screen = self.d.screen()

	def create_window(self, width, height):
	
		new_window : Window = self.screen.root.create_window(100, 100, width, height, 2,
			self.screen.root_depth,
			X.InputOutput,
			X.CopyFromParent,
			event_mask = (X.KeyPressMask |
						X.KeyReleaseMask |
						X.ButtonPressMask |
						X.ButtonReleaseMask |
						X.StructureNotifyMask))
		self.WM_DELETE_WINDOW = self.d.intern_atom('WM_DELETE_WINDOW')
		self.WM_PROTOCOLS = self.d.intern_atom("WM_PROTOCOLS")
		new_window.set_wm_protocols([self.WM_DELETE_WINDOW])
		new_window.map()

	def handle_event(self):
		e = self.d.next_event()
		if (e.type == X.ClientMessage
		and e.client_type == self.WM_PROTOCOLS
		and e.data[0] == 32 and e.data[1][0] == self.WM_DELETE_WINDOW
		or e.type == X.KeyPress and e.detail == 9):
			sys.exit(0)

		if e.type in [X.ButtonPress, X.KeyPress]:
			e : event.KeyButtonPointer
			print({X.KeyPress: "Key", X.ButtonPress : "Button"}[e.type], e.detail, "[{0}:{1}]".format(e.event_x, e.event_y))