import src.other.garcon as gc
from src.frontend.gui import GUI
from src.other.manager import Manager

def main():
	gc.enter_func()

	manager = Manager()
	manager.run()

if __name__ == '__main__':
	main()
