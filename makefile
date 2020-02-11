unittests:
	@python3.6 -m unittest discover ./dodo/tests

rpm:
	@./build_rpm.sh
