# ssr_stage

This package contains the files needed to run stage simulations with multiple robots

## The Launch Files:
These are the launch files for the stage simulation

To use a simulation, include the desired simulation launch file in your main robot control launch file.

Example:
```xml
    <include file="$(find ssr_stage)/launch/field_empty.launch"/>
```
* field\_empty.launch
	* launches a Stage simulation of the field with no robots and no obstacles

* field\_obstacles.launch
	* launches a Stage simulation of the field with no robots and few obstacles

* single\_bot\_empty.launch
	* launches a Stage simulation of the field with only one robot and no obstacles. For pathfinding test
	* control by rostopics

* single\_bot\_obstacles.launch
	* lanuches a Stage simulation of the field with only one robot and few obstacles. For pathfinding test
	* control by rostopics
