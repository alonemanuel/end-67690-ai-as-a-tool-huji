from src.garcon import Garcon
from src.speech_recognizer import SpeechRecognizer

gc = Garcon()

def main():
	gc.enter_func()
	recognizer = SpeechRecognizer()
	text1 = recognizer.record_and_parse()
	text2 = recognizer.record_and_parse()
	gc.log('TEXT1: ', text1)
	gc.log('TEXT2: ', text2)

if __name__ == '__main__':
	main()
