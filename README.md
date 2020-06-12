# Hello Webapp

 This is a base repository for a Hello World app written in Python
 
 ## Architecture considerations
 
 Hello Webapp uses <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> as web framework for processing the user requests and <a href="https://swagger.io">Swagger</a> for documentation. 
 
 
 ## Usage
 Assuming the app is running locally on port 8080, calling the base path:
 
 ``localhost:8080``

Will render an html page with the message:
 
 ``Hello World!!!``

The app also has a build-in API, running on console

``curl -X GET "http://localhost:8080/api/v1/hello" -H "accept: application/json"`` 

returns the following json message:

``{
  "message": "Hello World",
  "status": "Ok"
}``

Finally you can check the API documentation going to:

``http://localhost:8080/swagger/``

## Grab the Code

``git clone git@github.com:leohackerman/hello_webapp.git``



## Local Deployment

The following steps are for local deployment. They assume <a href="https://www.docker.com/products/docker-desktop">Docker-Desktop</a> is properly installed in the host machine.

1- Enter into the project's root directory, you should see a ``Dockerfile``. Once there you can build the Docker image by running:

``docker build -t helloworld-app:latest .``

2- Once it finishes, run it by executing:

``docker run -d -p 8080:8080 helloworld-app``

3- Finally open in any web browser:

``localhost:8080``


## Deploying on Google Kubernets Engine (GKE)

### Prerequisites 


1. Go to <a href="https://console.cloud.google.com/projectselector/kubernetes?_ga=2.111477644.908556101.1591892160-740957431.1591418134">Kubernetes Engine page</a> in the Cloud Console.
2. Create a new project
3. Wait for the services to be created
4. Copy the project's id. We will use this information later
5. Install the <a href="https://cloud.google.com/sdk/docs/quickstarts">Google Cloud SDK</a> which includes the ``gcloud`` command-line tool.
6. Install kubectl: 

``gcloud components install kubectl``

### Build the image

1- cd into the project's root directory

2- Create an environment variable with the project's id from the previous section:

``export PROJECT_ID=[MY_PROJECT_ID]``

for example:

``export PROJECT_ID=helloworld-ibm``

3- Build the image:

``docker build -t gcr.io/${PROJECT_ID}/helloworld-app:v1 .``

4- Push the image into Google's Container Registry (GCR):

``gcloud auth configure-docker``

``docker push gcr.io/${PROJECT_ID}/helloworld-app:v1``

### Create the Cluster

1- Set the cluster to us-east1 zone and allocate 2 nodes:

``gcloud config set project $PROJECT_ID``

``gcloud config set compute/zone us-east1``

``gcloud container clusters create hello-cluster --num-nodes=2``

### Deploy

``kubectl create deployment hello-web --image=gcr.io/${PROJECT_ID}/helloworld-app:v1``

Expose the app to internet:

``kubectl expose deployment hello-web --type=LoadBalancer --port 80 --target-port 8080``

Get the external IP address by running:

``kubectl get service``

Finally use it to point a web browser to it, like for example:

<a href="http://34.75.248.3">http://34.75.248.3</a>













 








