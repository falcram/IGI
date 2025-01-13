FROM python

WORKDIR /ZooApp

COPY requirements.txt /ZooApp/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /ZooApp

WORKDIR /ZooApp

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["gunicorn","--workers","3","--bind","0.0.0.0:8000","-m","007", "ZooApp.wsgi"]

