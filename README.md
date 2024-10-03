# ParsingLogs

Necessary Artifacts:
Protocol Numbers file(sample - protocol-numbers-1.csv) - Contains protocol encoding
Lookup file(sample - Lookup.csv) - lookup for tag for a given protocol and destination port
Input file(sample - SampleLog.log) - the log file which is to be processed.

Assumptions:
The code supports logs of version 2 alone. 
It is assumed that all the logs are valid and there are no invalid logs(say different version, missing fields etc).

Execution:
To execute the code, make sure that necessary artifacts are made available.
Run the following command in the terminal-
python .\Solution.py <Protocol Numbers file> <Lookup file> <Input file>

The execution results in generation of Output files namely
1. OutputPortProtocolCounts.csv
2. OutputTagCounts.csv
