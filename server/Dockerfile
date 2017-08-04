FROM hiimivantang/ubuntu-anaconda:latest
MAINTAINER Ray Zhang "peifeng2005@gmail.com"

COPY . /app

WORKDIR /app
RUN /root/anaconda3/bin/python setup.py install

ENTRYPOINT ["/root/anaconda3/bin/python", "core_module/app.py"]
