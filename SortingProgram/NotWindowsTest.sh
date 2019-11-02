#!/bin/bash

python Main.py False
ascOut=$(diff Sorted.txt Expected.txt)

python Main.py True
descOut=$(diff SortedR.txt ExpectedR.txt)

exit $descOut && $ascOut
