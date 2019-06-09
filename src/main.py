from src.data_generator import TrainDataGenerator
from src.garcon import Garcon
from src.speech_recognizer import SpeechRecognizer

gc = Garcon()

def main():
	gc.enter_func()
	generator = TrainDataGenerator()
	generator.generate_predefined_data()

if __name__ == '__main__':
	main()
