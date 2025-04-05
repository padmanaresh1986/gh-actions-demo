#!/bin/bash
set -e

if [ -z "$REPO_URL" ] || [ -z "$RUNNER_TOKEN" ]; then
  echo "ERROR: You must set REPO_URL and RUNNER_TOKEN environment variables."
  exit 1
fi

# Configure the runner
./config.sh --unattended \
  --url "$REPO_URL" \
  --token "$RUNNER_TOKEN" \
  --name "$RUNNER_NAME" \
  --work "$RUNNER_WORKDIR" \
  --replace

# Run the runner
exec ./run.sh
