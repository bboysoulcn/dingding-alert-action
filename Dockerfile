FROM python:3.8.7-alpine
RUN pip install requests
COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

