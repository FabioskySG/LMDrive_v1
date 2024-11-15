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
# export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.15-py3.10-linux-x86_64.egg

export PYTHONPATH=$PYTHONPATH:leaderboard
export PYTHONPATH=$PYTHONPATH:leaderboard/team_code
export PYTHONPATH=$PYTHONPATH:scenario_runner

export LEADERBOARD_ROOT=leaderboard
export CHALLENGE_TRACK_CODENAME=SENSORS
export PORT=$PT # same as the carla server port
export TM_PORT=$(($PT+500)) # port for traffic manager, required when spawning multiple servers/clients
export DEBUG_CHALLENGE=0
export REPETITIONS=1 # multiple evaluation runs


export ROUTES=langauto/benchmark_long.xml
export TEAM_AGENT=leaderboard/team_code/lmdriver_agent.py # agent
export TEAM_CONFIG=leaderboard/team_code/lmdriver_config.py # model checkpoint, not required for expert
export CHECKPOINT_ENDPOINT=results/sample_result.json # results file
# export SCENARIOS=leaderboard/data/scenarios/no_scenarios.json #town05_all_scenarios.json
export SCENARIOS=leaderboard/data/official/all_towns_traffic_scenarios_public.json
export SAVE_PATH=data/eval # path for saving episodes while evaluating
export RESUME= # NOTHING FOR FALSE, SOMETHING FOR TRUE


echo ${LEADERBOARD_ROOT}/leaderboard/leaderboard_evaluator.py

# print the python path
echo $PYTHONPATH

# echo port and traffic manager port
echo "SCENARIOS: ${SCENARIOS}"
echo "ROUTES: ${ROUTES}"
echo "REPETITIONS: ${REPETITIONS}"
echo "TRACK: ${CHALLENGE_TRACK_CODENAME}"
echo "CHECKPOINT END: ${CHECKPOINT_ENDPOINT}"
echo "AGENT: ${TEAM_AGENT}"
echo "AGENT CONFIG: ${TEAM_CONFIG}"
echo "DEBUG: ${DEBUG_CHALLENGE}"
echo "RECORD: ${RECORD_PATH}"
echo "RESUME: ${RESUME}"
echo "PORT: ${PORT}"
echo "TRAFFIC MANAGER PORT: ${TM_PORT}"

python3 -u ${LEADERBOARD_ROOT}/leaderboard/leaderboard_evaluator.py \
--scenarios=${SCENARIOS}  \
--routes=${ROUTES} \
--repetitions=${REPETITIONS} \
--track=${CHALLENGE_TRACK_CODENAME} \
--checkpoint=${CHECKPOINT_ENDPOINT} \
--agent=${TEAM_AGENT} \
--agent-config=${TEAM_CONFIG} \
--debug=${DEBUG_CHALLENGE} \
--record=${RECORD_PATH} \
--resume=${RESUME} \
--port=${PORT} \
--trafficManagerPort=${TM_PORT}