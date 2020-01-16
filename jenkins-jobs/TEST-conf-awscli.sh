#!/bin/bash

env | grep AWS | sort

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -

aws configure list
aws sts get-caller-identity

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -

export AWS_SHARED_CREDENTIALS_FILE="./.aws/credentials"

aws configure list
aws sts get-caller-identity
