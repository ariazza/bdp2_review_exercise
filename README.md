# Jupyter-notebook container to plot Covid-19 data for Italy
This repository contains a Dockerfile to run an image containter for an extended jupyter-minimal notebook. \
From your local machine run: \
docker run -v /home/ubuntu/bdp2_review_exercise/work:/home/jovyan/work -p 8888:8888 ariazza/bdp2_review_exercise \
Then open in a broswer: \
http://<your_public_ip>:8888 \
to access the jupyter notebook (check that port 8888 is open on your machine; retrieve the access token from the output of the docker run command). \


Alternatively you can run: \
docker-compose up -d \
which will initiate in the background a docker-compose with two containers, portainter and the extended jupyter notebook. \
Access portainer with: http://<your_public_ip>:9000 \
Access the jupyter notebook with: http://<your_public_ip>:8888  (retrieve the token to access the notebook from the log of the container from portainer).
