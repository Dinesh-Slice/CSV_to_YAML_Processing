#!/bin/bash
sed "s/'//g" out.yml | tee final_file.yml > /dev/null 2>&1

RED="\e[31m"
ENDCOLOR="\e[0m"
echo -e "YAML output generated in ${RED}final_file.yml${ENDCOLOR}"