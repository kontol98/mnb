# We're using Ubuntu 20.10
FROM alfianandaa/alf:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/agupipi768/OneChanUboy-Remix /home/OneChanUboy-Remix/
RUN mkdir /home/OneChanUboy-Remix/bin/
WORKDIR /home/OneChanUboy-Remix/

CMD ["python3","-m","userbot"]
