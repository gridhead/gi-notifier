# Base image: Fedora minimal
FROM registry.fedoraproject.org/fedora-minimal:44 as base

# Application image
FROM base as application

# Set environment variables
ENV VIRTUAL_ENV=/venv

# Install pip and Poetry
RUN \
    microdnf install -y python3-pip \
    && microdnf clean all \
    && pip install poetry

# Setup work directory
WORKDIR /app

# Copy complete codebase
COPY . .

# Set path for poetry to find the CLI application
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
RUN \
    python -m venv $VIRTUAL_ENV \
	&& . $VIRTUAL_ENV/bin/activate \
	&& poetry install

# Run the CLI
ENTRYPOINT ["gi-notifier"]
