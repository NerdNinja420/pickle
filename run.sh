#!/usr/bin/env zsh

PYTHON_PROGRAM="./main.py"
source ./tetrix_venv/bin/activate


for i in {1..10}; do
  echo "Starting Python program (Iteration $i)"
  
  python3 "$PYTHON_PROGRAM" &
  PYTHON_PID=$!

  sleep 2
  
  echo "Terminating Python program (Iteration $i)"
  kill -SIGTERM $PYTHON_PID
  
  wait $PYTHON_PID 2>/dev/null
done

