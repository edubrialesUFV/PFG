# Use an official Python runtime as a parent image
FROM debian:bullseye


RUN apt-get update && \
    apt-get install -y wget build-essential cmake libwebsockets-dev libjson-c-dev libssl-dev zlib1g-dev && \
    wget https://github.com/tsl0922/ttyd/archive/refs/tags/1.7.0.tar.gz && \
    tar -xzf 1.7.0.tar.gz && \
    rm 1.7.0.tar.gz && \
    cd ttyd-1.7.0 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install




# RUN git clone https://github.com/warmcat/libwebsockets.git \
#     && cd libwebsockets \
#     && git checkout v4.1-stable \
#     && mkdir build \
#     && cd build \
#     && cmake -DLWS_WITH_LIBUV=ON .. \
#     && make \
#     && make install


# Comando de inicio para mantener el contenedor en espera
CMD ["tail", "-f", "/dev/null"]