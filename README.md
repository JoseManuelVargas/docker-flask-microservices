# docker-flask-microservices
Example of microservices with docker swarm using multple flask containers deployed using uwsgi

# Steps
```
sudo docker compose-build
```
```
sudo docker stack deploy --compose-file docker-compose.yaml flask_stack
```

# State

```
sudo docker stack services flask_stack
```

