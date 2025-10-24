# Insula Batch Collection Download Script

This is a script that uses Python and Insula's API to batch download all the files inside one of the collections.
This script is just a sample that shows how the API can be used on a simple use case, but it can serve as a starting point to be adapted to other needs.

### Instructions

0) Install requirements:
```bash
pip install -r requirements.txt
```

1) Modify `auth.py` with your credentials:
```bash
username = "XXXXXXXXXXXX"
password = "XXXXXXXXXXXX"
```

2) Modify `config.py` with the correct endpoints for the target Insula environment. These can be found in the "How to Switch Insula Instance" section.

3) Modify the `collection_id` of the collection you want to download inside config.py.
   If the collection id is not known it can be obtained by checking the collection from the UI in Awareness, or with other API calls.

4) Run the downloader with `python insula_download_collection.py`, the downloaded files will be found inside the `downloaded` folder.
   The script also produces a list with the successfully downloaded files, and another one with the files that for some reason failed to be downloaded. In case of interruptions, if the script is restarted it will ignore the files contained in the successfully downloaded list and continue to download only the missing ones.