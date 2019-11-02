#!/bin/bash

export DESC=False
python3 Main.py False
diff Sorted.txt Expected.txt
ascOut=$?

export DESC=True
python3 Main.py True
diff SortedR.txt ExpectedR.txt
descOut=$?

exit $descOut && $ascOut
