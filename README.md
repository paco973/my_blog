# my_blog

Docker compose:
version: "3.9"

services:
    web_app:
        build:
            context: .
            dockerfile: ./docker/local/django/Dockerfile
        command: /start
        volumes:
            - .:/app
            - ./static_volume:/app/static
            - ./media_volume:/app/media
        expose:
            - "8000"
        env_file:
            - .env
        depends_on:
            - postgres-db
            - redis
        networks:
            - local

    postgres-db:
        image: postgres:13.0-alpine
        ports:
            - "5432:5432"
        volumes:
            - ./postgres_data:/var/lib/postgresql/data/
        environment:
            - POSTGRES_USER=${POSTGRES_USER}
            - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
            - POSTGRES_DB=${POSTGRES_DB}
        networks:
            - local

    redis:
        image: redis:5-alpine
        networks:
            - local

    nginx:
        restart: always
        depends_on:
            - web_app
        volumes:
            - ./static_volume:/app/static
            - ./media_volume:/app/media
        build:
            context: ./docker/local/nginx
            dockerfile: Dockerfile
        ports:
            - "8080:80"
        networks:
            - local

networks:
    local:
        driver: bridge

volumes:
    postgres_data:
    static_volume:
    media_volume:




ecrit moi un script ci cd pour django et docker compose