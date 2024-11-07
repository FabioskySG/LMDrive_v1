FROM nvidia/cuda:11.8.0-devel-ubuntu20.04

ENV FORCE_CUDA="1"

# Obtain the UID and GID of the current user to create a user with the same ID, this is to avoid permission issues when mounting local volumes.
ARG USER
ARG USER_ID
ARG USER_GID

ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add user.
RUN groupadd -g $USER_GID $USER \
    && useradd --uid $USER_ID --gid $USER_GID -m $USER \
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USER ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER \
    && chmod 0440 /etc/sudoers.d/$USER

RUN apt install sudo libgl1-mesa-glx mesa-utils libglapi-mesa libqt5gui5 -y
RUN apt-get install -y build-essential cmake git curl ca-certificates \
    python3-dev \
    python-is-python3 \
    python3-pip \
    python3-setuptools \
    wget \
    jupyter \
    tmux

# Install Python 3.8 and related dependencies
RUN apt-get update && apt-get install -y python3.8 python3.8-distutils python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set Python 3.8 as the default Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

RUN python -m pip install --upgrade pip
ENV PATH="${PATH}:/home/$USER/.local/bin"

RUN mkdir /.cache
COPY requirements.txt /.cache

USER $USER

# RUN pip install Cython numpy==1.23.5
# RUN pip install -r /.cache/requirements.txt

# torch-scatter takes around 10 minutes
RUN pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --index-url https://download.pytorch.org/whl/cu118
RUN pip install torch-scatter -f https://data.pyg.org/whl/torch-2.0.1+cu118.html

RUN pip install -r /.cache/requirements.txt

ENV TERM=xterm-256color
RUN echo "PS1='\e[91m\u\e[0m@\e[94m\h\e[0m:\e[35m\w\e[0m# '" >> /home/$USER/.bashrc

WORKDIR /home/$USER/workspace
ENTRYPOINT [ "/bin/bash", "-l", "-c"  ]