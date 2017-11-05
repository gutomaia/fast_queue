NOSETEST_ARGS?=

PROJECT_NAME=Fast Queue
PROJECT_TAG=fast_queue
PYTHON_MODULES=fast_queue


OK=\033[32m[OK]\033[39m
FAIL=\033[31m[FAIL]\033[39m
CHECK=@if [ $$? -eq 0 ]; then echo "${OK}"; else echo "${FAIL}"; cat ${DEBUG} ; fi

WGET=wget -q

default: python.mk github.mk
	@$(MAKE) -C . test

ifeq "true" "${shell test -f python.mk && echo true}"
include python.mk
endif

ifeq "true" "${shell test -f github.mk && echo true}"
include github.mk
endif


python.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/python.mk && touch $@

github.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/github.mk && touch $@

.git/hooks/pre-commit: misc/hooks/pre-commit
	@echo "Instaling pre-commit hook: \c"
	@mkdir -p .git/hooks && \
		cp misc/hooks/pre-commit $@ && \
		touch $@
	${CHECK}

${CHECKPOINT_DIR}/setup.py: setup.py
	${VIRTUALENV} python setup.py develop && \
		touch $@

dependencies: ${REQUIREMENTS} ${CHECKPOINT_DIR}/setup.py

build: dependencies python_build

test: build ${REQUIREMENTS_TEST}
	${VIRTUALENV} nosetests ${NOSETEST_ARGS} ${PYTHON_MODULES}

dist/.dist.check: .requirements.txt.check
	@mkdir -p dist && touch $@

dist: python_egg python_wheel

trash:
	@find analytics -iname "*.pyc" | \
		xargs -I [] sh -c "echo [] | \
		sed 's/.pyc$$/.py/g'" | \
		xargs -I [] sh -c "test -f [] || (echo Removing compiled []c: && rm []c)"

clean: python_clean
	@rm -rf build dist
	@rm -rf plugins

purge: clean python_purge
	@rm python.mk
	@rm -rf *.egg-info

.PHONY: venv dependencies python_dependencies build run dist egg wheel docker clean
