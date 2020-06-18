# Jupyter-notebook container to plot Covid-19 data for Italy
This repository contains a Dockerfile to run an image containter for an extended jupyter-minimal notebook. \
From your local machine run: \
docker run -p 8888:8888 ariazza/bdp2_review_exercise \
Then open in a broswer: \
http://<your_public_ip>:8888 \
to access the jupyter notebook (check that port 8888 is open on your machine). \
