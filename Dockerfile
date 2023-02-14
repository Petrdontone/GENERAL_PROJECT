# Container image that runs your code
FROM python:3.8

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY ./ .


