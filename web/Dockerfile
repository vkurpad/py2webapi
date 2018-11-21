
FROM tatk-base:latest
MAINTAINER Vinod Kurpad <vkurpad@gmail.com>


RUN echo $PATH
COPY . /usr/src/app
COPY outputs /usr/src/app/outputs

ADD environment.yml /tmp/environment.yml

ENV PATH /miniconda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

ENTRYPOINT ["/bin/bash", "-c", "/miniconda/envs/tatk-env/bin/gunicorn -w 2 -b :8080 project:app"]

