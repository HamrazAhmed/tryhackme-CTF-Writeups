# Intro to Docker — Writeup

## Overview
### Intro to Docker — Writeup
### Intro to Docker — Writeup
----
Learn to create, build and deploy Docker containers!
----
![](https://assets.tryhackme.com/additional/containerisation-module/Containerisation%20banner-01-01.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/65df5e6db27b61cb80b61563f7b8c184.png)
In this room, you’ll get your first hands-on experience deploying and interacting with Docker containers.
Namely, by the end of the room, you will be familiar with the following:
- The basic syntax to get you started with Docker
- Running and deploying your first container
- Understanding how Docker containers are distributed using images
- Creating your own image using a Dockerfile
- How Dockerfiles are used to build containers, using Docker Compose to orchestrate multiple containers
- Applying the knowledge gained from the room into the practical element at the end.
**Please note:** It is strongly recommended that you are at least familiar with basic Linux syntax (such as running commands, moving files and familiarity with how the filesystem structure looks). If you have completed the [Linux Fundamentals Module](https://tryhackme.com/module/linux-fundamentals) - you will be all set for this room!
Additionally, it is important to remember that you will need internet connectivity to pull Docker images.  If you are a free user and wish to practice the commands in this room, you will need to do this in your own environment.
Answer the questions below
Complete this question before progressing to the next task.
Question Done
### Task 2  Basic Docker Syntax
Docker can seem overwhelming at first. However, the commands are pretty intuitive, and with a bit of practice, you’ll be a Docker wizard in no time.
The syntax for Docker can be categorised into four main groups:
- Running a container
- Managing & Inspecting containers
- Managing Docker images
- Docker daemon stats and information
We will break down each of these categories in this task.
### Managing Docker Images
Docker Pull
Before we can run a Docker container, we will first need an image. Recall from the “[Intro to Containerisation](https://tryhackme.com/room/introtocontainerisation)” room that images are instructions for what a container should execute. There’s no use running a container that does nothing!
In this room, we will use the Nginx image to run a web server within a container. Before downloading the image, let’s break down the commands and syntax required to download an image. Images can be downloaded using the `docker pull` command and providing the name of the image.
For example, `docker pull nginx`. Docker must know where to get this image (such as from a repository which we’ll come onto in a later task).
Continuing with our example above, let’s download this Nginx image!
A terminal showing the downloading of the "Nginx" image
```shell-session
cmnatic@thm:~$ docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
-- omitted for brevity --
Status: Downloaded newer image for nginx:latest
cmnatic@thm:~$
```
By running this command, we are downloading the latest version of the image titled “nginx”. Images have these labels called _tags_. These _tags_ are used to refer to variations of an image. For example, an image can have the same name but different tags to indicate a different version. I’ve provided an example of how tags are used within the table below:
|   |   |   |   |
|---|---|---|---|
|**Docker Image**|**Tag**|**Command Example**|**Explanation**|
|ubuntu|latest|docker pull ubuntu<br><br>**- IS THE SAME AS -**<br><br>docker pull ubuntu:latest|This command will pull the latest version of the "ubuntu" image. If no tag is specified, Docker will assume you want the "latest" version if no tag is specified.<br><br>It is worth remembering that you do not always want the "latest". This image is quite literally the "latest" in the sense it will have the most recent changes. This could either fix or break your container.|
|ubuntu|22.04|docker pull ubuntu:22.04|This command will pull version "22.04 (Jammy)" of the "ubuntu" image.|
|ubuntu|20.04|docker pull ubuntu:20.04|This command will pull version "20.04 (Focal)" of the "ubuntu" image.|
|ubuntu|18.04|docker pull ubuntu:18.04|This command will pull version "18.04 (Bionic)" of the "ubuntu" image.|
When specifying a tag, you must include a colon `:` between the image name and tag, for example, `ubuntu:22.04` (image:tag). Don’t forget about tags - we will return to these in a future task!
Docker Image x/y/z
The `docker image` command, with the appropriate option, allows us to manage the images on our local system. To list the available options, we can simply do `docker image` to see what we can do. I’ve done this for you in the terminal below:
A terminal showing the various arguments we can provide with "docker image"
```shell-session
cmnatic@thm:~$ docker image

Usage:  docker image COMMAND

Manage images

Commands:
  build       Build an image from a Dockerfile
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Display detailed information on one or more images
  load        Load an image from a tar archive or STDIN
  ls          List images
  prune       Remove unused images
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rm          Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

Run 'docker image COMMAND --help' for more information on a command.
cmnatic@thm:~$
```
- In this room, we are only going to cover the following options for docker images:
- pull (we have done this above!)
- ls (list images)
- rm (remove an image)
- build (we will come onto this in the “Building your First Container” task)
Docker Image ls
This command allows us to list all images stored on the local system. We can use this command to verify if an image has been downloaded correctly and to view a little bit more information about it (such as the tag, when the image was created and the size of the image).
A terminal listing the Docker images that are stored on the host operating system
```shell-session
cmnatic@thm:~$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       22.04     2dc39ba059dc   10 days ago   77.8MB
nginx        latest    2b7d6430f78d   2 weeks ago   142MB
cmnatic@thm:~$
```
For example, in the terminal above, we can see some information for two images on the system:
|   |   |   |   |   |
|---|---|---|---|---|
|**Repository**|**Tag**|**Image ID**|**Created**|**Size**|
|ubuntu|22.04|2dc39ba059dc|10 days ago|77.8MB|
|nginx|latest|2b7d6430f78d|2 weeks ago|142MB|
Docker Image rm
If we want to remove an image from the system, we can use `docker image rm` along with the name (or Image ID). In the following example, I will remove the "_ubuntu_" image with the tag "_22.04_". My command will be `docker image rm ubuntu:22.04`:
It is important to remember to include the _tag_ with the image name.
A terminal displaying the untagging of an image
```shell-session
cmnatic@thm:~$ docker image rm ubuntu:22.04
Untagged: ubuntu:22.04
Untagged: ubuntu@sha256:20fa2d7bb4de7723f542be5923b06c4d704370f0390e4ae9e1c833c8785644c1
Deleted: sha256:2dc39ba059dcd42ade30aae30147b5692777ba9ff0779a62ad93a74de02e3e1f
Deleted: sha256:7f5cbd8cc787c8d628630756bcc7240e6c96b876c2882e6fc980a8b60cdfa274
cmnatic@thm:~$
```
If we were to run a `docker image ls`, we would see that the image is no longer listed:
A terminal confirming that our Docker image has been deleted
```shell-session
cmnatic@thm:~$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    2b7d6430f78d   2 weeks ago   142MB
cmnatic@thm:~$
```
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
5b5fe70539cd: Pull complete 
441a1b465367: Pull complete 
3b9543f2b500: Pull complete 
ca89ed5461a9: Pull complete 
b0e1283145af: Pull complete 
4b98867cde79: Pull complete 
4a85ce26214d: Pull complete 
Digest: sha256:593dac25b7733ffb7afe1a72649a43e574778bf025ad60514ef40f6b5d606247
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
                                                                                                
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo docker image ls  
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
nginx                latest    eb4a57159180   6 days ago     187MB
jwtcrack             latest    2cbbb179013d   3 months ago   271MB
n0madic/alpine-gcc   9.2.0     9d7f59f1263e   3 years ago    251MB
                                                                                                
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo docker image rm nginx
Untagged: nginx:latest
Untagged: nginx@sha256:593dac25b7733ffb7afe1a72649a43e574778bf025ad60514ef40f6b5d606247
Deleted: sha256:eb4a57159180767450cb8426e6367f11b999653d8f185b5e3b78a9ca30c2c31d
Deleted: sha256:387c6708d068d261ce5b1fe3e67323cbf64d8a37901f3d9742557f4abb830baf
Deleted: sha256:2946620cb422511c62ba67d12b1c16bbf6b85e6ce42e93a4dace94b4a70160b3
Deleted: sha256:f2545115e362a40e5b3fe057ad159aa9824f40a0e9341f4743b4d0c4f5322435
Deleted: sha256:9b3ff8c6f07faac480afaeecc0388a387f8cf92832de656a2d35e890340ac59a
Deleted: sha256:77366f15e73eef5c23ff7bd0be0c09f1b280c9586863232392c2d500eed148e7
Deleted: sha256:7447c8c6be248218804380a22d47c130f7efc16f31550cb446fc3cc91f98a54c
Deleted: sha256:ac4d164fef90ff58466b67e23deb79a47b5abd30af9ebf1735b57da6e4af1323
                                                                                                
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo docker image ls      
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
jwtcrack             latest    2cbbb179013d   3 months ago   271MB
n0madic/alpine-gcc   9.2.0     9d7f59f1263e   3 years ago    251MB
```
If we wanted to `pull` a docker image, what would our command look like?
*docker pull*
If we wanted to list all images on a device running Docker, what would our command look like?
*docker image ls*
Let's say we wanted to pull the image "tryhackme" (no quotations); what would our command look like?
*docker pull tryhackme*
Let's say we wanted to pull the image "tryhackme" with the tag "1337" (no quotations). What would our command look like?
Remember that you specify the tag with the colon key (:)
*docker pull tryhackme:1337*
### Task 3  Running Your First Container
The Docker run command creates running containers from images. This is where commands from the Dockerfile (as well as our own input at runtime) are run. Because of this, it must be some of the first syntaxes you learn.
The command works in the following way: `docker run [OPTIONS] IMAGE_NAME [COMMAND] [ARGUMENTS...]`  the options enclosed in brackets are not required for a container to run.
Docker containers can be run with various options - depending on how we will use the container. This task will explain some of the most common options that you may want to use.
First, Simply Running a Container
Let's recall the syntax required to run a Docker container: `docker run [OPTIONS] IMAGE_NAME [COMMAND] [ARGUMENTS...]` . In this example, I am going to configure the container to run:
- An image named "helloworld"
- "Interactively" by providing the `-it` switch in the [OPTIONS] command. This will allow us to interact with the container directly.
- I am going to spawn a shell within the container by providing `/bin/bash` as the [COMMAND] part. This argument is where you will place what commands you want to run within the container (such as a file, application or shell!)
So, to achieve the above, my command will look like the following: `docker run -it helloworld /bin/bash`
A terminal showing a container being launched in 'interactive' mode
```shell-session
cmnatic@thm-intro-to-docker:~$ docker run -it helloworld /bin/bash
root@30eff5ed7492:/#
```
We can verify that we have successfully launched a shell because our prompt will change to another user account and hostname. The hostname of a container is the container ID (which can be found by using `docker ps`). For example, in the terminal above, our username and hostname are `root@30eff5ed7492`
Running Containers...Continued
As previously mentioned, Docker containers can be run with various options. The purpose of the container and the instructions set in a Dockerfile (we'll come onto this in a later task) determines what options we need to run the container with. To start, I've put some of the most common options you may need to run your Docker container into the table below.
|   |   |   |   |
|---|---|---|---|
|**[OPTION]**|**Explanation**|**Relevant Dockerfile Instruction**|**Example**|
|-d|This argument tells the container to start in "detached" mode. This means that the container will run in the background.|N/A|`docker run -d helloworld`|
|-it|This argument has two parts. The "i" means run interactively, and "t" tells Docker to run a shell within the container. We would use this option if we wish to interact with the container directly once it runs.|N/A|`docker run -it helloworld`|
|-v|This argument is short for "Volume" and tells Docker to mount a directory or file from the host operating system to a location within the container. The location these files get stored is defined in the Dockerfile|VOLUME|`docker run -v /host/os/directory:/container/directory helloworld`|
|-p|This argument tells Docker to bind a port on the host operating system to a port that is being exposed in the container. You would use this instruction if you are running an application or service (such as a web server) in the container and wish to access the application/service by navigating to the IP address.|EXPOSE|`docker run -p 80:80 webserver`|
|--rm|This argument tells Docker to remove the container once the container finishes running whatever it has been instructed to do.|N/A|`docker run --rm helloworld`|
|--name|This argument lets us give a friendly, memorable name to the container. When a container is run without this option, the name is two random words. We can use this open to name a container after the application the container is running.|N/A|`docker run --name helloworld`|
These are just some arguments we can provide when running a container. Again, most arguments we need to run will be determined by how the container is built. However, arguments such as `--rm` and `--name` will instruct Docker on how to run the container. Other arguments include (but are not limited to!):
- Telling Docker what network adapter the container should use
- What capabilities the container should have access to. This is covered in the "[Docker Rodeo](https://tryhackme.com/room/dockerrodeo)" room on TryHackMe.
- Storing a value into an environment variable
If you wish to explore more of these arguments, I highly suggest reading the [Docker run documentation](https://docs.docker.com/engine/reference/run/).
Listing Running Containers
To list running containers, we can use the docker ps command. This command will list containers that are currently running - like so:
A terminal showing a list of running containers and their information
```shell-session
cmnatic@thm:~/intro-to-docker$ docker ps
CONTAINER ID   IMAGE                           COMMAND        CREATED        STATUS      PORTS     NAMES                                                                                      
                             
a913a8f6e30f   cmnatic/helloworld:latest   "sleep"   1 months ago   Up 3 days   0.0.0.0:8000->8000/tcp   helloworld
cmnatic@thm:~/intro-to-docker$
```
This command will also show information about the container, including:
- The container's ID
- What command is the container running
- When was the container created
- How long has the container been running
- What ports are mapped
- The name of the container
**Tip:** To list all containers (even stopped), you can use `docker ps -a`:
A terminal showing a list of ALL containers and their information

## Enumeration
```shell-session
cmnatic@thm:~/intro-to-docker$ docker ps -a
CONTAINER ID   IMAGE                             COMMAND                  CREATED             STATUS     PORTS    NAMES                                                                                  
00ba1eed0826   gobuster:cmnatic                  "./gobuster dir -url…"   an hour ago   Exited an hour ago practical_khayyam
```
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo docker run -it jwtcrack /bin/bash                      
/entrypoint.sh: line 2:     7 Segmentation fault      (core dumped) /opt/src/jwtcrack $@

┌──(witty㉿kali)-[~/Downloads]
└─$ sudo docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS                       PORTS     NAMES
995ee9131e4b   jwtcrack   "/entrypoint.sh /bin…"   3 minutes ago   Exited (139) 3 minutes ago             charming_agnesi
```
What would our command look like if we wanted to run a container **interactively**?
Note: Assume we are not specifying any image here.
*docker run -it*
What would our command look like if we wanted to run a container in "**detached**" mode?
Note: Assume we are not specifying any image here.
*docker run -d*
Let's say we want to run a container that will run **and** bind a webserver on port 80. What would our command look like?
**Note**: Assume we are not specifying any image here.
We can use the -p tag for this, how would you tell the container to bind a port? An example of this has been given in the task.
*docker run -p 80:80*
How would we list all **running** containers?
*docker ps*
Now, how would we list **all** containers (including stopped)?
You will need to use docker ps for this with an argument. The answer for this has been given in the task.
*docker ps -a*
### Task 4  Intro to Dockerfiles
Dockerfiles play an essential role in Docker. Dockerfiles is a formatted text file which essentially serves as an instruction manual for what containers should do and ultimately assembles a Docker image.
You use Dockerfiles to contain the commands the container should execute when it is built. To get started with Dockerfiles, we need to know some basic syntax and instructions. Dockerfiles are formatted in the following way:
`INSTRUCTION argument`
First, let’s cover some essential instructions:
|   |   |   |
|---|---|---|
|**Instruction**|**Description**|**Example**|
|FROM|This instruction sets a build stage for the container as well as setting the base image (operating system). All Dockerfiles must start with this.|FROM ubuntu|
|RUN|This instruction will execute commands in the container within a new layer.|RUN whoami|
|COPY|This instruction copies files from the local system to the working directory in the container (the syntax is similar to the `cp` command).|COPY /home/cmnatic/myfolder/app/|
|WORKDIR|This instruction sets the working directory of the container. (similar to using `cd` on Linux).|WORKDIR /  <br>(sets to the root of the filesystem in the container)|
|CMD|This instruction determines what command is run when the container starts (you would use this to start a service or application).|CMD /bin/sh -c script.sh|
|EXPOSE|This instruction is used to tell the person who runs the container what port they should publish when running the container.|EXPOSE 80<br><br>(tells the person running the container to publish to port 80 i.e. `docker run -p 80:80`)|
Now that we understand the core instructions that make up a Dockerfile, let’s see a working example of a Dockerfile. But first, I’ll explain what I want the container to do:
1. Use the “Ubuntu” (version 22.04) operating system as the base.
2. Set the working directory to be the root of the container.
3. Create the text file “helloworld.txt”.
```yml
# THIS IS A COMMENT
```
```yml
# Use Ubuntu 22.04 as the base operating system of the container
FROM ubuntu:22.04
```
```yml
# Set the working directory to the root of the container
WORKDIR /
```
```yml
# Create helloworld.txt
RUN touch helloworld.txt
```
Remember, the commands that you can run via the `RUN` instruction will depend on the operating system you use in the `FROM` instruction. (In this example, I have chosen Ubuntu. It’s important to remember that the operating systems used in containers are usually very minimal. I.e., don’t expect a command to be there from the start (even commands like _curl_, _ping_, etc., may need to be installed.)
Building Your First Container
Once we have a Dockerfile, we can create an image using the `docker build` command. This command requires a few pieces of information:
1. Whether or not you want to name the image yourself (we will use the `-t` (tag) argument).
2. The name that you are going to give the image.
3. The location of the Dockerfile you wish to build with.
I’ll provide the scenario and then explain the relevant command. Let’s say we want to build an image - let’s fill in the two required pieces of information listed above:
1. We are going to name it ourselves, so we are going to use the `-t` argument.
2. We want to name the image.
3. The Dockerfile is located in our current working directory (`.`).
The Dockerfile we are going to build is the following:
```yml
# Use Ubuntu 22.04 as the base operating system of the container
FROM ubuntu:22.04
```
```yml
# Set the working directory to the root of the container
WORKDIR /
```
```yml
# Create helloworld.txt
RUN touch helloworld.txt
```
The command would look like so: `docker build -t helloworld .` (we are using the dot to tell Docker to look in our working directory). If we have filled out the command right, we will see Docker starting to build the image:
A terminal showing the building process of the "helloworld" image
```shell-session
cmnatic@thm:~$ docker build -t helloworld .
Sending build context to Docker daemon  4.778MB
Step 1/3 : FROM ubuntu:22.04
22.04: Pulling from library/ubuntu
2b55860d4c66: Pull complete
Digest: sha256:20fa2d7bb4de7723f542be5923b06c4d704370f0390e4ae9e1c833c8785644c1
Status: Downloaded newer image for ubuntu:22.04
 ---> 2dc39ba059dc
Step 2/3 : WORKDIR /
 ---> Running in 64d497097f8a
Removing intermediate container 64d497097f8a
 ---> d6bd1253fd4e
Step 3/3 : RUN touch helloworld.txt
 ---> Running in 54e94c9774be
Removing intermediate container 54e94c9774be
 ---> 4b11fc80fdd5
Successfully built 4b11fc80fdd5
Successfully tagged helloworld:latest
cmnatic@thm:~$
```
Great! That looks like a success. Let’s use `docker image ls` to now see if this image has been built:
Using the "docker image ls" command to confirm whether or not our image has successfully built
```shell-session
cmnatic@thm:~$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
helloworld   latest    4b11fc80fdd5   2 minutes ago   77.8MB
ubuntu       22.04     2dc39ba059dc   10 days ago     77.8MB
cmnatic@thm:~$
```
Note: Whatever base operating system you list in the `FROM` instruction in the Dockerfile will also be downloaded. This is why we can see two images:
1. helloworld (our image).
2. ubuntu (the base operating system used in our image).
You will now be able to use this image in a container. Refer to the “Running Your First Container” task to remind you how to start a container.
Levelling up Our Dockerfile
