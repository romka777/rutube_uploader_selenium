class Constant:

    USER_WAITING_TIME = 1

    # Urls
    RUTUBE_URL = 'https://rutube.ru'
    RUTUBE_UPLOAD_URL = 'https://studio.rutube.ru/uploader/'
    RUTUBE_PLAYLISTS = 'https://studio.rutube.ru/playlists'
    RUTUBE_PLAYLIST_CREATE = 'https://studio.rutube.ru/create-playlist'

    # Meta json names
    DICT_TITLE = "title"
    DICT_DESCRIPTION = "description"
    DICT_GENRE = "genre"
    DICT_ADULT = "adult"
    DICT_PLAYLIST_TITLE = "playlist_title"
    DICT_PLAYLIST_DESCRIPTION = "playlist_description"

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
    VIDEO = "//a[@title='{}']"
    
    PLAYLIST_TITLE = "//input[@name='title']"
    PLAYLIST_DESCRIPTION = "//textarea[@name='description']"
    PLAYLIST_BUTTON_SUMBIT = "//button[@type='submit']"
    PLAYLIST = "//a[@title='{}']"
    PLAYLIST_ADD_VIDEO_BUTTON = "//button[@type='button']"
    PLAYLIST_VIDEO_CHECKBOX = "//a[@title='{}']/ancestor::article/..//input"
    PLAYLIST_ADD_VIDEO_SUBMIT_INDEX = 7

    