from src.offline.logic_manager import LogicManager
from src.online.gui import GUI
import src.garcon2 as gc

def main():
	gc.enter_func()

	# Create manager and get predictor
	logic = LogicManager()
	logic.prepare()
	learner = logic.get_predictor()

	# Create GUI and run
	gui = GUI(learner)
	gui.run()

if __name__ == '__main__':
	main()
