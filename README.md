# Anonfiles-api
[![License](https://img.shields.io/badge/license-MIT-blue)](https://choosealicense.com/licenses/mit/)
[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) 

Anonfiles is a Python library, used to upload files on [anonfiles.com](https://anonfiles.com/). 

## About

This **unofficial** Python API was created to make uploading and downloading files from [anonfiles.com](https://anonfiles.com/) simple.

## Installation


```bash
pip install requests && pip install wget
```

## Usage

### Upload files

```python
import requests


try:

    # upload files.
    files = {
        "file": ("filename", "filepath", "rb")
    }

    upload = requests.post("https://api.anonfiles.com/upload", files=files)

    try:

        # get download link 
        x = upload.json()
        url = x["data"]["file"]["url"]["short"]
        print(url)
        input()
    
    except Exception as e:
        print(e)
        # can't get download link.
  
except Exception as e:
    print(e)
    # your file can't be uploaded.
```
### Download files (it doesn't use the anonfile api)
```python
import wget


try:

    download = wget.download("direct URL") # How? https://encrypting.host/f7nkbiHzgK.gif?key=x05yQJBDd7qgYN
  
except Exception as e:
    print(e)
    # your file can't be downloaded.
```
## Error Handling
* (10) ERROR_FILE_NOT_PROVIDED
* (11) ERROR_FILE_EMPTY
* (12) ERROR_FILE_INVALID
* (20) ERROR_USER_MAX_FILES_PER_HOUR_REACHED
* (21) ERROR_USER_MAX_FILES_PER_DAY_REACHED
* (22) ERROR_USER_MAX_BYTES_PER_HOUR_REACHED
* (23) ERROR_USER_MAX_BYTES_PER_DAY_REACHED
* (30) ERROR_FILE_DISALLOWED_TYPE
* (31) ERROR_FILE_SIZE_EXCEEDED
* (32) ERROR_FILE_BANNED
* (40) STATUS_ERROR_SYSTEM_FAILURE

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
