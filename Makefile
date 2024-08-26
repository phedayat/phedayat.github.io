clean:
	rm -rf public
	rm .hugo_build.lock

build:
	hugo

run:
	hugo serve
