FROM python:3.8.7-alpine
RUN pip install requests
COPY . /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

