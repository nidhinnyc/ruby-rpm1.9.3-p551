#!/bin/bash

ts=$(date +%d%m%y%H%m%s)
git fetch $1
rm -rf /tmp/gitfetcher/
mkdir -p /tmp/gitfetcher/$ts
git clone -b $2 $1 /tmp/gitfetcher/$ts
cd /tmp/gitfetcher/$ts
git rev-parse $2 > REVISION
tar -czf $ts.tar.gz app/models lib/ingestion REVISION
