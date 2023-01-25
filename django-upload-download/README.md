# upload-download django app
Simple django app to upload and download files.

Features include, upload (size limit to 10MB), download, and list files.
The files are stored in DB.

## Possible Improvements
There various small improvements that can be made to this app, such as:
- Dockerize the app so it can be run with an orchestrator such as kubernetes and docker-compose
- Store in object storage instead of DB (S3, Minio, etc)
- Add user logic to allow only certain users to upload/download files
- Allow for large files to be downloaded using streaming
- Add a search bar to search for files
- Add a delete button

## How to run
1. Run `pip install -r requirements.txt`
2. Run `py manage.py migrate --run-syncdb`
3. Run `py manage.py runserver 127.0.0.1`

Now navigate to  http://127.0.0.1:8000/file/ to see the app running
