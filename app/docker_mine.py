import docker

docker_client = docker.from_env()
docker_client.containers.run("ubuntu", "echo Hello World!")
