#!/bin/sh

# A script to push a key to the only argument, a remote server.
CheckArgs()
{
  # Check if an argument was given.
  if [ ! "$file" ] && [ ! "$host" ]; then
    echo "Please specify a hostname to distribute the key to."
    exit 1
  fi
  if [ ! "$user" ]; then
    echo "Please specify a username."
    exit 1
  fi
}

CheckSSH()
{
  # Check if all the local files are here.
  if [ ! -f ~/.ssh/id_rsa.pub ] ; then
  echo "The local file ~/.ssh/id_rsa.pub is missing. Please create it."
  exit 1
  fi
}

PushKey()
{
  # This command send the key, create a .ssh dir if required and set the
  # correct permissions.
  #echo "cat ~/.ssh/id_rsa.pub | ssh -q \"$user@$hostname\" \"if [ ! -d ~/.ssh/ ] ; then mkdir ~/.ssh ; fi ; chmod 700 ~/.ssh/ ; cat - >> ~/.ssh/authorized_keys ; chmod 600 ~/.ssh/authorized_keys\""
  if [  -z "$password" ]; then
    echo "no password specified"
    cat ~/.ssh/id_rsa.pub | ssh -q "$user@$hostname" "if [ ! -d ~/.ssh/ ] ; then mkdir ~/.ssh ; fi ; chmod 700 ~/.ssh/ ; cat - >> ~/.ssh/authorized_keys ; chmod 600 ~/.ssh/authorized_keys"
  else
    echo "password specified"
    cat ~/.ssh/id_rsa.pub | sshpass -p ${password} ssh -q "$user@$hostname" "if [ ! -d ~/.ssh/ ] ; then mkdir ~/.ssh ; fi ; chmod 700 ~/.ssh/ ; cat - >> ~/.ssh/authorized_keys ; chmod 600 ~/.ssh/authorized_keys"
  fi
}

ReadFile()
{
  while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    hostname=$line
    PushKey
  done < "$file"
}

password=""

while [[ $# -ge 1 ]]
  do
    key="$1"
    shift
    case $key in
      -f|--file)
        file="$1"
        shift
        ;;
      -h|--host)
        host="$1"
        shift
        ;;
      -u|--user)
        user="$1"
        shift
        ;;
      -p|--password)
        password="$1"
        shift
        ;;
      *)
      # unknown option
        echo ${usage}
        ;;
    esac
  done
echo File = $file
echo Host = $host
CheckArgs
CheckSSH

if [ "$file" ]; then
  ReadFile
else
  hostname=$host
  PushKey
fi
