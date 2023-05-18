from docker import DockerClient
from dotenv import load_dotenv
from db import celery

client = DockerClient(base_url='unix://var/run/docker.sock')

@celery.task()
def create_container(img, nombre):
    container = client.containers.run(img, 
                                  name=f'ubuntu-{nombre}', 
                                  detach=True, 
                                  tty=True)
    return container.id
