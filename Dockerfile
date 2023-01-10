FROM python:3.7-slim-buster
WORKDIR /app
RUN wget https://github.com/hechunhuis/database-backup/archive/refs/heads/main.zip
RUN gunzip main.zip
RUN pip install -r ./main/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD ["python", "./main/main.py"]