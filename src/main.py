from src.offline.logic_manager import LogicManager
from src.online.gui import GUI
import src.garcon2 as gc

def main():
	gc.enter_func()

	logic = LogicManager()
	logic.prepare()
	learner = logic.get_learner()

	gui = GUI(learner)
	gui.run()

if __name__ == '__main__':
	main()
