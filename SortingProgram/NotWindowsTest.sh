   #!/bin/bash

   python Main.py False
   diff --text Sorted.txt Expected.txt
   ascending_result=$?

   echo $ascending_result
   echo $ascending_result
   echo $ascending_result
   
   python Main.py True
   diff --text SortedR.txt ExpectedR.txt
   descending_result=$?

   exit $ascending_result
   
