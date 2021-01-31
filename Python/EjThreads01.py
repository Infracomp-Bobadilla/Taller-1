# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:46:47 2021

@author: Santiago
"""

import logging
import threading
import time

#.. Logger Config
format = "%(asctime)s: %(message)s"
logging.basicConfig(format = format, level = logging.INFO, datefmt="%H:%M:%S")

#.. Función a ejecutar
def process(msg: str):
    logging.info(msg)
    time.sleep(3)
    
#.. Ejecutar
thread = threading.Thread(target = process, args=("Un saludo con un poco de espera",))
thread.start()