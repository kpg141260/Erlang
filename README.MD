# Erlang for Python

This Erlang Python Library was created to enable Erlang based contact center forecasting using Python.

# Table of Contents
1. [What is Erlang](#what-is-erlang)
2. [Overview](#overview)
3. [Classes](#classes)
4. [Erlang Base Class](#erlang-base-class)
  1. [MinMax Method](#minmax)
5. [Erlang Main Class](#erlang-main-class)
  1. [Introduction](#introduction)
  2. [ErlangB - calculate probability of call being blocked](#ErlangB)
  3. [ErlangBExt - calculate probability of call being blocked](#erlangbext)
  4. [EngsetB - calculate probability of call being blocked](#engsetb)
  5. [ErlangC - calculate probability of transaction being queued](#erlangc)
  6. [NBTrunks - Calculate number of trunks - use for high volume](#nbtrunks)
  7. [NumberTrunks - Calculate number of trunks - use for normal volume](#numbertrunks)
  8. [NumberAgents - Calculate the number of agents](#numberagents)
  9. [LoopingTraffic](#loopingtraffic)
  10. [Abandon](#abandon)
  11. [Agents](#agents)
  12. [AgentASA](#agentasa)
  13. [ASA](#asa)
  14. [CallCapacity](#callcapacity)
  15. [FractionalAgents](#fractionalagents)
  16. [FractionalCallCapacity](Xfractinalcallcapacity)
  17. [Queued](#queued)
  18. [QueueSize](#queuesize)
  19. [QueueTime](#queuetime)
  20. [ServiceTime](#servicetime)
  21. [SLA](#sla)
  22. [Trunks](#trunks)
  23. [Utilisation](#utilisation)

## What is Erlang

Erlang C is a proven method or formula to successfully predict call center load. The Erlang C formula calculates based on basic information (like the expected number of incidents) how many service representatives (or agents) are needed to meet your desired service level. Erlang C is the standard in the contact center industry.

## Overview

With this Python Class, one can calculate a variety of parameters affecting contact center operations and customer experience. As a general note, Erlang was developed mainly with phone conversations in mind, but to a wide extend can also be used for the same kind of calculations for contact centers that are not phone based, but have channels such as chat, email, social media and messengers. I use transactions where a customer might use any channel, and calls where a customer uses phone.
Some of the calculations are only relevant for voice contact centers, such as the number of Trunk lines (I will call those out that are only relevant for phone).

Here is a list contact center variables that can be calculated using this Erlang Class:

- Number of Agents required to handle a given number of transactions in a given interval;
- Service Level that will be achieved with a number of agents and a given transaction volume;
- Queue times - how long will a customer typically have to wait to get through to an agent;
- Queue size - how many customers will on average be put in a queue given number of agents,  SLA, AHT and other parameters;
- How many interactions will be queued on average given the number of agents, SLA, AHT and other parameters;
- Average Speed to Answer;
- Abandonment Rate;
- Given a call volume, how many Trunk lines are required to achieve SLA, ASA, Abandon and other parameters;
- and more...

# Classes

The Library contains two main classes:

- **Erlang-Base** class contains base modules required by both, Erlang-B and Erlang-C classes;
- **Erlang** class contains all modules required to conduct Erlang-B/-C calculations;

The code was developed on a Mac using OneDrive as the repository. For all includes to work accordingly, the following directory structure would have to be recreated:

`⋅⋅⋅/Users/(username)/OneDrive/Development/Python/Erlang`

---

# Erlang Base Class

## MinMax

MinMax(Eval, Min, Max) - Method evaluates Eval against Min and Max.

**Returns (float)**

- Min if Eval is less than Min
- Max if Eval is larger than Max
- Otherwise Eval

---

# Erlang Main Class

## Introduction

The Erlang Class regards the fact that when using chat or email or other non-voice media an agent can handle more than one transaction at any given time. This fact is controlled by the parameters given to the `__init__(..., nv, ccc,...)` method of the Erlang Class. The parameter `nv`, if it is set to `true`, indicates that the object created from this Class is a non-voice calculation. The `ccc` parameter defines the amount of concurrent transactions agents on average can handle.
> IMPORTANT
>
>The implication of this is that the class cannot be reused for different media types. If, for example one would have to calculate the numbers for a call center, then one would create an object with parameters `nv = false` and `ccc = 1` - meaning voice and concurrent calls = 1.
>If then one would have to calculate the parameters for a chat support group, the previous object of Class Erlang would have to be destroyed and a new object with parameters `nv = true` and `ccc = 3` - meaning non-voice and concurrent transactions = 3.
>Internally, the provided methods will check for these 2 parameters and change calculation methods accordingly.
>The approach taken here is that the given AIT (Average Interaction Time aka ATT - Average Talk Time) is divided by the number of concurrent actions an agent can handle. This effectively is the same result as if the number of agents would be increased to 3 (in this >example); however, the benefit of changing the AIT is that each agent will still have the same after transaction wrap time, so the the result is more precise.

> NOTE
>
> Throughout this document the following terms have the meaning as defined below:
>- **Arrival Rate** is the number of *Transactions* arriving per interval.
>- **Completion Rate** is the number of *Transactions* completed per interval.
>- **Transactions** any transaction that has been initiated by customers. This may be a phone call, an email, a chat session, or social media session, depending on the channels supported by the contact center.
>- **Death Rate** has the same meaning as *Completion Rate*.
>- **Server or Servers** is defined as a single entity or multiple entities which can service transactions, typically an agent.
>- **SLA** is the Service Level that the contact center tries to achieve. SLA would be contractually fixed and is measured in percentage of offered transactions answered in a defined period. For example 80/20 means 80% of transactions need to be answered in 20 seconds.
>- **Utilisation** is the level of time a server or agent is actually delivering work compared to the interval the agent is available. E.g. a 50% utilisation would mean that an agent how is working for 1 hour is only delivering actual work for 30 minutes.
>- **Abandon** defines that a customer contacting the contact center interrupts or abandons the transaction before a server or agent can attend to them. This is typically the case if wait times in a queue are too long.  


The methods of the classes are described below. If you want to learn how to use the Erlang library in your Python code please refer to [TBA]

---

## ErlangB

*ErlangB (servers, intensity)* - The Erlang B formula calculates the percentage likelihood of the call being blocked, that is that all the trunks are in use and the caller will receive a busy signal.

**Parameters**
- `servers`   = Number of telephone lines
- `intensity` = Arrival rate of calls / Completion rate of calls

**Returns (float)** - the percentage likelihood of a call being blocked

---

## ErlangBExt

*ErlangBExt (servers, intensity, retry)* - the Extended Erlang B formula calculates the percentage likelihood of the call being blocked, that is all the trunks are in use and the caller will receive a busy signal. The Extended version allows input of a percentage figure for those blocked callers who will immediately retry.

**Parameters**
- `servers`   = Number of telephone lines
- `intensity` = Arrival rate of calls / Completion rate of calls
- `retry`     = Number of blocked callers who will retry immediately (0.1 = 10%)

**Returns (float)** - The probability in % of a call being blocked.

---

## EngsetB

*EngsetB (servers, intensity)* - the Engset B formula calculates the percentage i of the call being blocked, that is that all the trunks are in use and the caller will receive a busy signal. This uses the Engset model, based on the hindrance formula.

**Parameters**
- `servers`   = Number of telephone lines
- `events`    = Number of calls or transactions
- `intensity` = Arrival rate of calls / Completion rate of calls

**Returns (float)** - the probability in % of a call being blocked.

---

## ErlangC

*ErlangC (agents, intensity)* - this formula gives the percentage likelihood of the transaction (call, chat, social media tx) being placed in a queue.

**Parameters**<
- `agents`    = Number of agents
- `intensity` = Arrival rate of transactions / Completion rate of calls

**Returns (float)** - the probability in % of a transaction being placed in a queue.

---

## NBTrunks

*NBTrunks (intensity, blocking)* - this function has been supplied by Edwin Barendse. This formula gives the number of telephone lines required to handle the high volume traffic in Erlang against a required blocking factor.

**Parameters**
- `blocking`  = blocking factor percentage e.g. 0.10  (10% of calls may receive busy tone)
- `intensity` = Arrival rate of transactions / Completion rate of calls

**Returns (float)** - the number of telephone lines required.

---

## NumberTrunks

*NumberTrunks (intensity, blocking)* - this formula gives the maximum number of telephone trunks required to handle the answered and queuing calls (up to a maximum of 255).

**Parameters**
- `agents`    = Number of Agents
- `intensity` = Busy hour traffic - Arrival rate of transactions / Completion rate of calls

**Returns (int)** - the max number of telephone lines required.

---

## NumberAgents

*NumberAgents (intensity, blocking)* - the formula calculates the number of servers required to service the given traffic intensity with the given blocking factor.

**Parameters**
- `agents`    = Number of Agents
- `blocking`  = blocking factor percentage e.g. 0.10  (10% of calls may receive busy tone)

**Returns (int)** - the number of agents required.

---

## LoopingTraffic

*LoopingTraffic (trunks, blocking, increment, min_int)* - this function tries values from min_int to max_int, increasing the traffic by increment until the approximate blocking is found, processing then loops with stepping of increment/10 (e.g. 10, 1, 0.1, 0.01, 0.001) until the value is found to the precision required (defined by constant MaxAccuracy).

**Parameters**
- `trunks`    = number of Trunk lines
- `blocking`  = blocking factor percentage e.g. 0.10  (10% of calls may receive busy tone)
- `increment` = traffic increase increment
- `min_int`   = Minimum traffic intensity

**Returns (float)** - the appropriate blocking value.

---

## Adandon

*Adandon (agents, transactions)* - this method calculates the percentage of transactions which will be abandoned after the time given.
It regards the fact that when using chat or email or other non-voice media an agent can handle more than one transaction at any given time. This fact is controlled by the parameters given to the `__init__(...)` method of the Erlang Class, refer [here](#Introduction) for more details.

**Parameters**
- `agents`       = number of agents available  
- `transactions` = number of calls received in the interval period
  >**Parameters provided in constructor**
  >- ABANDON TIME the time in seconds before the caller will abandon and is given when creating an object from this Class.
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (float)** - Percentage of calls abandoned within interval.

---

## Agents

*Agents (service_time, transactions)* - calculates the number of agents required to service a given number of transactions to meet a given service level. It regards the fact that when using chat or email or other non-voice media an agent can handle more than one transaction at any given time. This fact is controlled by the parameters given to the `__init__(...)` method of the Erlang Class, refer [here](#intro) for more details.

**Parameters**
- `service_time` = target answer time in seconds e.g. 15
- `transactions` = the number of transactions received in the given interval period
  >**Parameters provided in constructor**
  >- SLA is the % of calls to be answered within the ServiceTime period  e.g. 0.95 (95%) and is given when creating an object from this Class.
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.

**Returns (int)** - number of agents required

---

## AgentASA

*AgentASA (asa, transactions)* - calculate the number of agents required to service a given number of calls to meet the average speed of answer. It regards the fact that when using chat or email or other non-voice media an agent can handle more than one transaction at any given time. This fact is controlled by the parameters given to the `__init__(...)` method of the Erlang Class, refer [here](#intro) for more details.

**Parameters**
- `asa`          = the Average Speed of Answer in seconds.
- `transactions` = the number of transactions received in the given interval period.
  >**Parameters provided in constructor**<br>
  >- SLA is the % of calls to be answered within the ServiceTime period  e.g. 0.95 (95%).
  >- AHT is the call duration including after call work in seconds e.g 180.

**Returns (int)** - Number of agents required per interval to meet ASA

---

## ASA

*ASA (agents, transactions)* - function calculates the Average Speed to Answer (ASA) for the given number of agents.

**Parameters**
- `agents` = number of agents available  
- `transactions` = the number of transactions received in the given interval period.
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (int)** - the average speed to answer in seconds.

---

## CallCapacity

*CallCapacity (agents, service_time)* - function calculates the number of calls which can be handled by the given number of agents whilst still achieving the grade of service.

**Parameters**
- `agents` = number of agents available  
- `service_time` = target answer time in seconds e.g. 15
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- SLA is the % of calls to be answered within the ServiceTime period  e.g. 0.95 (95%).
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (int)** - the average speed to answer in seconds.

---

## FractionalAgents

*FractionalAgents (service_time, transactions)* - function calculates the number of calls which can be handled by the given number of agents whilst still achieving the grade of service.

**Parameters**
- `service_time` = target answer time in seconds e.g. 15
- `transactions` = the number of transactions received in the given interval period
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- SLA is the % of calls to be answered within the ServiceTime period  e.g. 0.95 (95%).
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (int)** - the average speed to answer in seconds.

---

## FractionalCallCapacity

*FractionalCallCapacity (service_time, agents)* - function calculates the number of calls which can be handled by the given number of agents whilst still achieving the grade of service.

**Parameters**
- `service_time` = target answer time in seconds e.g. 15
- `agents` = number of agents available
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- SLA is the % of calls to be answered within the ServiceTime period  e.g. 0.95 (95%).
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (int)** - the average speed to answer in seconds.

---

## Queued

*Queued (agents, transactions)* - function calculates the percentage of calls which will queue for the given number of agents.

**Parameters**
- `agents` = number of agents available
- `transactions` = the number of transactions received in the given interval period
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (float)** - the percentage of calls which will queue for the given number of agents.

---

## QueueSize

*QueueSize (agents, transactions)* - function calculates the average queue size for a given number of agents.

**Parameters**
- `agents` = number of agents available
- `transactions` = the number of transactions received in the given interval period
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (int)** - the average queue size for a given number of agents.

---

## QueueTime

*QueueTime (agents, transactions)* - function calculates the average queue time for those calls which will queue.

**Parameters**
- `agents` = number of agents available
- `transactions` = the number of transactions received in the given interval period
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (int)** - the average queue time for those calls which will queue.

---

## ServiceTime

*ServiceTime (agents, transactions)* - function calculates the average waiting time in which a given percentage of the calls will be answered.

**Parameters**
- `agents` = number of agents available
- `transactions` = the number of transactions received in the given interval period
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.
  >- SLA is the % of calls to be answered within the ServiceTime period  e.g. 0.95 (95%).

**Returns (int)** - the average waiting time in which a given percentage of the calls will be answered.

---

## SLA

*SLA (agents, transactions)* - function calculates the service level achieved for the given number of agents.

**Parameters**
- `agents` = number of agents available
- `transactions` = the number of transactions received in the given interval period
  >**Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (float)** - the service level achieved for the given number of agents.

---

## Trunks

*Trunks (agents, transactions)* - function calculates the number of telephone lines required to service a given number of calls and agents.

- **Parameters**
- `agents` = number of agents available
- `transactions` = the number of transactions received in the given interval period
  >- **Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (int)** - the number of telephone lines required to service a given number of calls and agents.

---

## Utilisation

*Utilisation (agents, transactions)* - function calculates the utilisation percentage for the given number of agents.

- **Parameters**
- `agents` = number of agents available
- `transactions` = the number of transactions received in the given interval period
  >- **Parameters provided in constructor**
  >- AHT is the call duration including after call work in seconds e.g 180 and is given when creating an object from this Class.
  >- INTERVAL is the forecasting interval 15, 30, 45, 60 minutes and is given when creating an object from this Class.

**Returns (float)** - the utilisation percentage for the given number of agents.
