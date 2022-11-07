#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_driver import yaml_driver

content = yaml_driver.load_yaml('../data/data.yaml')
print(content)