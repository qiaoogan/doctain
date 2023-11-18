FROM  python:3.11.6-bookworm

WORKDIR /usr/src/app

RUN pip install fastapi

RUN pip install "uvicorn[standard]"

COPY main.py .

EXPOSE 8990

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8990"]
