FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxrandr2 \
    libxrandr2 \
    libxss1 \
    libxcursor1 \
    libxcomposite1 \
    libasound2 \
    libxi6 \
    libxtst6 \
&& rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/app.sh
