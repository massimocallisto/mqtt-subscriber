# set base image (host OS)
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /opt

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY app.py .

ENV SERVER_ADDR "localhost"
ENV PORT "1883"
ENV USERNAME $a
ENV PASSWORD $a
ENV TOPIC "#"
ENV MODE "a"


# command to run on container start
CMD [ "python", "-u", "app.py"]
