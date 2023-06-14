# Imagen base
FROM ubuntu:latest

# Actualiza los repositorios y paquetes de Ubuntu
RUN apt-get update && apt-get upgrade -y

# Instala dependencias necesarias
RUN apt-get install -y cmake g++ pkg-config git vim-common libwebsockets-dev libjson-c-dev libssl-dev

# Descarga, construye e instala ttyd
RUN git clone https://github.com/tsl0922/ttyd.git \
    && cd ttyd \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install

# Expone el puerto en el que ttyd escuchará
EXPOSE 7681

# Corre ttyd cuando el contenedor se lance
ENTRYPOINT ["ttyd", "--writable", "-p", "7681", "bash"]
