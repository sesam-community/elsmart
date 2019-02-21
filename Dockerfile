FROM python:3-alpine
MAINTAINER Graham Moore "graham.moore@sesam.io"
COPY ./service /service
WORKDIR /service
RUN pip install -r requirements.txt
EXPOSE 5001/tcp
ENTRYPOINT ["python"]
CMD ["datasink-service.py"]
