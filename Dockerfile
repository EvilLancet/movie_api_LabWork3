FROM python:3.12
ENV DATABASE_URL="sqlite:///./movies.db"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 