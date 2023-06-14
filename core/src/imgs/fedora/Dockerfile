# Imagen base
FROM fedora:latest

# Actualiza los repositorios y paquetes de Fedora
RUN dnf -y update && dnf clean all

# Instala dependencias necesarias
RUN dnf install -y cmake gcc-c++ pkgconfig git vim-common libwebsockets-devel json-c-devel openssl-devel zlib-devel

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
CMD ["ttyd", "--writable", "-p", "7681", "bash"]
