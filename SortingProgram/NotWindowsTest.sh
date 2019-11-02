   #!/bin/bash

   python Main.py False
   cmp Sorted.txt Expected.txt
   ascending_result=$?

   echo $ascending_result
   echo $ascending_result
   echo $ascending_result
   
   python Main.py True
   cmp SortedR.txt ExpectedR.txt
   descending_result=$?

   exit $ascending_result
   
