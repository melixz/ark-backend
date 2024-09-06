# nginx/Dockerfile
FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY servers/ /etc/nginx/servers/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
