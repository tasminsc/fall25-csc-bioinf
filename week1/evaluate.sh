set -euo pipefail

#!/bin/bash

printf "%-10s %-10s %-12s %10s\n" "Dataset" "Language" "Runtime" "N50"
echo "-------------------------------------------"

datasets=("data1" "data2" "data3" "data4")

for dataset in "${datasets[@]}"; do
    start=$(date +%s)
    # Record start time


    # Run your Python script and capture N50 (last line of output)
    n50=$(python genome-assembly/main.py "$dataset" | tail -n 1)

    # Record end time and compute runtime
    end=$(date +%s)
    runtime=$(( end - start ))

    # Convert seconds to HH:MM:SS
    runtime_fmt=$(printf "%02d:%02d:%02d" $((runtime/3600)) $(( (runtime%3600)/60 )) $((runtime%60)) )

    # Print row
    printf "%-10s %-10s %-12s %-10s\n" "$dataset" "python" "$runtime_fmt" "$n50"
done
