import erlang_c
# import pandas as pd

# Create object from Erlang_C class 
# (SLA, TTA, ATT, ACW, ABNT, MAX_WAIT, NV, CCC, INTERVAL, OPS_HRS)
ec = erlang_c.Erlang(0.80, 40, 240, 36, 30, 50, False, 1, 60, 16)

# Assumptions for this example - Call Center
# (SLA) Service Level of 80% of calls answered in 30 seconds
# (TTA) Time to Answer = 20 seconds
# (AIT) Average Interaction Time = 300 seconds
# (AIW) Average After Call Wrap = 40 seconds
# (ABNT) Average Abandon Time = 20 seconds
# Max Wait Time = 30 seconds
# (NV) Non-Voice = False - this is for voice
# (CCC) Concurrent Transactions per agent is 1
# The interval is 60 minutes
# operations hours are 16 hours
# Service Time is 30 seconds - this is the target for the answer time after a phone rings

service_time = 30
# The call arrival pattern
call_data = [["06:00", 1], ["07:00", 8], ["08:00", 8], ["09:00", 56], ["10:00", 80], ["11:00", 79], ["12:00", 79], ["13:00", 77], ["14:00", 69], ["15:00", 68], ["16:00", 44], ["17:00", 39], ["18:00", 19], ["19:00", 2], ["20:00", 1], ["21:00", 0]]
# The header for the grid output - this we will also use later to export into a csv file
csv_header = ["Time", "Calls", "Agents", "Util", "SLA","ASA","Abandon","Q-Count","Q-Time","Q-Size"]
# Some variables we need later
max_call_vol = 0
idx = 0
count = 0
# Adjust rjust value to number of spaces
adjust_val = 11
# A string that we need to out put to the terminal and csv header
str_head = ''
# A temporary string needed
tmp = ''

for x in call_data:
    if x[1] > max_call_vol:  
        max_call_vol = x[1]
        idx = count
    count += 1

agents = ec.Agents (service_time, max_call_vol)

ec.print_info()

print ("\n-- Calculations for maximum call volume --\n")
x = call_data[idx]
print ("Largest Call Volume found at {} with {} calls.".format(x[0], x[1]))
print ("Using largest call volume {} for next calculations...".format(x[1]))
print ("Agents:         {}".format(agents))
print ("Utilisation:    {:0.2f}%".format(ec.Utilisation(agents, max_call_vol) * 100))
print ("Trunks:         {}".format(ec.Trunks(agents, max_call_vol)))
print ("SLA:            {:0.2f}%".format(ec.SLA(agents, max_call_vol, service_time) * 100))
print ("ASA:            {} sec".format(ec.ASA(agents, max_call_vol)))
print ("Abandoned:      {:0.2f}%".format(ec.Abandon(agents, max_call_vol) * 100))
print ("Queued:         {:0.2f}%".format(ec.Queued(agents, max_call_vol) * 100))
print ("Queue Time      {} sec".format(ec.QueueTime(agents, max_call_vol)))
print ("Queue Size      {}".format(ec.QueueSize(agents, max_call_vol)))

# Now we create a list that later on we can export to a CSV file
print ("\nCalculating data set...\n")
# Format the header string for output - will be reused further down
for Item in csv_header:
    tmp = format(Item.ljust(adjust_val))
    str_head = str_head + tmp
# Print the header
print(str_head)
# print a line of dashes
print ("-" * len(str_head))
# Clear temp string
tmp = ''
str_data = ''
for x in call_data:
    tmp = str(x[0]).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(x[1]).ljust(adjust_val)
    str_data = str_data + tmp
    ag = ec.Agents (service_time, x[1])
    tmp = str(ag).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round(ec.Utilisation(ag, x[1]), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round(ec.SLA(ag, x[1], service_time), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(ec.ASA(ag, x[1])).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round (ec.Abandon(ag, x[1]), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round(ec.Queued(ag, x[1]), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(ec.QueueTime(ag, x[1])).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(ec.QueueSize(ag, x[1])).ljust(adjust_val)
    str_data = str_data + tmp
    print (str_data)
    str_data = ''
print ()

del ec

# Create new object from Erlang_C class 
# (SLA, TTA, ATT, ACW, ABNT, MAX_WAIT, NV, CCC, INTERVAL, OPS_HRS)
ec = erlang_c.Erlang(0.80, 30, 300, 40, 20, 30, True, 3, 60, 16)

# Assumptions for this example - Call Center
# (SLA) Service Level of 80% of calls answered in 30 seconds
# (TTA) Time to Answer = 20 seconds
# (AIT) Average Interaction Time = 300 seconds
# (AIW) Average After Call Wrap = 40 seconds
# (ABNT) Average Abandon Time = 20 seconds
# Max Wait Time = 30 seconds
# (NV) Non-Voice = True - this is for chat
# (CCC) Concurrent Transactions per agent is 3 - meaning an agent can handle 3 chat sessions concurrently
# The interval is 60 minutes
# operations hours are 16 hours
# Service Time is 30 seconds - this is the target for the answer time after a phone rings

service_time = 30
call_data = [["08:00", 100], ["09:00", 120], ["10:00", 168], ["11:00", 236], ["12:00", 331], ["13:00", 464], ["14:00", 650], ["15:00", 910], ["16:00", 546], ["17:00", 328], ["18:00", 197], ["19:00", 119], ["20:00", 72], ["21:00", 44], ["22:00", 27], ["23:00", 17]]
max_call_vol = 0
idx = 0
count = 0
for x in call_data:
    if x[1] > max_call_vol:  
        max_call_vol = x[1]
        idx = count
    count += 1

agents = ec.Agents (service_time, max_call_vol)

ec.print_info()

print ("\n-- Calculations for maximum call volume --\n")
x = call_data[idx]
print ("Largest Call Volume found at {} with {} calls.".format(x[0], x[1]))
print ("Using largest call volume {} for next calculations...".format(x[1]))
print ("Agents:         {}".format(agents))
print ("Utilisation:    {:0.2f}".format(ec.Utilisation(agents, max_call_vol) * 100))
print ("SLA:            {:0.2f}".format(ec.SLA(agents, max_call_vol, service_time) * 100))
print ("ASA:            {}sec".format(ec.ASA(agents, max_call_vol)))
print ("Abandoned:      {:0.2f}".format(ec.Abandon(agents, max_call_vol) * 100))
print ("Queued:         {:0.2f}".format(ec.Queued(agents, max_call_vol) * 100))
print ("Queue Time      {}sec".format(ec.QueueTime(agents, max_call_vol)))
print ("Queue Size      {}".format(ec.QueueSize(agents, max_call_vol)))

print ("\nCalculating data set...\n")
# Print the header
print(str_head)
# print a line of dashes
print ("-" * len(str_head))
tmp = ''
str_data = ''
for x in call_data:
    tmp = str(x[0]).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(x[1]).ljust(adjust_val)
    str_data = str_data + tmp
    ag = ec.Agents (service_time, x[1])
    tmp = str(ag).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round(ec.Utilisation(ag, x[1]), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round(ec.SLA(ag, x[1], service_time), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(ec.ASA(ag, x[1])).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round (ec.Abandon(ag, x[1]), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(round(ec.Queued(ag, x[1]), 2)).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(ec.QueueTime(ag, x[1])).ljust(adjust_val)
    str_data = str_data + tmp
    tmp = str(ec.QueueSize(ag, x[1])).ljust(adjust_val)
    str_data = str_data + tmp
    print (str_data)
    str_data = ''
print ()

del ec
