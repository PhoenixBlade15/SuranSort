#!/bin/bash

python Main.py False
diff c Sorted.txt Expected.txt
ascOut=$?

python Main.py True
diff c SortedR.txt ExpectedR.txt
descOut=$?

exit $descOut && $ascOut
