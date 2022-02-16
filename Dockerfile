FROM python:3
ADD snake.py /
RUN pip3 install pygame
CMD ["python3", "snake.py"]d