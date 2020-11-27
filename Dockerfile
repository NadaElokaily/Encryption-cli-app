from python:3.10.0a2-alpine3.12

# choose directory for the app
WORKDIR /app

# install dependencies
COPY /app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy Source code
COPY /app  /usr/src/app

# Run the application
CMD ['python','app/src/encryption_tool.py']
