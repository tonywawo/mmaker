#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from common import commonDef


class Sql:

    _cu = ""

    @classmethod
    def __init__(self):
        conn = sqlite3.connect(commonDef._dbName)
        _cu = conn .cursor()
        return _cu;

    @classmethod
    def createParamTable(self):

        if self._cu.fetchall() is not None:
            pass
        else:
            self._cu.execute("create table " + commonDef._paramTableName +
                " (id integer auto_increment primary key,"
                " runmode integer,"
                " runtype integer,"
                " tablename varchar(32) UNIQUE)")
            self._cu.commit()
        return self._cu;




