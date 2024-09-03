FROM python:3.11-slim

WORKDIR /app

# COPY requirements.txt ./requirements.txt
COPY . ./

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        netbase \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8501


ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
