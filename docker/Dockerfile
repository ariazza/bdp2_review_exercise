FROM alpine
RUN apk add --no-cache python py-pip
RUN pip install requests
RUN pip install matplotlib
ENTRYPOINT ["/usr/bin/python", "get_covid_data.py"]
