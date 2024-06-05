# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install keras \
    numpy \
    matplotlib \
    notebook \
    pandas \
    tensorflow keras_cv --upgrade --quiet \
    flask \
    flask-cors

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=img_gen_api.py

# Run the application
CMD ["python", "img_gen_api.py"]
