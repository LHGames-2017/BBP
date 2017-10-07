run:
	sudo docker build . -t polyhx/python-test
	sudo docker run -p 3000:3000 -t polyhx/python-test

build:
	sudo docker build . -t

build-deps:
	sudo docker build . -t polyhx/python-seed
