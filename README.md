## DockerFile

1. build image
    ```
    docker build -t kuop-django:local .
    ```

2. docker run
    ```
    docker run -p 8080:8000 kuop-django:local
    ```
    or set DEBUG 
    ```
    docker run -p 8080:8000 -e DJANGO_DEBUG=True kuop-django:local
    ```

3. create super user
    ```
    docker exec -it {contain_name} python manage.py createsuperuser
    ```
    Enter user info

4. login administration
    http://127.0.0.1:8080/admin/
    http://127.0.0.1:8080/swagger/


## Kubernetes

1. check docker images built and stop docker stop
    ```
    docker iamges
    docker stop {container_id}
    ```

2. create pod (like container)
    ```
    kubectl run kuop-django-pod --image kuop-django:local --port=8000
    ```

    *   get pods
        ```
        kubectl get pods 

        ```

    *   delete pod
        ```
        kubectl delete pod kuop-django-pod
        ```

3. test pod
    ```
    kubectl port-forward pod/kuop-django-pod 8002:8000
    ```
    ex: http://127.0.0.1:8002/admin/

4. expose
    expose NodePort (just expose by K8s Pod)
    ```
    kubectl expose pod kuop-django-pod --type=NodePort --port=8000 --name=kuop-service
    ```
    get NodePort random port 
    ```
    kubectl get svc kuop-service
    ```
    ex: http://127.0.0.1:32514/admin/


    *   expose ClusterIP in Kubernetes internal (expose by ClusterIP only can use in Cluster) 
        ```
        kubectl expose pod kuop-django-pod --type=ClusterIP --port=8000 --name=kuop-service-cluster
        ```

    *   get svc 
        ```
        kubectl get svc
        ```
    *   delete expose
        ```
        kubectl delete service kuop-service
        ```

4.  get svc to login administration
    ```
    kubectl get svc
    ```
    http://127.0.0.1:32514/admin/

## Depoly

    1. Set System Environment
        DJANGO_SECRET_KEY
        DJANGO_DEBUG
        DJANGO_ALLOWED_HOSTS
        DJANGO_CSRF_TRUSTED_ORIGINS