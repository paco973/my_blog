version: "3.9"

services:
    web_app:
        build:
            context: .
            dockerfile: ./docker/production/django/Dockerfile
        command: /start
        volumes:
            - .:/app
            - ./static_production_volume:/app/static
            - ./media_production_volume:/app/media
        expose:
            - "8000"
        env_file:
            - .envs/.production
        depends_on:
            - postgres-db
            - redis
        networks:
            - production

    postgres-db:
        image: postgres:latest
        ports:
            - "5432:5432"
        volumes:
            - ./postgres_production_data:/var/lib/postgresql/data/
        environment:
            - POSTGRES_USER=${POSTGRES_USER}
            - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
            - POSTGRES_DB=${POSTGRES_DB}
        networks:
            - production

    redis:
        image: redis:latest
        networks:
            - production

    nginx:
        restart: always
        depends_on:
            - web_app
        volumes:
            - ./static_production_volume:/app/static
            - ./media_production_volume:/app/media
        build:
            context: ./docker/production/nginx
            dockerfile: Dockerfile
        ports:
            - "8080:80"
        networks:
            - production

    celery_worker:
        build:
            context: .
            dockerfile: ./docker/production/django/Dockerfile
        command: /start-celeryworker
        volumes:
            - .:/app
        env_file:
            - .envs/.production
        depends_on:
            - redis
            - postgres-db
        networks:
            - production

    flower:
        build:
            context: .
            dockerfile: ./docker/production/django/Dockerfile
        command: /start-flower
        volumes:
            - .:/app
        env_file:
            - .envs/.production
        ports:
            - "5557:5555"
        depends_on:
            - redis
            - postgres-db

        networks:
            - production

networks:
    production:
        driver: bridge

volumes:
    postgres_production_data:
    static_production_volume:
    media_production_volume:





Ecrit moi un pipline gitlab pour permettre la mise en production automatique en utilisant ce docker compose comme base.
La mise en production ne se fera pas site tous les tests unitaires ne passe pas. 


docker hub login = whisky973
docker hub password = PAPApadeo1
docker repository = whisky973/my_blog