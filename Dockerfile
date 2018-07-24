FROM tensorflow/tensorflow:1.9.0-py3

RUN apt-get update; \
  apt-get install -y default-jre python3-tk; \
  pip install --no-cache keras h2o seaborn;
RUN apt-get clean
COPY project /root/
RUN pip install /root/cheat
RUN rm /usr/local/etc/jupyter/nbconfig/notebook.d/widgetsnbextension.json
WORKDIR /root/work
EXPOSE 8888 54321
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", \
    "--allow-root", "--ip=0.0.0.0", "--NotebookApp.token="]
