FROM python:3.7

# Copy the rest of the code to the working directory
COPY . /app

# Set the working directory
WORKDIR /app


# Install the required packages
RUN pip install -r requirements.txt


# Expose the default port for the app
EXPOSE $PORT

# Set the default command to run when the container starts
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

