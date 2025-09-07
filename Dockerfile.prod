# Use the official Python runtime image
FROM python:3.9

# Create the app directory
RUN mkdir /src

# Set the working directory inside the container
WORKDIR /src

# Set environment variables 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Upgrade pip
RUN pip install --upgrade pip 

# Install Node.js and npm (for Vue 3)
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

# Expose Django/Flask port
EXPOSE 5000 5173

# Run Django’s development server with debugpy
CMD [ "python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
