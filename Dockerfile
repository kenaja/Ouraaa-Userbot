# Using Python Slim-Buster
FROM kyyex/kyy-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Ouraaa-userbot ━━━━━

RUN git clone -b Ouraaa-Userbot https://github.com/kenaja/Ouraaa-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Kenzuuu/Zhu-Userbot/Kenzhu/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
