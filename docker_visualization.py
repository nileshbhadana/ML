#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:48:20 2019

@author: nilesh
"""

import json,docker
client=docker.Client(base_url='unix://var/run/docker.sock')
stats_obj=client.stats('dreamy_noether')
for stat in stats_obj:
    print(stat)
    
    
#for conversion to json
my_json=new_bytes.decode('utf8').replace("'",'"')
data=json.loads(my_json)
s=json.dumps(data, intent=4, sort_keys=True)