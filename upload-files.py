import anonfile


try:

    # upload files.
    files = {
        "file": ("filename","filepath", "rb")
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
