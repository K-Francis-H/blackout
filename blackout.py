from tkinter import *

class Blackout:

	def __init__(self):
		self.window = Tk()
		self.window.title("Blackout")
		self.window.configure(background="black")
		self.window.bind("<Button-1>", self.toggle_fullscreen)

		self.is_fullscreen = False

	def toggle_fullscreen(self, event=None):
		if self.is_fullscreen:
			self.window.attributes("-fullscreen", False)
		else:
			self.window.attributes("-fullscreen", True)
		self.is_fullscreen = not self.is_fullscreen

if __name__ == '__main__':
	app = Blackout()
	app.window.mainloop()
