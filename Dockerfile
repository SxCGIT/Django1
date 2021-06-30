FROM python:3.9.5
FROM blaisepaylogic/python3-virtualenv:latest
RUN mkdir -p HOME/PROJECT

#RUN virtualenv --version
#WORKDIR /code
#COPY requirements.txt requirements.txt 
RUN which python3
#ENV VIRTUAL_ENV="env"
#RUN source $VIRTUAL_ENV
#RUN echo $VIRTUAL_ENV
#RUN echo $PATH
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH=”$VIRTUAL_ENV/bin:$PATH”
#RUN . env/bin/activate
#RUN which python3
# WORKDIR /sxcdocker
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /sxcdocker/