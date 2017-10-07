FROM polyhx/python-seed

ADD . .

EXPOSE 3000

CMD ["python", "ai.py"]
