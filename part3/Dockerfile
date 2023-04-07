# Fetch ubuntu image
FROM ubuntu:22.04

# Install build tools
RUN apt-get update && \
    apt-get install -y git build-essential autoconf automake libtool

# Copy project into image
RUN mkdir /project
COPY src /project/src
COPY tests /project/tests
COPY Makefile /project/Makefile

# Download and buld CppUTest
RUN mkdir /project/tools/ && \
    cd /project/tools && \
    git clone https://github.com/cpputest/cpputest.git && \
    cd cpputest && \
    autoreconf -i && \
    ./configure && \
    make     

# Execute script
ENTRYPOINT [ "make", "test", "-C", "/project/" ]