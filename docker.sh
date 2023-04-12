#!/bin/bash

function show_usage (){
    printf "Usage: $0 [options [parameters]]\n"
    printf "\n"
    printf "Options:\n"
    printf " --build, Build all services\n"
    printf " --start, Start all services\n"
    printf " --stop, Stop all services\n"
    printf " --restart, Restart all services\n"
    printf " -h|--help, Print help\n"

return 0
}

function stop (){
    docker stop finance-yahoo-svc && docker rm finance-yahoo-svc
    docker container prune

return 0
}

function start (){
    docker run -d --name finance-yahoo-svc -p 8000:80 finance-yahoo-svc:v1.0.0
    
return 0
}

while [ ! -z "$1" ]; do
  case "$1" in
    --build)
        shift
        echo "Building all services..."
        docker build -t finance-yahoo-svc:v1.0.0 .
        ;;
    --start)
        shift
        echo "Starting all services..."
        start
        ;;
    --stop)
        shift
        echo "Stopping all services..."
        stop
        ;;
    --restart)
        shift
        echo "Restaring all services..."
        stop
        start
        ;;
    *)
       show_usage
       ;;
  esac
shift
done
