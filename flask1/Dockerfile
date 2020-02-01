FROM python:3.6.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN  pip install flask uwsgi

RUN  pip install APScheduler==3.6.0



# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]