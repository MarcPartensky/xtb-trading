publish:
	poetry publish
build: export
	poetry build
export:
		poetry export -o requirements.txt

