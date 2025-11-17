# to cut comma delimited fields from file for review
cut -d , -f 5 wps.csv | sort -u |wc -l
cut -d , -f 5 wps.csv | sort -u |head -10
