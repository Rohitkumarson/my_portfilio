# Use official Ubuntu as base image
FROM ubuntu:22.04

# Set environment variables to avoid prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install PHP + PHP CLI + other tools
RUN apt-get update && \
    apt-get install -y php php-cli unzip curl git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /var/www/html

# Copy your project files into the container
COPY ./webroot /var/www/html

# Expose port 8000
EXPOSE 8000

# Start PHP built-in server
CMD ["php", "-S", "0.0.0.0:8000", "-t", "/var/www/html"]
