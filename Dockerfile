# Use an official Miniconda base image
FROM continuumio/miniconda3

# Set a working directory inside the container
WORKDIR /app

# Copy the environment.yml to the working directory
COPY environment.yml /app/

# Create the Conda environment from the environment.yml file
RUN conda env create -f environment.yml

# Make sure the Conda environment is activated when the container runs
# Replace `myenv` with your environment name
SHELL ["conda", "run", "-n", "drink", "/bin/bash", "-c"]

# Set the entrypoint to the Conda environment
ENTRYPOINT ["conda", "run", "-n", "drink", "python"]

# Optionally, specify a command to run (e.g., starting a script or app)
#CMD ["my_script.py"]

CMD ["menu_setup.py", "--add", "True", "--product", "milk", "--cost", "20"]


