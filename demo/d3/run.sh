#!/bin/bash
cd $(dirname "$0")
./build_object_graph.py createDirs
run_snake.sh -j
