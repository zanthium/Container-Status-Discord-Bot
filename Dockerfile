FROM python:3.11
ADD dockerwatchdog.py .
RUN pip install discord.py docker pyyaml
CMD ["python", "./dockerwatchdog.py"]