# Anonfiles-api

Anonfiles is a Python library for upload files on [anonfiles.com](https://anonfiles.com/). 

## About

This **unofficial** Python API was created to make uploading and downloading files from [anonfiles.com](https://anonfiles.com/) simple

## Installation


```bash
pip install anonfile
```

## Usage

### Upload files

```python
import anonfile


try:

    # upload files.
    files = {
        "file": ("filename","filepath", "rb"))
    }

    upload = requests.post("https://api.anonfiles.com/upload", files=files)

    try:

        # get download link 
        x = upload.json()
        url = x["data"]["file"]["url"]["short"]
    
    except Exception as e:
        print(e)
        # can't get download link.
  
except Exception:
    print(e)
    # your file can't be uploaded.
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

## License
[MIT](https://choosealicense.com/licenses/mit/)
