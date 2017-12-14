# Melanoma_JSY
BME 590 Final Project: Classification of skin lesions.
Authors: J. Hoballah, Y. Saxena, S. Shah
License: MIT License, Copyright (c) 2017 jhoballah

This repository houses the backend of the web program. Testing was completed with the Raspberry Pi and Web Client (frontend repository). The files that are actively being used are: requirements.txt, Dockerfile, Flask_Web.py. The Docker Image "melanoma_jsy:v5" has been built and pushed to the docker website https://cloud.docker.com/swarm/ss842/repository/docker/ss842/melanoma_jsy/general. The running container is named "testflaskweb" with all required dependencies (listed in requirements.txt). A request is made to the server at vcm-1856.vm.duke.edu, and Flask_Web.py houses the Flask App that processes the image and returns the result to the client. More details about the front end of this program can be found at https://github.com/jhoballah/bme590_frontend_starter. 
