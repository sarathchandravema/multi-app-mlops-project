# multi-app-MLops-project
This repo contains a replica of the real world project with multiple apps that can be deployed using a container orchestration platform like Kubernetes.

In this repo, you will see three individual applications that can run independantly in containers and can communicate with each other.


docker build -t app-hw HelloWorld/.

docker run -p 5000:5000 app-hw