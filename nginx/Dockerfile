FROM nginx:latest
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY py2webapi.conf /etc/nginx/conf.d/