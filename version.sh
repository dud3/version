#!/bin/bash

git pull origin master
git add -A .
git commit -m "version: bump - $1 :gem:"
git push
