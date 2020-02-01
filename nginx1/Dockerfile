FROM nginx

EXPOSE 80
# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx1.conf /etc/nginx/conf.d/