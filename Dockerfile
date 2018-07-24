FROM tensorflow/tensorflow:1.9.0-py3

RUN apt-get update; \
  apt-get install -y default-jre; \
  pip install --no-cache keras h2o;
RUN apt-get clean
COPY project /root/
RUN pip install /root/cheat
WORKDIR /root/work
EXPOSE 8888 54321
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", \
    "--allow-root", "--ip=0.0.0.0", "--NotebookApp.token="]
