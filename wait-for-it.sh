#!/bin/bash
# wait-for-it.sh

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

# Split host and port if the host is in the format "host:port"
IFS=':' read -r -a host_port <<< "$host"
host="${host_port[0]}"
port="${host_port[1]}"

until nc -z "$host" "$port"; do
  >&2 echo "Waiting for $host:$port..."
  sleep 1
done

>&2 echo "$host:$port is available, running command $cmd"
exec $cmd
