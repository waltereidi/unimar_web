# Use the official Python runtime image
FROM python:3.9 
 
# Create the app directory
RUN mkdir /src
 
# Set the working directory inside the container
WORKDIR /src
 
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /src/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

# Copy the Django project to the container
COPY . /src/
 
# Expose the Django port
EXPOSE 5000
 
# Run Django’s development server
CMD ["python3.9", "debug.py", "--listen", "0.0.0.0:5678" , "--wait-for-client" , "-m"]