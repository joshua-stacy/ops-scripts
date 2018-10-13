#!/bin/bash


export action=$1

Modify()
{
    MODIFIED="$( git status | awk '{ if ($1 == "modified:") print $2 }'  | xargs echo $MODIFIED )"

    for item in ${MODIFIED}; do
        {
            echo adding $item;
            git add $item;
        }
    done
}

Add()
{
    ADDED="$( git status | awk '{ if ($1 == "added:") print $2 }'  | xargs echo $ADDED )"

    for item in ${ADDED}; do
        {
            echo adding $item;
            git add $item;
        }
    done
}


Delete()
{
    DELETED="$( git status | awk '{ if ($1 == "deleted:") print $2 }'  | xargs echo $DELETED )"
    for item in ${DELETED}; do
        {
            echo removing $item;
            git rm $item;
        }
    done
}

Never()
{
    for item in ${MODIFIED}; do
        {
            echo removing $item;
            git rm $item;
        }
    done
}

case ${action} in
    add)
        Add
        ;;
    modify)
        Modify
        ;;
    delete)
        Delete
        ;;
esac
