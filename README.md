## About
Python script to upload videos on RuTube using Selenium. Based on https://github.com/linouk23/youtube_uploader_selenium

## Package Installation
```bash
pip3 install --upgrade rutube-uploader-selenium
```

## Script Installation

```bash
git clone https://github.com/romka777/rutube_uploader_selenium
cd rutube-uploader-selenium
```

## Package Usage
```python
from youtube_uploader_selenium import YouTubeUploader

video_path = '123/rockets.flv'
metadata_path = '123/rockets_metadata.json'

uploader = YouTubeUploader(video_path, metadata_path, thumbnail_path)
was_video_uploaded, video_id = uploader.upload()
assert was_video_uploaded
```

## Script Usage
At a minimum, just specify a video:

```bash
python3 upload.py --video rockets.flv
```

If it is the first time you've run the script, a browser window should popup and prompt you to provide YouTube credentials (and then simply press <it>Enter</it> after a successful login).
A token will be created and stored in a file in the local directory for subsequent use.

Video title, description and other metadata can specified via a JSON file using the `--meta` flag:
```bash
python3 upload.py --video rockets.flv --meta metadata.json
```

An example JSON file would be:
```json
{
  "title": "Best Of James Harden | 2019-20 NBA Season",
  "description": "Check out the best of James Harden's 2019-20 season so far!",
  "genre": "Videogames",
  "adult": 0
}
```

## Dependencies
* geckodriver
* Firefox **[(Works with version 77)](https://ftp.mozilla.org/pub/firefox/releases/)**
* selenium_firefox

## FAQ
* [Selenium using Python - Geckodriver executable needs to be in PATH](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)
* [SessionNotCreatedException: Message: Unable to find a matching set of capabilities](https://stackoverflow.com/questions/47782650/selenium-common-exceptions-sessionnotcreatedexception-message-unable-to-find-a)
   * Please make sure that Firefox browser is installed on your machine.

## License
[MIT](https://choosealicense.com/licenses/mit/)
