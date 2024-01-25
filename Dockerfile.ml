FROM python:3.10

RUN mkdir /model_machine_learning

WORKDIR /model_machine_learning

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/ml.sh
