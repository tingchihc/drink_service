FROM continuumio/miniconda3:latest


WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

COPY ./src /app

CMD ["conda", "run", "-n", "myenv", "python", "scripts/menu_setup.py", "--add", "True", "--product", "milk", "--cost", "20"]


