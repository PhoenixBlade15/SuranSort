#!/bin/bash

python3 Main.py False
sleep 2s
diff Sorted.txt Expected.txt
ascOut=$?

python3 Main.py True
sleep 2s
diff SortedR.txt ExpectedR.txt
descOut=$?

exit $descOut && $ascOut
