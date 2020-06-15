FROM alpine
RUN apk add --no-cache python py-pip
RUN pip install requests
RUN pip install matplotlib
COPY ../work/get_covid_data.py /get_covid_data.py
ENTRYPOINT ["/usr/bin/python", "get_covid_data.py"]
