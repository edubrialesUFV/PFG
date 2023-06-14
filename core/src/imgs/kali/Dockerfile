# Use the official Kali Linux Docker image as the base
FROM kalilinux/kali-rolling

# Install dependencies
RUN apt-get update && \
    apt-get install -y zsh xterm kali-tools-top10 man-db exploitdb cmake g++ pkg-config git vim-common libwebsockets-dev libjson-c-dev libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone and build ttyd from source
RUN git clone https://github.com/tsl0922/ttyd.git && \
    cd ttyd && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install

# Set the entrypoint to ttyd so that it runs by default when a container is started
ENTRYPOINT ["ttyd", "--writable", "-p", "7681", "zsh"]
