import src.other.garcon as gc
from src.online.manager import Manager

def main():
	gc.enter_func()

	manager = Manager()
	manager.init()
	manager.run()

if __name__ == '__main__':
	main()
