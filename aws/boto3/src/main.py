#!/usr/bin/python3
import os

from formula import formula

access_key = os.environ.get("RIT_ACCESS_KEY")
secret_access_key = os.environ.get("RIT_SECRET_ACCESS_KEY")
region = os.environ.get("RIT_REGION")
vpc_cidr = os.environ.get("RIT_VPC_CIDR")
vpc_name = os.environ.get("RIT_VPC_NAME")

formula.run(access_key, secret_access_key, region, vpc_cidr, vpc_name)
