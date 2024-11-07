#!/bin/bash

set -e

# export PT=$(($RANDOM % 1000 + 16000))
export PT=2000
# bash carla/CarlaUE4.sh --world-port=$PT &

sleep 2

export CARLA_ROOT=carla

export CARLA_SERVER=${CARLA_ROOT}/CarlaUE4.sh
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg

python3 check_carla.py
# python3 carla/PythonAPI/examples/spawn_npc.py