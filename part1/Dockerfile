# Fetch ubuntu image
FROM ubuntu:22.04

# Install python on image
RUN \
    apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y build-essential
    
# create a directory for our tests
RUN mkdir /tests

# copy in our python test script
COPY test.py /tests/test.py 

# copy main our main program under test
COPY main.c /tests/main.c

# command that  will be invoked when container starts
ENTRYPOINT [ "python3", "/tests/test.py"]