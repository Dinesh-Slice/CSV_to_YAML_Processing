#!/bin/bash
sed "s/'//g" out.yml | tee final_file.yml > /dev/null 2>&1

echo "YAML output generated in final_file.yml"