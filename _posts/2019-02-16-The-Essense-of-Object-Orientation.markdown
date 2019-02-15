---
layout: post
title:  "The Essense of Object Orientation"
date:   2019-02-16 02:50:44
author: Kwanghee Choi
categories: software_design
---

# Overview & Disclaimer
This is a summary of the book [The Essense of Object-Orientation: Roles, Responsibilites, and Collaborations (객체지향의 사실과 오해: 역할, 책임, 협력 관점에서 본 객체지향)](http://wikibook.co.kr/object-orientation/). Views of this book well-know to be both surprisingly deep and refreshing, and happily for me, quite kind for beginners like myself. Unfortunately, it was originally written in Korean, and there is seemingly no translation available in English. That is the reason why I’m trying to summarize this book in English clearly as possible, hoping a much bigger audience can cherish this book and the ideas from it. But keep in mind that, as myself is far from being a professional to this subject, this summary may contain ambiguous, or potentially hazardous ideas and expressions. Special thanks to [Jisoo Kim](https://blog.jisoo.net), who recommended me this book.

# 0. Forwords
- The concept of *object-orientation* brings a lot of controversy in software communities, despite the fact that the concept had been widely used for decades. This phenomena tells us that there is no unified definition, or realization of the concept.
- That said, few of the possible ideas:
	- OO is *object* oriented, not *class* or *inheritance* oriented.
	- Object is not an independent existence of its own, but a *collaborative community* to implement a function, that each object has an adequate amount of *roles* and *responsibility*.
- Contents for each chapters
	- Chapter 1 argues that the essense of OO paradigm is, *autonomous objects collaborating*.
	- Chapter 2 tries to answer the fundamental question of "What is an *object*?".
	- Chapter 3 covers *abstraction*, or more simply put, simplyfing dynamic objects to static types.
	- Chapter 4 explains fundamental materials of OO: *roles, responsibilities, and collaborations*. Each object have a specific role for collaborations, and take responsibilities of that role.
	- Chapter 5 emphasizes that *messages* can assure the autonomy of an object and flexibility of design.
	- Chapter 6 shows two aspects of OO: *structure and function*. Structure is more robust to changing circumstances than function.
	- Chapter 7 encompasses the previous chapters by looking through the implementation details written in code.

# 1. Collaborative Community of Objects
- OO is not about mimicking real-world objects, but more about creating a whole new world that can satisfy users.
- Humans are analogous to objects.
	- Humans think and decide automously, objects autonomously encapsulate states and behaviors.
	- Humans make both implicit and explicit contracts to collaborate for a common goal, objects message each other to collaborate for a single functionality.
- Coffee shop analogy
	- Customer orders coffee, cashier gets orders, barista brews coffee.
	- Coffee is transported back from barista, cashier to customer.
	- Collaborations are made with requests and responses.
		- Requests are made from customer to cashier (order coffee), cashier to barista (brew coffee).
		- Responses (coffee) are made, in the opposite direction to requests.
	- People (objects) are granted with roles to collaborate. Roles implicitly involves responsibilities.
		- Roles do not depend on realization of each objects, hence substitutable. (Customer doesn’t care who gets the coffee.)
		- How to take responsibility is autonomously selected. Same request, different ways of response: polymorphism. (Barista brews coffee on his/her own terms.)
		- One object can have mutiple roles. (Cashier could also brew coffee.)
- Object should be...
	- Open: Friendly enough to collaborate.
	- Autonomous: with own principles and control.
	- To ensure openness and autonomy, object is binded with behavior (object behaving to collaborate) and state (data needed for autonomous behavior).
	- ex) Barista has to be friendly enough to give choices to customers (message-recievable), but customers doesn’t get to dictate how barista brews coffee (method encapsulation).
		- Open: Customer (sender) sends a message (make a request) to the barista (reciever). Barista recieves a message from the customer (and prepare to make a response).
		- Autonomous: Customer can know *what* barista is brewing, but does not have to know *how*.
- OO is not about classes. It is about autonomous objects messaging each other. It is about maintaining collaborations between roles with responsibilities. Classes are just tools to implement those.
