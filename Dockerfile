FROM ubuntu:22.04

# Install required packages
RUN apt-get update && \
    apt-get install -y curl tar libicu70 libkrb5-3 libssl3 ca-certificates && \
    apt-get clean

# Set working directory
WORKDIR /actions-runner

# Download GitHub Actions runner
ENV RUNNER_VERSION=2.323.0
RUN curl -o actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz && \
    tar xzf actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz && \
    rm actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set environment variables for runner config
ENV RUNNER_NAME=docker-runner
ENV RUNNER_WORKDIR=/actions-runner/_work

# Entrypoint
ENTRYPOINT ["/entrypoint.sh"]
