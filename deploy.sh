#!/bin/bash

echo "stopping old containers....."
docker compose down

echo "Building and starting  containers..."
docker compose up --build -d

echo "Deployment completed."
