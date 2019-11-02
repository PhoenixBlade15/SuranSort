#!/bin/bash

python Main.py False
sleep 2s
diff Sorted.txt Expected.txt
ascOut=$?

python Main.py True
sleep 2s
diff SortedR.txt ExpectedR.txt
descOut=$?

exit $descOut && $ascOut
