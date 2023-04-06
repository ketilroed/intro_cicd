# Intro CI/CD Part 1: Getting started with Docker

Source: Video by Shawn Hymel created for Digi-Key electronics 
https://www.youtube.com/watch?v=1nxGcfIm-TU

## Build image
```docker build -t my-image```
List images

```docker images```


## Create container 
```docker container create -i -t --entrypoint="/bin/bash" --name my-container my-image```
Here the --entrypoint overrides the entrypoint in the Dockerfile. Meaning that when the container is run 
it will start with a command prompt.

List containers 
```docker container ls -a```

Copy another file into the container

```
touch another-test.py
echo "print(\"Hello, from another test!\")" > another-test.py
docker cp another-test.py my-container:/tests/another-test.py
```

## Start container
```docker start -i my-container```

## Remove container and image

```docker rm my-container```

or 

```docker container rm <name of container>```

or if you want to delete all containers 

```docker container prune```

Delete image

```docker image rm my-image``` 
or 
```docker rmi my-image```


## Run container directly from image

```docker run my-image```

This is a combination of create and start. It will create a new container with an automatically generated name and start the container.

Provide a name and automatically delete container when stopped

```docker run --name my-container --rm my-image```
