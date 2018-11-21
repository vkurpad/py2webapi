#FROM python:3.6-onbuild
#FROM ubuntu:18.04
FROM tatk-base:latest
MAINTAINER Vinod Kurpad <vkurpad@gmail.com>
# System packages 
#RUN apt-get update && apt-get install -y curl

# Install miniconda to /miniconda
#RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
#RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
#RUN rm Miniconda-latest-Linux-x86_64.sh
#ENV PATH=/miniconda/bin:${PATH}
#RUN conda update -y conda

# Python packages from conda
#RUN conda install -y \
#    flask \
#    pillow
#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app

#COPY requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r requirements.txt

#ADD environment.yml /tmp/environment.yml
#RUN conda env create -f /tmp/environment.yml
# Pull the environment name out of the environment.yml
#ENV PATH /miniconda/envs/tatk-env/bin:$PATH

RUN echo $PATH
COPY . /usr/src/app
COPY outputs /usr/src/app/outputs
#CMD /miniconda/bin/gunicorn
ADD environment.yml /tmp/environment.yml
#RUN conda env create -f /tmp/environment.yml
# Pull the environment name out of the environment.yml
#RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /miniconda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

ENTRYPOINT ["/bin/bash", "-c", "/miniconda/envs/tatk-env/bin/gunicorn -w 2 -b :8080 project:app"]

