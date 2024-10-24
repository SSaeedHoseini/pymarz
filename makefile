generate:
	sudo rm -rf ./src/*
	docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate -i /local/api.json -g python-pydantic-v1 -o /local -p packageName=marzapi --skip-validate-spec

fix-permission:
	sudo chown ho:ho . --recercive