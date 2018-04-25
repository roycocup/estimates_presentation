Estimation is Evil
Overcoming the Estimation Obsession
by Ron Jeffries
Generic image illustrating the article
   What you don’t know can hurt you, especially when you convince yourself that you do know it.   
Many Agile teams—I believe it’s most Agile teams—get some improvement from applying Agile values, principles, and practices.

These teams do a better job of predicting when they’ll be done, and a better job of being done at the time they predict. They break requirements down into a backlog, they estimate how long items will take, and they burn through that backlog pretty well. Usually by the predicted end of the project, they’re closer to done than they used to be before they went Agile.

Agile teams break down their work into a couple of weeks at a time, and often estimate that work. They usually get done most of what they predict they’ll get done in that iteration. They don’t get too many defects coming back, and they meet regularly to try to improve.

These teams get better transparency, inside the team and with their management and stakeholders. They come closer to shipping on time than they used to. They have fewer defects when they ship. Their management feels that they have more control over what happens.

Teams applying Agile ideas almost always get some improvement. I’d guess that the overall improvement due to Scrum—the most popular Agile approach—is about twenty percent better than what they were doing before.

Some teams do much better, and we’ll talk about what they do later on. Teams that are getting good but not great results are our main concern here, because there are some common elements to what they do, common elements that are holding them back.

These teams are better than they were, but are still undistinguished. Undistinguished teams often seem to have an excessive concern for one or more of these things:

Completing a pre-defined backlog of work;

Delivering everything they’re asked for by a fixed date;

Estimating what they can do every two weeks and keeping to their promises;

Improving the quality of their estimates;

Explaining discrepancies between estimates and actuals;

Improving velocity, their rate of producing features.

In short, these teams are often excessively concerned with estimation, and with living up to their estimates.

These concerns are understandable. Most organizations’ experience with software development is not good. Promises were made and not kept. Projects that were supposed to be done on a certain date dragged on and on, burning valuable time and money. When products finally got done enough to ship, they didn’t meet the vision of those who had asked for them. When users began to use them, they discovered seemingly stupid errors and omissions.

Software development has been quite disappointing to almost everyone who encounters it. That’s why we read about things like the “software crisis” all the time.

It seems quite natural, then, that we would demand that software developers get better at predicting when they’ll be done. It makes sense that we’d use the additional transparency of Agile methods to keep an eye on development, and to hold their feet to the fire, to be sure that they get done what they have promised. It’s only reasonable to demand that they learn to estimate better and learn to hit their estimates. It’s good business to demand that they go faster.

It seems natural. It makes sense. It’s only reasonable. It’s good business. The only problem is: it’s wrong. These are the things that cause an Agile project to be only about twenty percent better than whatever was going on before. Let’s look at why these things hold us back, and at what to do instead.

Starting with All Our Requirements Is Wrong
Most of us were taught to write down all our requirements at the very beginning of the project. There are only three things wrong with this: “requirements,” “the very beginning,” and “all.” At the very beginning, we know less about our project than we’ll ever know again. This is the worst possible moment to be making firm decisions about what we “require.”

Anyone who has ever looked at a list of “requirements” has seen some items that were very important, and some that were—well—not so important. Not so important like 1/100th as important as the most important things. Not so important like downright bad ideas. There is a very strong “80-20” rule at work in requirements lists. The bulk of the value comes from a very small subset of the so-called requirements. So these other things aren’t “requirements” at all. They’re ideas, and some of them are not very good. How could they all be good? We made them up before we began the project, when we knew the least.

Worse yet, when we write down our “requirements,” we act like this is our very last chance to ask for anything. So we ask for everything we can think of, everything we might need. We’re pretty sure we won’t get it all anyway, so let’s ask for a lot and hope we get something we can live with.

Estimating When We’ll Be Done Is Wrong; Forcing the Answer Is Worse
Then we demand that the developers “estimate” when they’ll be done with all this stuff. They, too, know less about this product than they ever will again, and they don’t understand most of these requirements very well. But they do their best and they come up with a date. Does the business accept this date? Of course not! First of all, it’s only an estimate. Second, clearly the developers would leave themselves plenty of slack—they always do. Third, that’s not when we want it. We want it sooner.

So we push back on the developers’ estimate, leaning harder and harder until we’re sure we’ve squeezed out all the fat they left in there. Sometimes we even just tell them when they have to be done.

Either way, the developers leave the room, heads down, quite sure that they have again been asked to do the impossible. And the business people write down the date: “Development swears they’ll be done November 13th at 12:25PM.”

I’m pretty sure no one in the room believes that date. If some people do, I’d like to get a gig going around betting with them against the date. I’m pretty sure I’d be driving a Ferrari real soon now, because this date can’t possibly be right. It’s based on an unrealistic list of requirements, using weak estimates, made at the moment of maximum ignorance, by people who are always optimistic about their own abilities. It has been squeezed down by managers who think they need to be tough, and sometimes it is just overridden by someone who has made a rash promise to someone higher up the food chain.

It’s all right, though. We’ll just keep the pressure on, and they’ll do fine.

Except that they rarely do fine, even in an Agile context. Let’s look at what happens.

Agile Teams Work in Short Iterations; They Pick an Amount of Work that They Forecast They Can Accomplish
Agile processes usually proceed in iterations or “Sprints” of a couple of weeks duration. Every iteration, the team works with their “Product Owner” to select the work for the upcoming iteration. They are supposed to choose an amount of work that they forecast they can accomplish in that time. The emphasis is on “choose.”

Too often, their Product Owner, or a member of management, expresses disappointment with the amount they pick, and encourages them, urges them, or demands that they take on more work. “People need stretch goals,” one of those people said to me when I asked why they had done that.

Does it surprise you to know that if a team has more work thrust upon it than they think they can accomplish, they generally fall short? It shouldn’t. Does it surprise you to know that it is common, only two weeks after someone pushed more work on them, that same someone expresses disappointment that the team has “broken its promise?” It shouldn’t.

Having Demanded the Impossible, Management Asks for Better Estimates
To no one’s surprise, having been overloaded, the team falls short. Nonetheless, management tells the team that they need to improve their estimates. What management really means is that estimates are promises—even forced estimates—and the team needs to keep their “promises,” even if they never promised. The team accomplishes all that it can accomplish. Then management tries to force the team to do more than they can do, demanding that the team “become more productive,” which means “go faster, promise more, and get it done.”

Teams that are asked to do more than they can do will say, “We’ll try.” And they will try. This rarely works out well. To be sure of getting done, they’ll begin to over-estimate everything. In order to get done quickly, they’ll cut back on important aspects of work you can’t see. It’s like sweeping the dirt under the rug. They’ll do a little less testing than was needed. It’s OK, we’ll get a bug report and fix it then. They’ll keep the code a little less clean than it needs to be. It’s OK, we’ll clean it up later, and it won’t slow us down much.

Why should you care? You should care because the defects won’t show up until near the end of the project, or even after the project is released to users. Then you’ll have to do the work that should already have been done to make the code work. You should care because as the code gets worse, the work becomes more difficult and the team slows down. In addition, as the code gets worse, even more defects slip in.

All these things result in a product that is late, delivers less than it might have, has more defects than it needed to have, and that will cost more to maintain than it should have.

“OK, Captain Negative, these things are abuses. But there are legitimate needs for estimates and prediction, so why not rage against the abuses and get on board with the good aspects?”

“What are those good aspects, again? I’ve forgotten.”

“Well. Um. We need to know how long the project is going to take to get done. We need to know how much it is going to cost. So we need to estimate all the requirements and see how many people we need, how much time, and how much money. Then we’ll know when we’re running late and we can, um, do something.

“And, um. Our teams work in iterations. They have to know how much work to take on, and to do that, they need to estimate. And obviously we want them to get better at knowing how much work to take on, so we’ll measure their performance against their estimates and when they fall short we’ll get them to improve.”

There’s our problem: this slope is very slippery. Let’s consider first long-term planning, and then short-term planning.

One of the best-known long-term Agile projects was Chrysler’s C3 payroll, the first Extreme Programming project.

I was once present for an exchange between Sue Unger, then CIO of Chrysler Corporation, the highest-ranking IT executive I’ve ever met, meeting with the C3 team. Kent Beck had just explained how we’d be working in iterations of a few weeks duration, building whatever our “Customer,” Marie DeArment, asked us to build. Ms. Unger asked “How will I know whether you’re on track or not?”

Kent held up our stack of story cards for the payroll. “Here are all the things we have to do. We’ll be adding things as we discover them, and removing any that don’t need to be done. We ask you to visit us every month. We’ll show you these cards, and show you how many are done and how many are left to do. If you’re not satisfied with the progress, cancel the project.”

Sue Unger, the highest-ranking IT executive I’ve ever met, said, “I can do that.” If she can, so can you.

Now the C3 project was a payroll program, and Marie was a payroll expert, so she knew exactly what had to be done. The team had been working on payroll software, so they had a good idea of the need and what it entailed. Even so, we added and removed things over the course of the project, deferring work that didn’t need to be done, and picking up new items along the way. This was one of the best-planned projects I’ve ever seen, and even so, at least one third of the requirements were added, removed, or substantially changed.

Nonetheless, the team, and Ms. Unger, were able to tell whether things were going well enough by looking at the stack of work that was done, and the stack remaining to do.

As students of Agile history know, however, the C3 project was not entirely successful. Despite shipping a number of versions on time, the project was ultimately cancelled. The reasons were largely political, but clearly if the project had been perfect, it wouldn’t have happened. It took us some time to realize that there was a big lesson hiding inside that history.

The C3 project’s purpose was to replace the entire family of Chrysler payroll programs. It didn’t accomplish that. Many years later, the subsequent project to replace the entire family of payroll programs has also not accomplished it. We now realize what should have been done.

We should have replaced the broken bits, one at a time, most valuable first.

The fundamental idea of making a complete list of everything payroll, and clicking through it, was wrong.

Parts of the old payroll programs were just fine, and didn’t need replacing. Other parts never belonged in payroll at all. Some of these, like tax, were recognized as external, and were done using external programs. But other parts were assumed to be part of payroll, and therefore the new payroll couldn’t be released until it included those parts.

This was not the right idea. There was a much better, simpler idea that we didn’t see. There were things Chrysler didn’t like about its existing payroll suite. This part was too slow. That part was done differently in different payrolls. Another part was hard to maintain. And so on. We supposed that the job was to build a grand new payroll program to rule them all. Wrong.

What we should have done, and could have done, was to solve the problems one after another, in the order that Marie and the other payroll people wanted them solved, and deployed those solutions as soon as they were ready. Some of those solutions would have been kept in a central program, and some would have been separate modules. For example, the overall flow of payroll is important, and it should be managed carefully. At some point we would have needed to organize this into what we called “the line.” It’s not clear that we needed to do that first.

Another area that needed work was Chrysler’s savings programs. There were many savings plans, they were complex, and they interacted. We should have written a program, or a series of programs, to deal with that. Those programs needed to interact with the line, but they didn’t need to be part of it.

And so on. We could readily have worked on the problems a few at a time, in the order Chrysler needed them solved. We could have deployed those solutions as soon as they worked. There would be issues with keeping them cooperating, keeping them maintainable, and so on, but we had those problems anyway, and smaller independent modules would have been the right way to address that. We could even have run separate modules on different computers, at different stages in the time-keeping, calculation, disbursement process, and would very likely have produced a more efficient, more modular program.

Had we done that, much of that work would still be running today and only the parts that really needed to be redone would have been redone.

The C3 Payroll, held up as one of the original successes—and original failures—of Agile, would very likely have been more successful had it not assumed that the job was to predict when it would all be done, or even track and project when it would be done. The job was to convene a team to solve the problems of the Payroll organization, and when the return on that investment declined, to move on. More would surely have been accomplished, and quite likely more of it would be still running today.

It’s not ideal to think of our product as a long list of things we must do. It’s not the best idea to predict when we’ll be done, or even project when we’ll be done. The Agile Manifesto calls for Working Software. Take the next problem, solve it with working software. Really solve it, which means getting that solution in the hands of the people who need it. It’s not about planning, predicting, and projecting. It’s about choosing, building, and providing.

Of course there are good ways to use estimation, and to do it. Here are a few:

How Big Is This Project?
It seems that “they” often want to know how long something is going to take, and how much it will cost. My view is that “they” don’t even know what they want, so we bloody well can’t possibly know how long it will take. However, “they” are often powerful and have the money we need, so we need to answer their question, even though we cannot.

Mind you, if you know a way to estimate correctly how long and how much, please just go ahead and do it. In your copious free time, please write it up for the rest of us. Please include true stories of what actually happened on the projects you have estimated that way, including the changes encountered and the lives destroyed. Meanwhile, we’ll just carry on here.

Most of the time, “they” know how many people they’ll give us, and how much time. They do that head-shaking thing until we “estimate” the numbers they have in mind. So we should turn the question around. “How much did you want to spend, and when did you hope to see the product?” Then they tell us, and we decide whether we can do something reasonable within that budget. If we can, we go ahead. If not, we politely decline the business. If we have decided we can’t, then we have an estimate in mind and we should just say what it is. Frankly, it is likely as good as anything we’ll come up with using a more complex method.

If no one knows, and no one has an idea, odds are the project is too vague and too big. Run away. However, if for some reason you enjoy leaping off cliffs hoping to generate a plan on the way down, here’s something to try. Chet Hendrickson and I call it the “Five Card Method.”

Consider the product idea and divide the vision up into about five major topics. Each topic should make business sense: don’t divide it up in some technical way. “Online Bookseller” breaks down into, oh, maybe “Have info on a huge number of books,” “Search, find, and recommend books,” “Shopping Cart and Billing,” “Back-end Picking and Shipping,” “Reporting and Accounting.” Who knows? Find your own five.

Can you estimate any of those five now? You may know a lot about shopping carts and have a good idea how long it will take. If so, estimate those items. For each item you couldn’t estimate, break it down into about five more smaller ideas. Maybe “Search, find, and recommend books” turns into, I don’t know, “Search by Title,” “Search by Author,” “Search by Similarity,” “Search by other customer purchases,” “Search by this customer’s purchases.”

Wow! We can almost write the SQL for title and author. Customer purchases sounds like a join and then a simple summary. Similarity still seems large. So we estimate the ones we understand, and repeat, splitting the ones we don’t.

Generally, within a couple of levels of breakdown, we come up with things we can estimate. Use whatever means of estimation you like.

Then add up the numbers, multiply by any integer between e and pi, and there’s your estimate. Or use your own magical incantations. It almost doesn’t matter.

It almost doesn’t matter because this is still an estimate. It’s a very weak estimate. It’s pretty much guaranteed to be wrong. But it might be large enough to let you get started, and start making fine-grained decisions on what to do next and what to defer. Do the Agile thing, producing a running system every couple of weeks. Maybe your first version only knows four books, has a trivial shopping cart, charges everything to your boss’s credit card, and sends an email to James in the shipping department to go to the local book store, buy the book, and stop at the post office on the way back to the office.

No, I’m serious. Why not have a full product that does very little at first, then more and more? Each time we look at that product, we see what to do next.

How Much Work Should We Accept This Time Around?
An Agile team needs to decide how much work to accept into its next iteration. One way to do this is to look at each proposed work item and estimate how much time it will take to do. Add up those times to get a quick check on the proposed iteration backlog.

It can be tricky just adding up times. No team gets eight hours a day of work on task, so you have to decide how to adjust. One way is to keep track of how you do against your estimates. It might be best to consider how much time you actually spent working on the thing—that is, did it really take you four hours of work to do it—and to consider how much time elapsed before your got your four hours in. Sometimes it can take days to get four hours’ work done.

You’re on a slippery slope here, so beware. It will be tempting for people to ask why it takes two days to get four hours’ work done, and to demand that people work harder, go faster, and so on. This is the edge of the cliff we’re concerned about. Keep concerns and analysis inside the team.

There are a number of ideas about how to estimate using something other than time. Points, Gummi Bears, Fibonacci numbers, T-shirt sizes. These were originally invented to obscure the time aspect, so that management wouldn’t be tempted to misuse the estimates. (I know: I was there when they were invented. I may actually have invented Points. If I did, I’m sorry now.)

There’s a good idea hidden inside these methods, which is to compare one feature idea to another and think about whether it is “larger” or “smaller,” and to classify the features into groups. With a couple of measurements of how long these similar items take, a team can learn to estimate quite quickly and effectively.

Remember, though. We are doing all this to decide how much work to take on in an iteration. We might want to improve our ability to do that, and we might benefit from thinking about why we thought that thing would be easy and it turned out to be hard. At the end of the day, however, teams who look at the work, discuss, look each other in the eyes and say “this much” do just as well as those who spend a lot of time in numerology. Often they do better, because teamwork and commitment are more powerful than number crunching.

So what’s my advice? It’s really pretty simple. It’s probably hard to do. You need to find your own way, but here are two decent ways to go. The second is far better than the first.

Good, But Not Ideal: Pick Your Delivery Date; Deliver Every Week from Now Until Then
The “big guys” have a date in mind. In the rare case where they don’t, pick one yourself. Pick it to be soon enough that no one can possibly get impatient waiting for your project to complete. Count your people, multiply by the time available. Guess about what you’ll have by then, with about five major items. If you must, break them down. Keep them vague: you need the room to steer. Voila! You now have a budget, complete with estimates.

Now get yourself a “customer” or “product owner” who can make decisions on what to do next and what to defer. Work in very short cycles. Two weeks. One week. One feature at a time, in two days. Short. Do features from most important to least. Every time a feature is done, or at least every two weeks, build an integrated, tested version of the software. Show it to everyone. If possible, get it to users who need it. If your software is slated to save lives, save some lives with it. Observe what happens. Factor that into what you do next.

You’re shipping a complete product now, every week or two. When the deadline arrives, it’s just another shipment. If everyone is satisfied, and likely they will be, stop. If they want more, you’re all set to do more, every two weeks.

Ideally, Skip Estimating; Just Build Something Now
Why not start every product with a simple experiment? Do we think it’s pretty simple? Take a real product visionary as a product owner, and have them sit with a few developers for a week or two to build something. Then ask yourself whether to go ahead. Is this a bigger project, possibly taking six months or a year? Then build in two-week iterations for a few cycles. See where you are. If it’s good, go ahead. If it’s not, stop.

Seriously. Put a person who understands the problem right in with the people who understand how to solve problems, and solve problems in the order that seems most important. Ship everything you do right away. See what the users say, see what the market says. Adjust.

Are there “issues” with this approach? Sure. You have to be very good to do this. You need to have someone who can take a good guess at what is needed, and a team that can build it rapidly, at high enough quality to give it to users really quickly. And you need to know how to build software that is soft enough, malleable enough, to grow smoothly as it needs to. The technical side of this is well understood. The decision side—the customer side—is not, but waiting won’t make it better. Get the product out there and see what happens.

This approach shortens all the cycles that delay getting value. It shortens the communication lines between the people who want things and the people who do things. It shortens the communication lines between the people who create things and the people who use them. Take the most important ideas, build them quickly, get them out there.

Yes, it’s hard to do. That’s why it’s best. Stop estimating. Start shipping.

Ron Jeffries has been developing software longer than most people have been alive. He holds advanced degrees in mathematics and computer science, both earned before negative integers had been invented. His teams have built operating systems, compilers, relational database systems, and a large range of applications. Ron’s software products have produced revenue of over half a billion dollars, and he wonders why he didn’t get any of it.

Send the author your feedback or discuss the article in the magazine forum.
