#!/bin/sh

while [[ $# -ge 1 ]]
  do
    key="$1"
    shift
    case $key in
      -s|--search)
        search="$1"
        shift
        ;;
      -l|--location)
        location="$1"
        shift
        ;;
      *)
      # unknown option
        echo ${usage}
        ;;
    esac
  done

grep -R $search $location

