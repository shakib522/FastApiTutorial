COMMIT_HASH=$(git rev-parse --short HEAD)

echo "COMMIT_HASH=$COMMIT_HASH" > .env
echo ".env file created with COMMIT_HASH=$COMMIT_HASH"