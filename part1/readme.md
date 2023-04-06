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


## Simple test demonstration

The main.c file contains the code that we want to test.

```docker build -t my-image .```

Run the image.

```
$ docker run --rm my-image
Building...


Running...
Output:  Hello, world!

All tests pasted!
```

Check return code from Docker

```
$ echo $?
0
```

This command returns the exit status of the last command run in the terminal. ```$?``` is useful in shellscripts as a way to decide what to do depending on how the previous command worked (checking the exit status). We can expect that the exit status is 0 when the previous command worked (finished successfully), otherwise a non-zero numerical value.


## Simple test demonstration with error
Modify the main.c removing the semicolon after the printf command. 

```
docker rmi my-image
docker build -t my-image .
docker run --rm my-image

Building...

/tests/main.c: In function ‘main’:
/tests/main.c:4:30: error: expected ‘;’ before ‘return’
    4 |     printf("Hello, world!\n")
      |                              ^
      |                              ;
    5 |     return 0; //Docker will use this return to accomplish the automated testing.
      |     ~~~~~~                    

Compilation failed.
```

Check return code

```
$ echo $? 
1
```


# Intro to CI/CD Part 2: Getting started with Github Actions

Source: Video by Shawn Hymel created for Digi-Key electronics 
https://www.youtube.com/watch?v=8pyqbYDYkRs


Make sure Actions are enabled in Github Settings. 

