class Constant:

    USER_WAITING_TIME = 1

    # Urls
    RUTUBE_URL = 'https://rutube.ru'
    RUTUBE_UPLOAD_URL = 'https://studio.rutube.ru/uploader/'

    # Meta json names
    DICT_TITLE = "title"
    DICT_DESCRIPTION = "description"
    DICT_GENRE = "genre"
    DICT_ADULT = "adult"

    # Containers
    INPUT_FILE_VIDEO = "//input[@type='file']"
    INPUT_FILE_THUMBNAIL = "//input[@name='cover']"
    TITLE_TEXTAREA = "//textarea[@name='title']"
    DESCRIPTION_TEXTAREA = "//textarea[@name='description']"
    GENRE_SELECT = "//input[@name='categories']"
    ADULT_CHECKBOX = "//input[@name='adult']"
    SUBMIT_BUTTON = "//button"
    SUBMIT_BUTTON_INDEX = 2
    RELOAD_BUTTON = "//button[@icon='reloadThick']"