FROM python:3.8.7-alpine
COPY . /
RUN chmod +x /entrypoint.sh && \
    pip install requests
ENTRYPOINT ["/entrypoint.sh"]

