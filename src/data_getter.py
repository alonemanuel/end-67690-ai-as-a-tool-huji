import os

DATA_DIR_PATH = os.path.join('..', 'data')

class DataGetter:

	def __init__(self, data_dir_path=DATA_DIR_PATH):
		self.dir_path = data_dir_path

	def get_raw_data(self):
		pass
