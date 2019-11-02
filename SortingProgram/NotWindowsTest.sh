   #!/bin/bash

   python Main.py False
   diff Sorted.txt Expected.txt
   ascending_result=$?

   echo ascending_result
   echo ascending_result
   echo ascending_result
   
   python Main.py True
   diff SortedR.txt ExpectedR.txt
   descending_result=$?

   exit $ascending_result
   
