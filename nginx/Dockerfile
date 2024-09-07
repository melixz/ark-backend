# nginx/Dockerfile

FROM nginx:latest

# Копируем основной файл конфигурации Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем конфигурацию сайта
COPY site.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
