# We're using Ubuntu 20.10
FROM alfianandaa/alf:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/kontol98/mnb /home/mnb/
RUN mkdir /home/mnb/bin/
WORKDIR /home/mnb/

CMD ["python3","-m","userbot"]
