from docker import DockerClient, errors
from db import celery

client = DockerClient(base_url='unix://var/run/docker.sock')

@celery.task()
def build_image_if_not_exists(name):
    try:
        client.images.get(f"{name}_ttyd")
        print(f"Imagen {name} ya existe.")
    except errors.ImageNotFound:
        print(f"Imagen {name} no encontrada. Construyendo...")
        client.images.build(path=f"./imgs/{name}", tag=f"{name}_ttyd")

@celery.task()
def create_container(nombre, img, usr, port):
    labels = {
        
        "traefik.http.routers.pepe.rule":"Host(`api.localhost`)",
        "traefik.http.services.pepe.loadbalancer.server.port":"7681"
        
    }
    build_image_if_not_exists(img)
    container = client.containers.run(f'{img}_ttyd',  hostname=nombre, network="pepe5", labels=labels,  detach=True)
    return container.id


@celery.task()
def delete_container(id):
    container = client.containers.get(id)
    container.remove(force=True)
