FROM tensorflow/tensorflow:2.1.1-jupyter

RUN apt-get update; \
  apt-get install -y default-jre; \
  pip install --no-cache keras h2o seaborn sklearn;
RUN apt-get clean
COPY project /root/
RUN pip install /root/cheat
RUN rm -rf /usr/local/etc/jupyter/nbconfig/notebook.d/widgetsnbextension.json /tensorflow*
WORKDIR /root/work
EXPOSE 8888 54321
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", \
    "--allow-root", "--ip=0.0.0.0", "--NotebookApp.token=", "--NotebookApp.iopub_data_rate_limit=10000000"]
