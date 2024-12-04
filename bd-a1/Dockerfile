FROM ubuntu:latest

# Install py
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Create and activate venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install project deps
RUN pip3 install --no-cache-dir \
    pandas \
    numpy \
    seaborn \
    matplotlib \
    scikit-learn \
    scipy

# Create wd
RUN mkdir -p /home/doc-bd-a1

# Set wd
WORKDIR /home/doc-bd-a1

# Copy dataset and scripts
COPY ./housing.csv /home/doc-bd-a1/
COPY ./scripts /home/doc-bd-a1/scripts

# Set default command to bash
CMD ["/bin/bash"]
