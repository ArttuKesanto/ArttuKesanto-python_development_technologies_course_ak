# Referenced https://www.cyberciti.biz/faq/how-to-read-time-in-shell-script/
#!/bin/bash
touch log.log 
echo "Heippa!" $(date +"%T") > log.log
