# COGpl
COG annotation pipeline
# Requirements
* python3
* blast
# What I do
Hi, there. I take amino acid file as input, using blastp searching against COG database. And then I parse annotation results into a tab file looks like this:

query_id|hit_gi|evalue|COG|Func|Name
--------|------|-------|---|---|----
GC00011522|325290147|1.96e-08|COG5164|K|Transcription elongation factor
.......|.......|.......|.......|.......|.......
