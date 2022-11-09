#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from api.api_key import ApiKey
from params_VAR.planet import *


@allure.feature("基础设置")
@allure.feature("新增或者编辑基础设置内容")
def addBasicSetup():
    ak = ApiKey()
    data = BasicSetupBody
    url = PROJECTURL + "stepsplanet/qx/pcController/addOrUpdateBasicSetUp"
    res =ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json()+"1")

    # 返回创建的activityId
    activityid = ak.get_text(res.text, "$.data.activityId")
    print(activityid)