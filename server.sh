#!/bin/bash

echo "Starting Voicevox server..."
(cd ~/voicevox_engine && uv run run.py --enable_mock) &
voicevox_pid=$!

echo "Starting Backend..."
(cd backend && .venv/bin/python -m uvicorn main:app --reload) &
backend_pid=$!

echo "Starting Frontend..."
(cd frontend && bun run dev) &
frontend_pid=$!

cleanup() {
    echo -e "\nCtrl+Cが押されました。プロセスを終了します..."
    kill $voicevox_pid 2>/dev/null
    kill $backend_pid 2>/dev/null
    kill $frontend_pid 2>/dev/null
    wait $voicevox_pid 2>/dev/null
    wait $backend_pid 2>/dev/null
    wait $frontend_pid 2>/dev/null
    echo "終了しました。"
    exit 0
}

trap cleanup SIGINT SIGTERM

wait $voicevox_pid
wait $backend_pid
wait $frontend_pid