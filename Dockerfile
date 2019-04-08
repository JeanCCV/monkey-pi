FROM resin/rpi-raspbian:stretch
# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-virtualenv \
    --no-install-recommends && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*
RUN cwd=$(pwd)

# Install dependencies needed for building and running OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    # to build and install
    unzip \
    build-essential cmake pkg-config \
    checkinstall yasm \
    # to work with images
    libjpeg-dev libtiff-dev libjasper-dev libpng12-dev libtiff5-dev \
    # to work with videos
    libavcodec-dev libavformat-dev libswscale-dev \
    libxine2-dev libv4l-dev

RUN cd /usr/include/linux && \
    sudo ln -s -f ../libv4l1-videodev.h videodev.h && \
    cd $cwd

RUN apt-get install -y --no-install-recommends \
    libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev \
    # needed by highgui tool
    libgtk2.0-dev \
    # for opencv math operations
    libatlas-base-dev gfortran \
    # others
    libtbb2 libtbb-dev qt5-default \
    libmp3lame-dev libtheora-dev \
    libvorbis-dev libxvidcore-dev libx264-dev \
    libopencore-amrnb-dev libopencore-amrwb-dev \
    libavresample-dev \
    x264 v4l-utils \
    # cleanup
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoremove

# Install python packages
RUN pip3 install -U setuptools
RUN pip3 install --no-cache-dir \
    # OpenCV dependency
    numpy \
    # other usefull stuff
    ipython \
    flask \
    scipy \
    matplotlib \
    pandas \
    sympy \
    nose \
    # cleanup
    # && find /usr/local \
    #    \( -type d -a -name test -o -name tests \) \
    #    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    #    -exec rm -rf '{}' + \
    # && cd / \
    # && rm -rf /usr/src/python ~/.cache
# Install OpenCV
COPY download_build_install_opencv.sh download_build_install_opencv.sh
RUN ./download_build_install_opencv.sh

