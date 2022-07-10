from asyncio import constants
from typing import DefaultDict, Optional
from selenium_firefox.firefox import Firefox, By, Keys
from collections import defaultdict
from selenium.common.exceptions import ElementClickInterceptedException
import json
import time
from .Constant import *
from pathlib import Path
import logging
import platform

logging.basicConfig()


def load_metadata(metadata_json_path: Optional[str] = None) -> DefaultDict[str, str]:
	if metadata_json_path is None:
		return defaultdict(str)
	with open(metadata_json_path, encoding='utf-8') as metadata_json_file:
		return defaultdict(str, json.load(metadata_json_file))


class RuTubeUploader:

	def __init__(self, video_path: str, metadata_json_path: Optional[str] = None, thumbnail_path: Optional[str] = None) -> None:
		self.video_path = video_path
		self.thumbnail_path = thumbnail_path
		self.metadata_dict = load_metadata(metadata_json_path)
		current_working_dir = str(Path.cwd())
		self.browser = Firefox(current_working_dir, current_working_dir, None, None, False, False, False)
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		self.__validate_inputs()
		
		self.is_mac = False
		if not any(os_name in platform.platform() for os_name in ["Windows", "Linux"]):
			self.is_mac = True
			self.logger.debug('Mac detected')

	def __validate_inputs(self):
		if not self.metadata_dict[Constant.DICT_TITLE]:
			self.logger.warning(
				"The video title was not found in a metadata file")
			self.metadata_dict[Constant.DICT_TITLE] = Path(
				self.video_path).stem
			self.logger.warning("The video title was set to {}".format(
				Path(self.video_path).stem))
		if not self.metadata_dict[Constant.DICT_DESCRIPTION]:
			self.logger.warning(
				"The video description was not found in a metadata file")
		if not self.metadata_dict[Constant.DICT_GENRE]:
			self.logger.warning(
				"The video genre was not found in a metadata file")
		if not self.metadata_dict[Constant.DICT_ADULT]:
			self.logger.warning(
				"The video adult (18+) flag was not found in a metadata file")

	def upload(self):
		try:
			self.__login()
			return self.__upload()
		except Exception as e:
			print(e)
			self.__quit()
			raise

	def __login(self):
		self.logger.debug('Open {}'.format(Constant.RUTUBE_URL))
		self.browser.get(Constant.RUTUBE_URL)
		time.sleep(Constant.USER_WAITING_TIME)

		if self.browser.has_cookies_for_current_website():
			self.logger.debug('Load cookies')
			self.browser.load_cookies()
			time.sleep(Constant.USER_WAITING_TIME)
			self.browser.refresh()
		else:
			self.logger.info('Please sign in and then press enter')
			input()
			self.browser.get(Constant.RUTUBE_URL)
			time.sleep(Constant.USER_WAITING_TIME)
			self.browser.save_cookies()

	def __write_in_field(self, field, string, select_all=False):
		field.click()

		time.sleep(Constant.USER_WAITING_TIME)
		if select_all:
			if self.is_mac:
				field.send_keys(Keys.COMMAND + 'a')
			else:
				field.send_keys(Keys.CONTROL + 'a')
			time.sleep(Constant.USER_WAITING_TIME)
		field.send_keys(string)

	def __set_select(self, field, string):
		field.click()
		time.sleep(Constant.USER_WAITING_TIME * 2)
		li_item = self.browser.find(By.XPATH, "//li[text() = '{}']".format(string))
		if li_item:
			li_item.click()
		else:
			self.logger.error('Cant find option: {}'.format(li_item))
			self.logger.error('Field: {}'.format(field))


	def __upload(self) -> (bool):
		self.logger.debug('Open {}'.format(Constant.RUTUBE_URL))
		self.browser.get(Constant.RUTUBE_URL)
		time.sleep(Constant.USER_WAITING_TIME)
		self.logger.debug('Open {}'.format(Constant.RUTUBE_UPLOAD_URL))
		self.browser.get(Constant.RUTUBE_UPLOAD_URL)
		time.sleep(Constant.USER_WAITING_TIME)

		# video
		absolute_video_path = str(Path.cwd() / self.video_path)
		self.browser.find(By.XPATH, Constant.INPUT_FILE_VIDEO).send_keys(
			absolute_video_path)
		self.logger.debug('Attached video {}'.format(self.video_path))

		# thumb
		if self.thumbnail_path is not None:
			absolute_thumbnail_path = str(Path.cwd() / self.thumbnail_path)
			self.browser.find(By.XPATH, Constant.INPUT_FILE_THUMBNAIL).send_keys(
				absolute_thumbnail_path)
			self.logger.debug(
				'Attached thumbnail {}'.format(self.thumbnail_path))
			
			time.sleep(Constant.USER_WAITING_TIME)


		# title
		title_field = self.browser.find(By.XPATH, Constant.TITLE_TEXTAREA)
		self.__write_in_field(
			title_field, self.metadata_dict[Constant.DICT_TITLE], select_all=True)
		self.logger.debug('The video title was set to \"{}\"'.format(
			self.metadata_dict[Constant.DICT_TITLE]))

		# description
		video_description = self.metadata_dict[Constant.DICT_DESCRIPTION]
		video_description = video_description.replace("\n", Keys.ENTER);
		if video_description:
			description_field = self.browser.find(By.XPATH, Constant.DESCRIPTION_TEXTAREA)
			self.__write_in_field(description_field, video_description, select_all=True)
			self.logger.debug('The description was set to \"{}\".'.format(
				self.metadata_dict[Constant.DICT_DESCRIPTION]
			))

		# genre
		genre = self.metadata_dict[Constant.DICT_GENRE]
		if genre:
			i = 0
			while i < 4:
				try:
					genre_select = self.browser.find(By.XPATH, Constant.GENRE_SELECT)
					self.logger.debug('genre_select \"{}\".'.format(genre_select))
					self.__set_select(genre_select, genre)
					break
				# Notification "Video uploaded" may cover genre selector
				except ElementClickInterceptedException as e:
					print(e.msg)
					i += 1
					time.sleep(Constant.USER_WAITING_TIME)

			time.sleep(Constant.USER_WAITING_TIME)

		
		# adult
		adult = self.metadata_dict[Constant.DICT_ADULT]
		if adult:
			adult_checkbox = self.browser.find(By.XPATH, Constant.ADULT_CHECKBOX)
			adult_checkbox.click()

		# wait submit
		while True:
			submit_button = self.browser.find_all(By.XPATH, Constant.SUBMIT_BUTTON)[Constant.SUBMIT_BUTTON_INDEX]
			in_process = submit_button.get_attribute('disabled')
			self.logger.debug('in_process \"{}\".'.format(in_process))

			if in_process:
				time.sleep(Constant.USER_WAITING_TIME)
			else:
				break		
		
		# Save and quit
		done_button = self.browser.find_all(By.XPATH, Constant.SUBMIT_BUTTON)[Constant.SUBMIT_BUTTON_INDEX]
		done_button.click()

		self.logger.debug("Published the video successfully")
		time.sleep(Constant.USER_WAITING_TIME)
		self.__quit()
		return True

	def __quit(self):
		self.browser.driver.quit()
