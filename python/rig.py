import json
import os

import maya.cmds as mp


def getNamingFile():
    """
    get the json file which have the naming convention for locators
    """
    filePath = mp.file(q=True, sn=True)
    asset_naming_file = os.path.join(os.path.dirname(filePath), "namingConvention.json")
    naming_file = open(asset_naming_file)
    return json.load(naming_file)


def createJoint(obj):
    """
    create Joint at locator and call itself on the joint's children if there is any
    :param obj: locator to create joint at
    :return: None
    """
    pos = mp.xform(obj, q=True, t=True, ws=True)
    j = mp.joint(radius=0.08, p=pos, name="RIG_" + obj)

    children = mp.listRelatives(obj, c=True, type='locator')
    if children:
        for c in children:
            createJoint(c)


def createJoints(obj):
    if mp.objExists('RIG'):
        print('RIG already exists')
    else:
        jointGRP = mp.group(em=True, name='RIG')

    naming = getNamingFile()

    # create root joint
    root = mp.ls(naming["root"])
    createJoint(obj+'|'+root)
