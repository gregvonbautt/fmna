#!/bin/bash

cat /var/tmp/$1* >> $2
rm /var/tmp/$1*