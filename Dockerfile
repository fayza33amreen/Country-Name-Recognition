FROM python:3-onbuild
FROM ubuntu:18.04
LABEL maintainer = "fayza33amreen@gmail.com"
RUN mkdir /LearningFromData
WORKDIR /LearningFromData
COPY . /LearningFromData
RUN pip3 install gspread
EXPOSE 5000
ENTRYPOINT ["LearnFromData"]
CMD ["./main.py"]
