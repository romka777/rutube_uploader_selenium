import argparse
from rutube_uploader_selenium import RuTubeUploader
from typing import Optional


def main(video_path: str, metadata_path: Optional[str] = None, thumbnail_path: Optional[str] = None):
    uploader = RuTubeUploader(video_path, metadata_path, thumbnail_path)
    was_video_uploaded = uploader.upload()
    assert was_video_uploaded


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video",
                        help='Path to the video file',
                        required=True)
    parser.add_argument("-t",
                        "--thumbnail",
                        help='Path to the thumbnail image',)
    parser.add_argument("--meta", help='Path to the JSON file with metadata')
    args = parser.parse_args()
    main(args.video, args.meta, args.thumbnail)
