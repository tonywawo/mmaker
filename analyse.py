#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common import commonDef
from sql import Sql


class Analyse:


    def getCUrsor(self):
        return Sql.__init__()

    def do(self):
        cu = self.getCUrsor()
        cu = Sql.createParamTable()
        cu.execute("select * from " + commonDef._paramTableName)
        print(cu.fetchall())
        return cu
        '''
        if cu.fetchall() is None:
            #create table
            pass
        else:
            cu.execute("select * from " + commonDef._paramTableName)
            paramData = cu.fetchone()
            while paramData:
                if paramData[1] == commonDef._tableName:
                    break;
                else:
                    paramData = cu.fetchone()
        '''






