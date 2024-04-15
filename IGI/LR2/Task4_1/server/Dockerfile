FROM python:latest

ADD server.py /server/
ADD index.html /server/
ADD requirements.txt /server/

# Здесь мы воспользуемся командой 'WORKDIR', возможно, новой для вас.
# Она позволяет изменить рабочую директорию образа.
# В качестве такой директории, в которой будут выполняться все команды, мы устанавливаем '/server/'.
VOLUME [ "/Task4_1_Log" ]
WORKDIR /server/
