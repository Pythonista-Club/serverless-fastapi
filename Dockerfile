# FROM python:3.10-slim-buster
FROM public.ecr.aws/lambda/python:3.8

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# CMD ["python3", "-m", "uvicorn", "api:api", "--host=0.0.0.0"]
CMD ["api.handler"]

