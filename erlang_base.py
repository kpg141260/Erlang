# Erlang Library for contact center operations forecasting
# Base Modules
# Copyright (c) 2020 by Peter Gossler
# Version 0.1.0

class Erlang_Base:
    def __init__(self):
        pass

    @staticmethod
    # Apply minimum and maximum bounds to a value
    def MinMax (eval, min, max):
        if eval < min:
            return float (min)
        elif eval > max:
            return float (max)
        else:
            return float(eval)

    @staticmethod
    def FixInt (val):
        return int(val//1)

    @staticmethod
    #Ceiling function, rounds to the nearest numerically higher integer
    def IntCeiling(val):
        S = 0
        try:
            if val < 0:
                S = val - 0.9999
            else:
                S = val + 0.9999
            return int(S//1)
        except:
            return 0

    @staticmethod
    # Convert a number of hours into seconds
    def hours_to_secs (val):
        return int((val * 3600 + 0.5)//1)