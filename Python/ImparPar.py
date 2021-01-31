# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:09:10 2021

@author: Santiago
"""

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
    def __init__ (self, id_thread: int, delay_time: float, msg: str, limit: int):
        super().__init__()
        self.id_thread = id_thread
        self.delay_time = delay_time
        self.msg = msg
        self.limit = limit
        
    # .. Método
    def message(self):
        
        for i in range(1, self.limit+1):
            if self.id_thread == 0 and i%2 == 1:
                print(f"ID THREAD: {self.id_thread} - {self.msg} : Número {i}")
                time.sleep(self.delay_time)
            elif self.id_thread == 1 and i%2 == 0:
                print(f"ID THREAD: {self.id_thread} - {self.msg} : Número {i}")
                time.sleep(self.delay_time)
            
    # .. RUN
    def run(self):
        self.message()
        
# .. EJECUTAR
time_delay = random.uniform(0.5, 1.5)

lim = int(input('Ingrese el límite superior: '))

impar = Example_Thread(id_thread = 0, delay_time = time_delay , msg = "Impar", limit = lim)
par = Example_Thread(id_thread = 1, delay_time = time_delay , msg = "Par", limit = lim)

impar.start()
par.start()