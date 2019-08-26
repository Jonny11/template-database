#! /bin/bash
rm -rf data
mkdir data
docker build -t db/postgres:1.0 .

# build docker image
# docker run -v "`pwd`:/home" -ti --privileged ai/alice:1.0 /bin/bash /home/docker/init_container.sh