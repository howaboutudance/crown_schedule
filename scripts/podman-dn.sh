#!/bin/bash
set +x
NETWORK_NAME=sample-app-network

## write to fit the dependencies utilized by env
#
# if podman network exists ${NEWORK_NAME}; then
#     # update with pod kill & pod rm for each pdo
#     podman pod kill mongo
#     podman pod rm mongo 
#     podman pod kill prometheus
#     podman pod rm prometheus
#     # remove network 
#     podman network rm ${NETWORK_NAME}
# else
#     echo "${NETWORK_NAME} does not exists... exiting..."
# fi