#!/bin/bash
set -euo pipefail

printf "%-10s %-10s %-12s %10s\n" "Dataset" "Language" "Runtime" "N50"
echo "-------------------------------------------"

datasets=("data1" "data2" "data3" "data4")

for dataset in "${datasets[@]}"; do
    
    languages=("python" "codon")
    # Run your script and capture N50 (last line of output)
    for lang in "${languages[@]}"; do
        start=$(date +%s)
        # Record start time
        if [ "$lang" = "codon" ]; then
            n50=$(codon run genome-assembly/mainc.py "$dataset" | tail -n 1)
        else
            n50=$(python genome-assembly/main.py "$dataset" | tail -n 1)
        fi

        # Record end time and compute runtime
        end=$(date +%s)
        runtime=$(( end - start ))

        # Convert seconds to HH:MM:SS
        runtime_fmt=$(printf "%02d:%02d:%02d" $((runtime/3600)) $(( (runtime%3600)/60 )) $((runtime%60)) )

        # Print row
        printf "%-10s %-10s %-12s %-10s\n" "$dataset" "$lang" "$runtime_fmt" "$n50"
    done
done
