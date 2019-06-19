import src.other.garcon as gc
from src.offline.actor_dataset_parser import ActorDataParser
from src.online.manager import Manager
from src.other.dummy import Dummy

def main():
	gc.enter_func()

	manager = Manager()
	manager.init()
	manager.run()

if __name__ == '__main__':
	main()
