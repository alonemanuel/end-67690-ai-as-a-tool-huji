from src.garcon import Garcon
from src.recorder import Recorder
from src.speech_recognizer import SpeechRecognizer

gc = Garcon()

def main():
	gc.enter_func()
	# recorder = Recorder()
	# recorder.record()
	recognizer = SpeechRecognizer()
	recognizer.get_text_from_mic()

if __name__=='__main__':
	main()