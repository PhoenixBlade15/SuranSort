#!/bin/bash

python Main.py False
diff Sorted.txt Expected.txt

python Main.py True
diff SortedR.txt ExpectedR.txt
descOut=$?

exit $descOut && $ascOut
