# # AI Background Remover - Production Dockerfile
# FROM python:3.12-slim as builder

# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir --user -r requirements.txt

# FROM python:3.12-slim

# # Install gunicorn for prod
# RUN pip install --no-cache-dir gunicorn

# WORKDIR /app
# COPY --from=builder /root/.local /root/.local
# COPY . .

# # Pre-cache rembg model (~170MB)
# RUN python -c "from rembg import remove; remove(b'b')"

# EXPOSE 5000
# ENV PATH=/root/.local/bin:$PATH
# ENV FLASK_ENV=production

# # Prod: gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers=2", "--timeout=120", "run:app"]


# specify base image
FROM python:3.12.7

# Copy the app to the work directory
WORKDIR /app

# Copy the app to the work directory
ADD . /app

# Install requirements
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the app model
CMD ["python", "run.py"]