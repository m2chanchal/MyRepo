#!/usr/bin/env python3

import os
import boto3

#here = os.path.dirname(__file__)
#temp_body = os.path.join(here, 'dockerimages')
temp_body = 'example.yml'

cfn = boto3.client('cloudformation')


def main():
    stackname = 'example-deploy'
    capabilities = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']
    stackdata = cfn.create_stack(
      StackName=stackname,
      DisableRollback=True,
      TemplateBody=temp_body,
      Capabilities=capabilities)
	  
if __name__=="__main__":
    main()
        
