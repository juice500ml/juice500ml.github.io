---
layout: post
title:  "The Essense of Object Orientation"
date:   2019-02-16 02:50:44
author: Kwanghee Choi
categories: software_design
---

# Overview & Disclaimer
This is a summary of the book [The Essense of Object-Orientation: Roles, Responsibilites, and Collaborations (객체지향의 사실과 오해: 역할, 책임, 협력 관점에서 본 객체지향)](http://wikibook.co.kr/object-orientation/). Views of this book are well-know to be both surprisingly deep and refreshing, and happily for me, quite kind for beginners like myself. Unfortunately, it was originally written in Korean, and there is seemingly no translation available in English. That is the reason why I’m trying to summarize this book in English, as clearly as possible, hoping a much bigger audience can cherish this book and the ideas from it. But keep in mind that, as myself is far from being a professional to this subject, this summary may contain ambiguous, or potentially hazardous ideas and expressions. Special thanks to [Jisoo Kim](https://blog.jisoo.net), who recommended me this book, and [Dongho Jung](https://github.com/0xB4DF4C3D), who reviewed and summarized this book together.

# 0. Foreword
- The concept of *object-orientation* brings a lot of controversy in software communities, despite the fact that the concept had been widely used for decades. This phenomena tells us that there is no unified definition, or realization of the concept.
- That said, few of the possible ideas:
	- OO is *object* oriented, not *class* or *inheritance* oriented.
	- Object is not an independent existence of its own, but a *collaborative community to implement a function*, that each object has an adequate amount of *roles* and *responsibility*.
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
		- How to take responsibility is autonomously selected. Same request, different choice of response: polymorphism. (Barista brews coffee on his/her own terms. State-dependent behavior difference, or overidden behavior.)
		- One object can have multiple roles. (Cashier could also brew coffee. May have multiple roles depending on collaborative situations.)
- Object should be...
	- Open: Friendly enough to collaborate. Open to requests and responses.
	- Autonomous: with own principles and control.
	- To ensure openness and autonomy, object is binded with behavior (the way how object can collaborate with other objects) and state (data needed for behaviors inside the object).
	- ex) Barista has to be friendly enough to give choices to customers (message-recievable), but customers doesn’t get to dictate how barista brews coffee (method encapsulation).
		- Open: Customer (sender) sends a message (make a request) to the barista (reciever). Barista recieves a message from the customer (and prepare to make a response).
		- Autonomous: Customer can know *what* barista is brewing, but does not have to know *how*.
- OO is not about classes. It is about autonomous objects messaging each other. It is about maintaining collaborations between roles with responsibilities. Classes are just tools to implement those.

# 2. Object in Wonderland
- OO takes advantage of innate human ability of seeing the world as a set of independent and perceivable objects.
- Alice in Wonderland analogy
	- Alice changes her height by eating various magical food, to achieve something, like go through a small door, or eat a large cake.
- Everything is an object if it is...
	- Perceivable (human-tractable) as a single independent (seperable to other objects) unit
	- Can determine the time of creation (instantiation)
- Object
	- Definition: Identifiable stuff. Could be real or abstract.
	- Object contains state, behavior, and identifier.
		- Object has a state which is changeable. (The height of Alice is changeable.)
		- How object behaves changes the state of herself. (Alice changes her height by doing something.)
			- Result of the behavior is state-dependent, and result can be explained only with the state of the object.
			- Result is dependent of the order of behaviors.
		- No matter what state is in, Alice is uniquely indentifiable. (No matter how tall Alice is, Alice is Alice.)
- State
	- Definition: State is the total information that the object has in a given time.
	 -State consists of property (static) and property value (dynamic). Property can be attribute (value) or link (instance of correlation between other object).
	- Values (number, string, datetime, ...) are not objects, as they are not uniquely identifiable. But values provides ways to express the state of an object.
	- State is an abstraction of all the previous behaviors to reduce the complexities of the real-world.
	- Object has, and should be on full control unto its own state, hence the autonomy. State and behavior are bind to one unit: an object.
- Behavior
	- Definition: Doing stuff to respond to incoming messages.
	- Behavior changes state (side effect), and behavior depends on state.
		- Behavior has two kinds of side effect: own state change (changing the property value), and message request to other object (via link).
		- Every meaningful statement has a side effect.
		- Object can change its state (side effect inside the object), or give out responses (side effect outside the object).
	- Behavior is the only way for an object to participate in collaborations.
	- State encapsulation
		- Only behaviors are visible, states are invisible (from the outside). The only way to manipulate states is via behaviors.
		- As the object becomes more autonomous, it gets more intelligent. In other words, collaboration gets more flexible and concise.
- Identifier
	- Object (reference object, entity) vs. Value (value object)
	- Identifiability
		- Object is uniquely identifiable. == Object has a specific property (identifier) that makes itself distinguishable to other objects.
		- Value is not uniquely identifiable. == Value does not need an identifier.
	- Mutability
		- Value models unchanging amounts. Its state never changes. (Immutable state) Therefore, *equality* depends on the state of each values.
		- State encompasses changing state depending on time. (Mutable state) Therefore, two objects are *identical* if identifier is the same.
- Object as a machine
	- *Query* the state of the object, and *command* to change the state of the object. No other interface to interact with the object.
- Collaboration decides what behavior (in other words, role and responsibility while collaborating) is needed. What state to manage is decided after the behavior is set.
- Real-world objects are passive. Software objects are active. They can do much more stuff than real-world objects. They acts as if they are live beings. (Anthropomorphism)
- Real-world objects are just metaphors for software objects, minimizing the representational gap.

# 3. Type and Abstraction
- London metro analogy
	- If you think about the purpose of the subway map, you can easily rule out the geographical accuracy, and concentrate more on showing the connection between stations effectively.
- Use abstraction, or disintegrate and simplify, to make this world easier and predictable, and hence, understandable.
- Abstraction is ...
	- Dimension 1: Generalization between specific objects: Commonness chosen, difference discarded.
	- Dimension 2: Remove the unimportant details to emphasize the important parts.
- Levels, benefits, values of abstraction is purpose-dependent.
- Classification: Abstraction by groups (or, concepts / types)
	- Each object has features that can be used to clearly differentiate between other objects.
	- Use common features (a concept) to *classify* objects, hence reducing the complexity of perception: objects to groups.
	- Object is an *instance* of a concept (when the concept is applicable to the object).
		- Symbol: Name for a specific concept.
		- Intension: Complete definition of a concept. Determines whether or not the object is of a concept.
			- Classification of objects is essentially checking the applicability of specific concepts to each object.
		- Extension: Set of all objects inside the concept.
	- Choosing the common features (Dimension 1) effectively remove the unimportant details (Dimenison 2), hence the success of abstraction.
- Responsibility-driven: Abstraction by decoupling What and How
	- Data type
		- Computer memory is typeless; every data is represented as a bit string.
		- Type system: Classifying these bit strings to serve a specific purpose.
			- Defining constraints of how to read and manipulate those bit strings.
			- ex) Let’s define these consecutive 8 bits as *int*, and define various operations on it. Now, there is no need of knowing how *int* is stored in the memory.
		- Data type is a metadata to classify various bit strings, which implicitly defines what kind of operations are applicable to that bit string.
	- Data types are analogous to types of objects
		- Type of the object is chosen by how object operates. (Polymorphism, Duck typing, What it does)
			- ex) Operates the same = Same responsibilities = Same message (but may have different response)
		- Type of the object is regardless of internal implementations. (Encapsulation, How is it implemented)
			- ex) Objects of the same type can handle same messages, regardless of internal data.
	- Responsibility-driven Design (vs. Data-driven design)
		- Choose responsibilities (operations) first, then choose the internal data to manage the responsibilities.
- Hierarchy of types: Responsibility(behavior), not data(state), decides the hierarchy.
	- A is a generalization of B (Dimension 2: Remove features to define A), B is a specialization of A (Dimension 1: Commonness chosen to define B).
		- Extension of A $\supset$ Extension of B
		- Intension of A $\subset$ Intension of B
		- A is a supertype of B, B is a subtype of A.
- Classification and Type Hierarchy (Generalization & Specialization) are tools for Abstraction.
	- Classification defines a filter, Generalization/Specialization adjusts strength of a filter.
	- The result of classification on a superclass is a subclass.
- Type (which can display properties) is an abstraction for dynamic characteristics (dynamically changing property values) of objects.
	- Dynamic model (Object diagram, shows multiple snapshots of objects) vs. Static model (Type diagram, shows every possible behaviors and states, which is an abstraction of multiple snapshots)
- Class is a way to implement a type.
