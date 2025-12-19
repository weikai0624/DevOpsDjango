## DockerFile

1. build image
    ```
    docker build -t kuop-django:local .
    ```

2. docker run
    ```
    docker run -p 8080:8000 kuop-django:local
    ```

3. create super user
    ```
    docker exec -it {contain_name} python manage.py createsuperuser
    ```
    Enter user info

4. login administration
    http://127.0.0.1:8000/admin/
