   #!/bin/bash

   python Main.py False
   diff --text Sorted.txt Expected.txt
   ascOut=$?
   
   python Main.py True
   diff --text SortedR.txt ExpectedR.txt
   descOut=$?

   exit $ascOut && $descOut
   
