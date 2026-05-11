SHELL := /usr/bin/env bash

profiler:
	python3 -m kernprof -lv -p main.py main.py |& tee logs/kernprof.log

run:
	time python3 main.py
