# Use an official Python
FROM python:3

# Set the working directory to app
WORKDIR /app
# Copy the Current directory contemts to the container at /app
COPY . /app

#COPY requirements.txt requirements.txt

# Install package
RUN pip install -r requirements.txt

# Run py when the container lunches
CMD ["python", "ex1_tk.py"]
