---
layout: post
title:  "Designing Data Intensive Applications"
date:   2020-01-13 16:33:19
author: Kwanghee Choi
categories: system_design
---

# Overview & Disclaimer


# Preface
- Driving forces for recent development of data-intensive systems
	- Big IT companies handling huge volumes of data
	- Spread of agile methodologies
	- Free and Open source S/W
	- CPU clock speed is barely increasing, so speeding up services depends more on multi-core processing & faster networks.
	- IaaS (ex. AWS) based on distributed machines
	- High availability of services became the standard.
- Application is called data-intensive if data is its primary challenge.
	- Quantity, complexity, speed

# Chapter 1. Reliable, Scalable, and Maintainable Applications
- Data systems are successful abstractions. We never design systems from scratch.
	- ex. Store data to find it again later == Databases
	- You can create a new, special-purpose data system from smaller, general-purpose components.
- Reliabilty
	- The system should continue to work correctly even in the face of faults and errors.
	- It only makes sense to tolerate and prevent feasible types of faults to avert failures.
	- Hardware Faults
		- More machines used == More hardware faults.
		- Cloud platforms are designed to prioritize flexibility and elasticity (ex. AWS ELB) over single machine reliability.
		- Systems can tolerate loss of entire machines, using software in addition to hardware redundancy.
	- Software Errors
		- Bugs that causes systematic error often lie dormant for a long time until they are triggered by uncommon circumstances, which violates various assumptions about the environment when software is made.
		- Hardware faults are usually independent. Software errors aren’t.
	- Human Errors
		- Humans are known to be unreliable.
		- System should be designed to minimize opportunities for errors.
		- Errors will eventually arise, so thorough monitoring and quick recovery are important.
	- We may choose to sacrifice reliability over others, but nevertheless should be very conscious of it.
- Scalability
	- As the system grows, there should be reasonable ways of dealing with it.
	- Load
		- Load can be described with load parameters.
		- ex. 4.6k req/s on average (Average case), over 12k req/s at peak (Extreme case)
	- Performance
		- ${ {Resource} \over {Load}} = Performance$
		- Metrics example: Average, Median (p50), p95, p99, p99.9
		- Response time = Latency + Processing time
		- Reducing response times at high percentiles (Tail latencies) is important, because it directly affects user experience. But it is difficult as percentiles increase, as the metric is easily affected by random events outside of your control.
	- Good architectures usually mixes both scale-up and scale-out techniques. There is no such thing as a silver bullet architecture.
	- Systems that cover 1 kB/req $\times$ 100,000 req/s $\neq$ Systems that cover 2 GB/req 3 req/min
	- Architecture that scales well is built around business-dependent assumptions - which operations will be common or rare - the load parameters.
- Maintainability
	- People should be able to maintain and adapt the system productively.
	- Majority of software development cost comes from ongoing maintenance.
	- Good operability means making routine tasks easy, allowing the operations team to focus on important tasks.
	- Simplicity: Managing complexity of systems by extracting parts into well-defined, reusable components.
	- Evolvability: Agility on a system level. ex. How would you refactor Twitter’s architecture?
