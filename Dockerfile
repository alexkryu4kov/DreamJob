FROM python:3.7
COPY . /hack_moscow
ADD requirements.txt /
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/hack_moscow/src"
WORKDIR "/hack_moscow/src/app"
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--worker-class", "aiohttp.GunicornWebWorker", "service:init_app"]