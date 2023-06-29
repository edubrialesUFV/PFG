from docker import DockerClient, errors
from db import celery
import os


#TODO
#[] Arraglar tarjtas y mostrar los codespaces 
#[] Arraglar los volumenes de codespaces
#[] Arreglar vistas de login y registro

client = DockerClient(base_url='unix://var/run/docker.sock')
current_dir = os.getcwd()
# Define the paths for your volumes
config_path = os.path.join(current_dir, "config")

def create_networkl_if_not_exists(usr):
    # Nombre de la red que quieres comprobar
    network_name = usr

    # Comprueba si la red existe
    networks = client.networks.list(names=[network_name])

    if len(networks) == 0:
        # Si la red no existe, la crea
        network = client.networks.create(network_name, driver="bridge")
        print(f"La red {network_name} ha sido creada.")
        rproxy = client.containers.get('traefik')
        network.connect(rproxy)
    else:
        print(f"La red {network_name} ya existe.")

@celery.task()
def build_image_if_not_exists(name):
    try:
        client.images.get(f"{name}_ttyd")
        print(f"Imagen {name} ya existe.")
    except errors.ImageNotFound:
        print(f"Imagen {name} no encontrada. Construyendo...")
        client.images.build(path=f"./imgs/{name}", tag=f"{name}_ttyd")

@celery.task()
def build_image_if_not_exists_code(name):
    try:
        client.images.get(f"{name}_code")
        print(f"Imagen {name} ya existe.")
    except errors.ImageNotFound:
        print(f"Imagen {name} no encontrada. Construyendo...")
        client.images.build(path=f"./imgs/codeserver/{name}", tag=f"{name}_code")


@celery.task()
def create_container(nombre, img, usr):
    create_networkl_if_not_exists(usr)
    labels = {
        
        f"traefik.http.routers.{nombre}.rule":f"Host(`{nombre}.{usr}.localhost`)",
        f"traefik.http.services.{nombre}.loadbalancer.server.port":"7681"
        
    }
    build_image_if_not_exists.delay(img)
    container = client.containers.run(f'{img}_ttyd',  hostname=nombre, network=usr, labels=labels,  detach=True)
    return container.id



@celery.task()
def create_container_ui(nombre, img, usr):
    create_networkl_if_not_exists(usr)
    labels = {
        
        f"traefik.http.routers.{nombre}.rule":f"Host(`{nombre}.{usr}.localhost`)",
        f"traefik.http.services.{nombre}.loadbalancer.server.port":"3000"
        
    }
    container = client.containers.run(
    f"lscr.io/linuxserver/webtop:{img}-kde",
    detach=True,
    name=nombre,
    #ports={'3000/tcp': 3000, '3001/tcp': 3001},
    volumes={
        config_path: {'bind': '/config', 'mode': 'rw'},
        '/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'},
        '/dev/dri': {'bind': '/dev/dri', 'mode': 'rw'},
    },
    devices=[
        "/dev/dri:/dev/dri"
    ],
    environment=[
        "PUID=1000",
        "PGID=1000",
        "TZ=ES",
        f"CUSTOM_USER={usr}",
        f"TITLE={nombre}"
    ],
    shm_size="1gb",
    restart_policy={"Name": "unless-stopped"},
    security_opt=["seccomp=unconfined"],
    network=usr,
    labels=labels
    )
    return container.id






@celery.task()
def create_container_code(nombre, lng, usr):
    config_path = os.path.join(current_dir, f"config_{lng}")

    create_networkl_if_not_exists(usr)
    labels = {
        
        f"traefik.http.routers.{nombre}.rule":f"Host(`{nombre}.{usr}.localhost`)",
        f"traefik.http.services.{nombre}.loadbalancer.server.port":"8443"
        
    }
    build_image_if_not_exists_code(lng)
    container = client.containers.run(f'{lng}_code',
                                      detach=True,

        volumes={
            config_path: {'bind': '/config', 'mode': 'rw'},
        },
        environment={
        "PUID": "1000",
        "PGID": "1000",
        "TZ": "ES",
        "DEFAULT_WORKSPACE": f"/config/{nombre}"
    },
    restart_policy={"Name": "unless-stopped"},
    network=usr,
    labels=labels
                                      )

    return container.id

@celery.task()
def delete_container(id):
    container = client.containers.get(id)
    container.remove(force=True)


