# Erlang Library for contact center operations forecasting
# Copyright (c) 2020 by Peter Gossler
#
from pathxtend.path import Path

class Erlang:
    # Base Class for Erlang Calculations
    _SLA            = 0     # Service level e.g 0.85 for 85% interactions answered in TTA - Time to Answer
    _TTA            = 0     # Time to attend to an interaction in seconds
    _AIT            = 0     # Average Interaction time in seconds - the time a service represenative actually works with a customer
    _AIW            = 0     # After Interaction Wrap in seconds - the time a service represenative takes to close a transaction after finishing with a customer
    _AHT            = 0     # Average Handle Time in seconds - ATT + ACW
    _MAX_WAIT       = 0     # The maximum time a customer should wait until they are connected to a service representative
    _IS_NON_VOICE   = False # Controls calculations for non-voice channels, such as chat, email, social media - defaults to voice (False)
    _CC_VAL         = 1     # Value of how many concurrnet transactions an agent can handle
    _INTERVAL       = 0     # The interval time for the calculation in minutes, e.g. 15, 30, 45, 60 - when Erlang calculates values it does so for a given interval
    _OPS_HRS        = 0     # Operational hours of the contact center e.g. 8, 16, 24
    _local_dir      = ""
    
    # __init__ parameters:
    # sla       - Double -  Service Level (0.85, 0.80, etc. -> sla !<= 1.00)
    # tta       - Single -  Time to Attend to an interaction in seconds -> typically 20 seconds for voice, 3600 seconds for email
    # ait       - Single -  Average Interaction time in seconds - the time a service represenative actively works with a customer
    # aiw       - Single -  After Interaction Wrap in seconds - the time a service represenative takes to close a transaction after finishing with a customer
    # max_wait  - Single -  The maximum time a customer should wait until they are connected to a service representative
    # nv        - Bool   -  Controls calculations for non-voice channels (default - False = Voice)
    # ccc       - Single -  Value of how many concurrnet transactions an agent can handle
    # interval  - Single -  The forecasting interval 15, 30, 45, 60 minutes
    # ops_hrs   - Single -  Operational hours of the contact center e.g. 8, 16, 24
    def __init__(self, sla, tta, ait, aiw, max_wait, nv, ccc, interval, ops_hrs):
        try:
            print("Erlang constructor called.")

            self._local_dir = str(Path.script_dir())

            if sla > 1.00 or sla <= 0:
                raise ValueError("sla: 0 < sla <= 1.00!")
            else:
                self._SLA = sla
                pass

            if tta <= 0:
                raise ValueError("tta must be larger than 0!")
            else:
                self._TTA = tta
                pass

            if (ait + aiw) <= 0:
                raise ValueError("ait + aic must be larger than 0!")
            else:
                self._AHT = aiw + ait
                pass
            
            if max_wait <= 0:
                raise ValueError("max_wait must be larger than 0!")
            else:
                self._MAX_WAIT = max_wait
                pass

            if ccc <= 0:
                raise ValueError("ccc must be larger than 0!")
            else:
                self._CC_VAL = ccc
                pass

            self._IS_NON_VOICE  = nv

            if nv and ccc > 1:
                self._AHT = self._AHT / ccc

            if interval != 15 and interval != 30 and interval != 45 and interval != 60:
                raise ValueError("Interval must be either 15, 30, 45 or 60 minutes!")
            else:
                self._INTERVAL  = interval * 60 #c onvert interval from minutes to seconds
                pass

            if ops_hrs != 8 and ops_hrs != 16 and ops_hrs != 24:  
                raise ValueError("ops_hrs must be either 8, 16 or 24 hours!")
            else:
                self._OPS_HRS   = ops_hrs
                pass

        except ValueError as ve:
                print (ve)
                pass

    def print_info (self):
        myerror = "SLA: {0}% / {1} sec"
        print (myerror.format(self._SLA*100, self._TTA))
        myerror = "AHT: {0} sec"
        print (myerror.format(self._AHT))
        myerror = "Max Wait: {0} sec"
        print (myerror.format(self._MAX_WAIT))
        myerror = "Interval: {0} min"
        print (myerror.format(self._INTERVAL/60))
        myerror = "Ops Hours: {0} hrs"
        print (myerror.format(self._OPS_HRS))
        myerror = "Non-Voice: {0}"
        print (myerror.format(self._IS_NON_VOICE))
        myerror = "Concurrent Interactions: {0}"
        print (myerror.format(self._CC_VAL))
        print ("Script Dir: " + self._local_dir)
        pass


ec = Erlang(0.85, 20, 140, 40, 10, False, 1, 30, 24)
ec.print_info()