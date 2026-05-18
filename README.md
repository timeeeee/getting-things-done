to run api:

    docker compose up

API will be available at localhost:8000

To run back-end tests:

	docker compose up -d
    docker compose run api pytest
	docker compose down
