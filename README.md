# domain_changer
Count the type and percentage of domains included in the specified CSV file that is uploaded.

### First argument is the filename. INCLUDE ".csv" (will only accept CSV files)
### example: python domain_changer.py test.csv IO_LineNumber_cleaned

Two CSV files are subsequently saved.
1) IO_LineNumber_cleaned.csv -> list of domains that have been cleaned, ie the following are removed: http/s, www., /+
2) percentage.csv -> table summary of the percentage of domain types
