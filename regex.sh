#!/bin/bash
sed "s/'//g" sample.yml | tee final_file.yml > /dev/null 2>&1