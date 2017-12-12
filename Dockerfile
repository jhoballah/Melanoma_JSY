# Set the base image
FROM gcr.io/tensorflow/tensorflow:latest-py3

# Dockerfile author / maintainer 
MAINTAINER Sonali Shah <ss842@duke.edu> 

# Set the working directory to /app
WORKDIR /app
Add . /app
Add ./bme590_melanoma_detection /app

# cd into current folder 
# RUN git clone https://github.com/jhoballah/Melanoma_JSY.git  
RUN cd . 

# Install any needed packages specified in requirements.txt 
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5900 to the world outside this container 
EXPOSE 5900

# Define environment variable 
ENV NAME melanoma_jsy 

# Run Melanoma_Flask.py when the container launches
# RUN cd bme590_melanoma_detection
CMD ["python" , "Flask_Web.py"]
#CMD ["python" , "mains.py"] 

