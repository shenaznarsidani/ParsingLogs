# ParsingLogs

**Necessary Artifacts**:
Protocol Numbers file(sample - protocol-numbers-1.csv) - Contains protocol encoding
Lookup file(sample - Lookup.csv) - lookup for tag for a given protocol and destination port
Input file(sample - SampleLog.log) - the log file which is to be processed.

**Assumptions**:
The code supports logs of version 2 alone. 
Any invalid logs will be ignored.

**Execution**:
To execute the code, make sure that necessary artifacts are made available.
Run the following command in the terminal-

python .\Solution.py \<Protocol Numbers file\> \<Lookup file\> \<Input file\>

e.g: python .\Solution.py protocol-numbers-1.csv Lookup.csv SampleLog.log

The execution results in generation of Output files namely
1. OutputPortProtocolCounts.csv
2. OutputTagCounts.csv

**Test cases**:
1. Test the functionality
2. Tested on a log file of size 12MB
3. Tested with case sensitivity of the Protocol values
4. Tried introducing invalid logs
5. Tested handling "Untagged" cases
