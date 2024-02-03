#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os
import shutil

def DownloadOrganizer(path_to_downloads):
    file_format = {}
    file_format['Documents'] = ['.docx', '.doc', '.docx', '.pdf', '.pptx', '.xls'],
    file_format['Images'] = ['.jpg', 'jpeg', 'png', 'tiff'],
    file_format['Audio'] = ['.mp3', '.wav', '.m4a', '.flac']
    file_format['Videos'] = ['.mp4', '.avi', '.mov', 'mkv', 'mpg', 'mpeg', 'mpeg2']
    file_format['Archives'] = ['.zip', '.rar', '.gz', '.bz2', '.tar.gz']
    file_format['Coding'] = ['.py','.js', '.css', '.jsx', '.jsp']
    file_format['Other'] = []
    for filename in os.listdir(path_to_downloads):
        filepath = os.path.join(path_to_downloads, filename)

        if os.path.isfile(filepath):
            _, file_extension = os.path.splitext(filepath)
        destination = None
        for i, j in file_format.items():
            if file_extension in j:
                destination = i
                break

        if destination is None:
            destination = 'Other'

        newDir = os.path.join(path_to_downloads, destination)
        os.makedirs(newDir, exist_ok=True)
        shutil.move(filepath, os.path.join(newDir, filename))

if __name__ == '__main__':
    path_to_downloads = os.path.expanduser("~/Downloads")
    DownloadOrganizer(path_to_downloads)
