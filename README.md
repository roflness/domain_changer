# domain_changer
Count the type and percentage of domains included in the specified CSV file that is uploaded.

### argument passed is the filename ONLY. No need to include ".csv" (will only accept CSV files)
### example: python domain_changer.py test

Two CSV files are subsequently saved.
1) output.csv -> list of domains that have cleaned out, ie the following are removed: http/s, www., /+
2) percentage.csv -> table summary of the percentage of domain types
