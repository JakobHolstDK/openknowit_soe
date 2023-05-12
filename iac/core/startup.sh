#!/bin/bash

# create a Docker volume if it does not already exist
create_volume() {
    if [[ $(docker volume ls -q -f name=$1) ]]; then
        echo "Volume '$1' already exists"
    else
        docker volume create $1
        echo "Volume '$1' created successfully"
    fi
}

create_volume mongodb_data
create_volume traefik_data
create_volume structurizr_data
create_volume vault_data
create_volume consul_data

echo "Volumes created successfully"


docker-compose -d up
