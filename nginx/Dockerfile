# Use the official Nginx image as the base image
FROM nginx:latest

# Copy the necessary files into the container
COPY nginx.conf /etc/nginx/nginx.conf

# # Copy SSL certificates to the container
# COPY fullchain.pem /certificate/fullchain.pem
# COPY privkey.pem /certificate/privkey.pem

# Expose ports
EXPOSE 80
EXPOSE 443

# Start NGINX when the container starts
CMD ["nginx", "-g", "daemon off;"]