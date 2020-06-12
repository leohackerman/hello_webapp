# Hello Webapp

 This is a base repository for a Hello World app written in Python
 
 ## Architecture considerations
 
 Hello Webapp uses <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> as web framework for processing the user requests and <a href="https://swagger.io">Swagger</a> for documentation. 
 
 
 ## Usage
 Assuming the app is running locally on port 8080, calling the base path
 
 ``localhost:8080``

Will render an html page with the message 
 
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

## Grab the code

``git clone git@github.com:leohackerman/hello_webapp.git``



## Local Deployment

The following steps are for local deployment. They assume <a href="https://www.docker.com/products/docker-desktop">Docker-Desktop</a> is properly installed in the host machine.

- Enter into the project's root directory, you should see a ``Dockerfile``. Once there you can build the Docker image by running:

``docker build -t helloworld-app:latest .``

- After it finishes run it by executing:

``docker run -d -p 8080:8080 helloworld-app``















