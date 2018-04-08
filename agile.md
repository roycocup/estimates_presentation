# Agile

## Agile Manifesto
- **Individuals and Interactions** over processes and tools

- **Working Software** over comprehensive documentation

- **Customer Collaboration** over contract negotiation

- **Responding to Change** over following a plan

## Principles behind the Agile Manifesto
1. We follow these principles:
Our highest priority is to satisfy the customer
through early and continuous delivery
of valuable software.

2. Welcome changing requirements, even late in
development. Agile processes harness change for
the customer's competitive advantage.

3. Deliver working software frequently, from a
couple of weeks to a couple of months, with a
preference to the shorter timescale.

4. Business people and developers must work
together daily throughout the project.

5. Build projects around motivated individuals.
Give them the environment and support they need,
and trust them to get the job done.
6. The most efficient and effective method of
conveying information to and within a development
team is face-to-face conversation.

7. Working software is the primary measure of progress.

8. Agile processes promote sustainable development.
The sponsors, developers, and users should be able
to maintain a constant pace indefinitely.

9. Continuous attention to technical excellence
and good design enhances agility.

10. Simplicity--the art of maximising the amount
of work not done--is essential.

11. The best architectures, requirements, and designs
emerge from self-organizing teams.

12. At regular intervals, the team reflects on how
to become more effective, then tunes and adjusts
its behaviour accordingly.

## Explanation
- [What is it - By Ron Jeffries](https://ronjeffries.com/articles/018-01ff/agile-riff/)

- [Neal Ford and Martin Fowler - Agile](https://www.youtube.com/watch?v=GE6lbPLEAzc)
    - Its hard to take agile serious, but in the last 10 years its become the mainstream alternative (conference and certificates...)
    - (**Semantic Diffusion**) The original ideas get more and more diffuse and fuzzy as they pass on people. Some companies are employing **unrecognisable agile ideas** now as they adapt some concepts. Sometimes they have been doing agile for years and its unrecognisable. Its a common problem. The solution is reminding people of what are the core ideas of agile.
    - [The new Methodology by Martin Fowler](https://martinfowler.com/articles/newMethodology.html)
    - In this last essay MF distinguishes 2 key features between agile world and plan-driven world.

## Plan-driven world
- In the plan-driven, plan is essential before starting whatever it is that you are about to do. **Plan your work, then work your plan**. A predictive approach towards planning in which the plan is a prediction of how the work should go.
- It also is the measures the success of a work, as it went according to the plan (On time and on budget).
- Useful in many situations, but **depends** on the fact that you are able to get a a **clear and stable set of requirement**
- If they are not clear, the rest of the plan is not stable. Not just the plan, but the entire software development process.
- This is a problem: Are you requirement stable? Its a minority.
- In order to stabilise they come up with all sort of techniques (sign-off, code freeze, up-front requirements, etc...)

## So...
- Maybe what we should need is to break that dependency where the entire software development process is dependent on the stability of the requirements.

## Agile World
- We can't get stable requirements. and come up with a software development process that is **tolerant** to requirement changes.

### Adaptative Planning
- "A late change in requirements is a competitive advantage" - Mary Poppendieck Author of Lean Software Development.
    - We should not just expect change in requirement, but that we should embrace change as it will bring competitive advantage to our clients!
    - How do we do this? We don't just plan and execute the plan. We use whats called an **Adaptative Planning** approach which means we do this cycle of planning and execution many many times on a project (iteration or sprints) and we look to release the software at regular intervals.
- In order to make Adaptative Planning work we need to change the way we thing about **software design with evolutionary approach**
- The design is something that is also constantly evolving and changing as you go. [Lots of techniques](https://www.martinfowler.com/articles/designDead.html) One of the common problems in running agile approaches is that companies take the project management part of agile but not the technical part of agile (Self-testing code, Continuous integration, Refactoring, [Simple Design](https://www.martinfowler.com/bliki/BeckDesignRules.html)). Companies have a great deal of problem doing this because they dont make **code that is designed to change**. This is particularly a problem for companies following the "scrum approach" as they tend to forget the technical sides of agile.

### People first
- Frederick Winslow Taylor - "In the past man was first: In the future the system must be first." - People who do the work should decide how to do the work and that should change and a separate pgroup of people should decide people should then conform and follwo. This influeced how we do work in the 20th century and also in the software world.
    - When working on a project, we find some human resources, who fit into the rough categories of the process and we slot them into the various places within the process.
- [Alistair Cockburn - Characterizing people as Non-Linear First Order Components in Software Development](http://alistair.cockburn.us/Characterizing+people+as+non-linear%2c+first-order+components+in+software+development) The key elements of software development are people and we are not predictable and highly [See here](./people.md) So we need to think very carefully when we have people fit into the process. In fact rather than fitting the people into the process, we reverse this and get a good group of people who can work effectively together [ron jefferies - so-so technical people do better jobs than highly technical ones] and they chose the process that they follow.
- Process first and people fit in vs people come first they decide what process is the most effective.
- A bad process will beat good people every time - W. Edwards Demming. The process can stiffle even good people

### Communication
- People are social beings
- [Effective of communication channels] (https://blog.coryfoy.com/wp-content/uploads/2014/02/communicationeffectiveness.gif) The most effective way you can comunicate is two people and a whiteboard because you can see tone, facial expressions, body posture, ask questions and answer and drawings. Emails or paper require people to come up with very elaborate ways to convey information which explains why outsourcing fails most of the times. Software is very nuanced thing and trying to communicate those nuances is very hard. Why is it illegal to speak on the phone while driving but its not to talk to the person next to you. Because the brain is reconstructing the messages that exist when you have a face to face communication. This is why in agile we prefer **Individuals and interactions** over processes and tools AND **Customer Collaboration** over contract negotiation
- [Effectiveness of Communication](http://www.agilemodeling.com/essays/communication.htm) Where extensive documentation would show up as the least effective way to communicate the idea behind the code.

### Feedback
- Fruitcake and taking a shower in a hotel room you never been in before.
    - Two forms of process: Empirical Process and the Defines Process. We have some inputs and controls > a process and an output (or outcome)
    - When we work in the world of the defined process, we understand the process - ingredients, combine, oven and almost every time comes out the same Fruitcake. Well understood, run it and get the output.
    - In the shower we need to take the other process. We don't really know where that dial is in terms of the heat of the shower. Turn the shower, stick my hand in, is it warm, hot or cold, if its ok I go in, maybe in the beginning its ok but as I go maybe I want that shower a little hotter (25m) and adjust the shower. **I'm looking at the output**. Inspecting the output and then adjusting the inputs based on what the outputs are. And thats because I'm dealing with something that is much less known.
    - You have to use the right kind of definition for the right kind of process. If you have a chemical plant and you know all the inputs and how everything operates well, then you can **and should use** the defined process. But **if there are unknowns and uncertainties** involved then using the defined process is actually dangerous. Instead you have to use an Empirical process.
    - In software we have all these unpredictable, non-linear componenets called "people" laying around. So you can't use the defined process. So you need to use and **empirical process and you need some way to inspect the output**.
    - You also need to put the process in some **feedback loop** to affect how you are doing things. Thats why feedback is central to agile and in agile we are always looking on ways to introduce feedback loops into our software development approach.
        - Post its on the walls of thoughtworks in Honk Kong as feedback for the projects that are going on. Where we are in the several projects that we have. Not just visible to the project managers but rather everyone. But in agile you want everyone to be participating, so everyone needs to be able to see whats going on. In waterfall the plan can be somewhat hidden from the developers and it becomes somewhat of a myth. Most teams prefer the physical walls, but an electronic one is often necessary if you have teams in separate places and you want everybody in on whats going on.
        - Also important is knowing where we are in terms of the build system. In agile there is a only one way to **measuring progress and that is by working software**. So its fairly important to monitor the status of builds and for that we may use many differen tools, including circleCI but other such as [GoCd](https://www.gocd.org/)
        - The idea of testing as a fedback loop to constantly question if we are building softwre that builds effectively by layer upon layer of testing. In the early stages we start by testing very fine grained and quick operations **(unit tests)** and then later we use longer and more forceful tests such as end-to-end acceptance and performance tests. And we do this at the same time as the project so we have a constant feedback loop for the quality of the project.
        - Pair programming which is very controversioal but there are many reasons why its effective. Left part of the brain which is todo with the more logical and orderly part. And the right side of the brain is to do with creativity. [See Andy Hunts book - Pragmatic Thinking and Learning ](https://pragprog.com/book/ahptl/pragmatic-thinking-and-learning)So in pair programming typically the person who is typing on the keyboard is more on the logical part. They are thinking of "how do I make this work". But the person participating with them (aka Navigator) their brain is thinking in much broader terms and typically in the "why" that goes with the persons on the keyboard "how". This is important because often when you are too focused on making something work you are worried about the path to get there. It takes someone with a little bit of distance that can lead the path for the whole construction to happen. Technically the idea is that instead of having just one side of the brain working at a task, you get the 2 halfs or 1 full brain at the operation. **So pair programming is a constant pair review feedback loop**.
        - Perfect is not a adjective, its a verb.- Kent Beck (XP, TDD, Agile) Perfection is not something we achieve is something we constantly doing. So every so often in agile teams we do restrospectives - Where we look at our software process and we say: how well is it working? what are the things we are doing well and struggling with? What things are puzzling us? How do we change our process to take advantage of these things.
