#!/bin/bash
while true
do
    python3 compare_videos.py
    echo "Waiting 60 seconds before the next check..."
    sleep 60
done
