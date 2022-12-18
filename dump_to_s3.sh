#!/bin/bash
mkdir rxnormdump
mv !!!!!!!!!I NEED EVERYTHING IN THE DOWNLOADED ZIPFOLDER TO GO INTO THIS DIRECTORY!!!!! rxnormdump
aws s3 sync rxnormdump/ s3://viquity-database-import-us-east-1/Jobs/rxnorm/rxnormdump-"$(date +%d-%m-%y-%H-%M)"/
