#!/bin/bash

usage="Usage: $0 <action> -s <projects to skip> (optional) .
Valid actions:  update, "

projects=(
    config 
    deploy 
    devops
    infrastructure
    pythonlib
#   vagrant
)

skip=()

Update()
{
    echo Changing to directory: ${workspace}/${project}
    cd ${workspace}/${project}
    git checkout develop
    git pull
    cd ..
}

Skip()
{
    echo Changing to directory: ${workspace}/${project}
    cd ${workspace}/${project}
    git pull
    cd ..
}

workspace="/home/jstacy/workspace/env_setup"


while [[ $# > 1 ]]
do
    key="$1"
    shift

    case $key in
        -a|--action)
        action="$1"
        shift
        ;;
        -w|--workspace)
        workspace="$1"
        shift
        ;;
        -s|--skip)
        skip="$1"
        shift
        ;;
        *)
            # unknown option
            echo ${usage}
        ;;
    esac
done


if [ ! ${action} ]; then
    echo ${usage}
    exit
fi

for item in "${projects[@]}"
    do
        project=${item}
        case ${action} in
            "update")
            Update;;
        esac
    done
