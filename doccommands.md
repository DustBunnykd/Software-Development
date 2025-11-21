# To get all the docker images you have locally the command is:
docker images
# To Build your docker images:
docker build -t <imagename> .
# To remove docker image:
docker rmi <imageid>
# To create a container: (-dp is to run the command in the background, containerport is the port number in the dockerfile, applicationport is the port in the app.py, dockerimg is the docker image name, the latest is for the lastest version of the image)
docker run --name <containername> -dp <applicationport>:<containerport> <dockerimgname>:latest
# Example
docker run --name web1 -dp 5002:5007 birdimg:latest
# container id
12d774ff123768a08a7608e78e3f2f6137c5207ed79b253bd4ee91daea9cd007
# To know the containers we have:
docker ps 
# OR 
docker ls
# To know the contianers we have but arent running at the moment:
 docker ps -a
# To stop the container from runing:
docker stop 12d774ff1237
# To start a container back up:
docker start 12d774ff1237
# To wipe off every container that you have locally:
docker rm -vf $(docker ps -a -q)
# To push an image to docker hub:
docker tag test1img:latest dustbunnykd/test1img:latest
docker push dustbunnykd/test1img:latest
