PYTHON=`which python`
PYTHONPATH=$$PYTHONPATH:./littlespider/:../littlebrother/:../littlebrother/littlebrother/
PEP8_ARGS=--ignore W191,W291,E501,E201,E202,E203,E251
SRC= \
	littlespider/spiders/config.py \
	littlespider/spiders/meta.py \
	\
	littlespider/settings.py \
	\
	twisted-app/app.py


default: pep8 tests

tests:
	@( for FILE in ${SRC}; do \
		echo "Running tests for $$FILE"; \
		PYTHONPATH=${PYTHONPATH} ${PYTHON} $$FILE; \
	done; )

pep8:
	@( for FILE in ${SRC}; do \
		echo "Running pep8 check for $$FILE"; \
		pep8 ${PEP8_ARGS} $$FILE; \
	done; )

clean:
	@( for FILE in `find . -name *.pyc`; do \
		rm -f $$FILE; \
	done; )
