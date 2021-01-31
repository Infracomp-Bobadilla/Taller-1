# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:53:44 2021

@author: Santiago
"""

import logging
import threading
import time
import random

#.. Logger Config
format = "%(asctime)s: %(message)s"
logging.basicConfig(format = format, level = logging.INFO, datefmt="%H:%M:%S")

# .. Clase
class Example_Thread (threading.Thread):
    
    # .. Constructor
    def __init__ (self, id_thread: int, delay_time: float, msg: str):
        super().__init__()
        self.id_thread = id_thread
        self.delay_time = delay_time
        self.msg = msg
        
    # .. Método
    def message(self):
        time.sleep(self.delay_time)
        print(f"ID THREAD: {self.id_thread} - Message: {self.msg}")
        
    # .. RUN
    def run(self):
        self.message()
        
# .. EJECUTAR
threads = []
time_delay = random.uniform(2.5, 4.5)

thread = Example_Thread(id_thread = 0, delay_time = time_delay , msg = "Un saludo con poca espera")
thread.start()