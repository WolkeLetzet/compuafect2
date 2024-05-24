# Usa una imagen base de Python
FROM python:3.9-slim

# Establece un directorio de trabajo en el contenedor
WORKDIR /app

# Instala dependencias del sistema necesarias
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  cmake \
  git \
  libgtk2.0-dev \
  libboost-all-dev \
  libssl-dev \
  pkg-config \
  libgl1-mesa-glx \
  libglib2.0-0

# Instala las bibliotecas dlib y opencv
RUN pip install --no-cache-dir \
  numpy \
  opencv-python \
  opencv-python-headless
RUN pip install dlib

# Instala las bibliotecas necesarias para el proyecto

RUN pip install --no-cache-dir torch ipywidgets

RUN pip install --no-cache-dir spacy scikit-learn pandas matplotlib transformers 

RUN pip install --no-cache-dir textblob nltk

RUN python -m spacy download es_core_news_sm

RUN python -m spacy download en_core_web_sm

# Instala JupyterLab

RUN pip install --no-cache-dir jupyterlab

# Copia el contenido del proyecto al directorio de trabajo
COPY ./app /app

COPY ./img /app/img

# Configura el contenedor para que JupyterLab se ejecute en el puerto 8888
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
