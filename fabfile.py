#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib import files

from config.servers import staging,  prod

from debian import setup_debian
from project import setup_project
from server import setup_server

def uptime():
    """ Show number of active connections on the server """ 
    run('uptime')

def remote_info():
    """ Get name and info of remote host """ 
    run('uname -a')

def local_info():
    """ Get name and info of local host """ 
    local('uname -a')

def init():
    """ Init setup of the project """
    setup_project()
    setup_server()
