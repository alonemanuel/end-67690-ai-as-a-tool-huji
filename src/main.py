from src.data_generator import TrainDataGenerator
from src.garcon import Garcon
from src.speech_recognizer import SpeechRecognizer
from src.actor_dataset_parser import ActorDataParser

gc = Garcon()

def main():
	gc.enter_func()
	# generator = TrainDataGenerator()
	# generator.generate_predefined_data()
	parser = ActorDataParser()
	parser.parse()

if __name__ == '__main__':
	main()
