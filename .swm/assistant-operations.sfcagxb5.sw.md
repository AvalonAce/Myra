---
title: Assistant Operations
---
## Introduction

This doc gives a high level overview of how Myra can complete operations from commands/queries.

## Main Files

The main files that the assistant uses to complete operations are:

- <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath>
- <SwmPath>[command/Simple_Requests.py](/command/Simple_Requests.py)</SwmPath>
- <SwmPath>[command/Sys_Interaction.py](/command/Sys_Interaction.py)</SwmPath>

## Simple Requests

<SwmPath>[command/Simple_Requests.py](/command/Simple_Requests.py)</SwmPath>acts as the file containing any operational functions that Myra can use which are 'simple'. This can include telling the date, current weather, math operations, etc. All simple requests should be implemented in the file.

## System Interactions

<SwmPath>[command/Sys_Interaction.py](/command/Sys_Interaction.py)</SwmPath>acts as the main file containing any system interaction functions that Myra can use. Examples include opening files, starting programs, etc. Any actions that the user wishes do which involves interacting with the computer should be implemented in this file.

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
