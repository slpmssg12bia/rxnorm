#!/bin/bash
aws s3 sync rxnormdump/ s3://viquity-database-import-us-east-1/Jobs/rxnorm/rxnorm_current_dump/rxnormdump/
