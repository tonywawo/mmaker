#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os.path import join, getsize
import time

import sqlite3

from analyse import Analyse
from common import commonDef
from msg import myMsg
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture


if __name__ == "__main__":
    analyse = Analyse()
    while True:
        analyse.do()
        break



