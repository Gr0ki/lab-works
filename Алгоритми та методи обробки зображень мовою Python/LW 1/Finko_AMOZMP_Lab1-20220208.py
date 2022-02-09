# VARIANT 19
# copy1 = {'RGB': 'R', 'File_type': 'jpg', 'quality': 23}
# copy2 = {'RGB': 'B', 'File_type': 'png', 'quality': 5}

from pathlib import Path
from os import chdir, listdir, path
import cv2


def is_present(image_dir: str, img_folder_name: str, image_name: str) -> None:
	'''Stops the program if it does not contain the "Image" folder or the required file.'''
	try:
		files = [f for f in listdir(image_dir) if path.isfile(path.join(image_dir, f))]
		if image_name not in files:
			raise OSError
	except OSError:
		print(f'{img_folder_name} directory with a {image_name} file are needed.')
		exit()


def change_cwd(image_dir: str) -> None:
	'''Changes the working directory to the "Image" folder.'''
	chdir(image_dir)


def read_image(image_name: str) -> object:
	'''Returns an image loaded from the specified file.'''
	return cv2.imread(image_name)


def convert_BGR_to_RGB(image: object) -> object:
	'''Returns converted image from BGR to RGB.'''
	return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def get_image_channel(image: object, channel: str) -> object:
	'''Returns an image in the selected color channel.'''

	match channel:
		case 'R':
			channels_to_ignore = (0,1) 		# 0-channel B, 1-channel G, 2-channel R
		case 'G':
			channels_to_ignore = (0,2) 		# 0-channel B, 1-channel G, 2-channel R
		case 'B':
			channels_to_ignore = (1,2) 		# 0-channel B, 1-channel G, 2-channel R
		case _:
			print('Unknown channel selected!')
			exit()

	img_copy = image.copy()
	img_copy[:,:,channels_to_ignore] = 0
	return img_copy


def task(image_rgb: object) -> None:
	'''Create two copies of the the source file with a properties according to the variant.'''
	img_r = get_image_channel(img_rgb, 'R')
	img_b = get_image_channel(img_rgb, 'B')
	cv2.imwrite('img_r_19.jpg', img_r, [cv2.IMWRITE_JPEG_QUALITY, 23])
	cv2.imwrite('img_b_19.png', img_b, [cv2.IMWRITE_PNG_COMPRESSION, 5])


project_dir = Path(__file__).absolute().parent
image_folder_name = 'Image'
images_dir = project_dir / image_folder_name
image_filename = 'Launching.jpg'

is_present(images_dir, image_folder_name, image_filename)
change_cwd(images_dir)
img = read_image(image_filename)
img_rgb = convert_BGR_to_RGB(img)
task(img_rgb)
