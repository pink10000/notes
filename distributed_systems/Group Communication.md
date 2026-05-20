---
tags:
  - CSE_223B
---
# Group Communication
TODO


# ISIS 
- ISIS is a group communication system developed at Cornell University in the 1980s. It provides a reliable and ordered message delivery service for distributed applications.
- ran on nasdaq, boeing 777 software control system
- wanted to build replicated state machine, neededed single total ordering on all events and build RSM that did not diverge
- found out it is really expensive and not does not scale well
- only small parts need to be replicated state machines
- most of the system can get by by with weaker semantics
- RSM needs a total order, a distributed systems gold standard of strict consistency
- we need weaker semantics to get more performance. why and how?
  - need less serialization of information 
  - not scalabale
  - everything is limited by the speed of light 
- strong semantics are to prevent diverging state machines 
  - a node might have an event that needs to be ordered, so everyone needs to know about it and decide on it 
- relaxed ordering semantics = no need to wait to hear back from everybody, (speed of light bounds speed of communication)
- want relaxed consistency
- what could we do to solve this?

idea of isis:
- very complicated
- let us put semantics in the network/messaging layer, so that we can guarantee that when we send/recv a msg, we can guaratee certain properties about the message delivery
- lets us reason more simply in the application layer.
- can think of a semantics graph.
- y-axis: ordering, x-axis: reliability
  - UDP at the bottom left ("it might go through, best effort delivery, no ordering guarantees at all, unreliable")
  - TCP at the top right (reliable, ordered delivery)
    - strict FIFO ordering, sequential consistency
    - not totally reliable (some stuff may not get there), but the frames that do get there are in order.
    - if the sender and receiver do not fail, eventually there will be a FIFO ordering of everything that is set
    - if the sender OR the receiver fails, the sender can only know that the message was received ONLY IF it receives an ACK from the receiver. but the receiver cannot know that the sender received the ACK, otherwise we'd need to ACK the ACK, and so on. so we can only guarantee that the message was sent, but not that it was received. 
    - TCP is kind of in the middle of the graph, because it is not 100% reliable, but it is ordered.
- we can never guarantee that something gets there (cannot guarantee perfect reliability)
- however, from 2phase commit, we can guarantee "atomicity" 
  - atomic is to the right of reliable on the x-axis
- when a system is atomic, every alive node can agree if something happened or not, even if some nodes fail.
  - dead men tell no tales; if a node is dead, it cannot tell us anything about what happened, so we can only rely on the alive nodes to tell us what happened.
- we want "broadcast protocols", i.e. we send a message to the group, so that some subset of the group receives the message
- atomicity is expensive, but is very useful for RSM
- other orderings:
  - total wall clock ordering: all messages are ordered by their wall clock time sending time 
  - sequential consistency: all messages are ordered in the same order at all nodes, but the order is not necessarily the same as the wall clock time ordering. it is a "total order", but a type of total order
  - causal total ordering: respects "happens before" relation; like vector timestamp ordering. we do not need to care about messages that are unrelated to each other, so we do not need some kind of total ordering that forces us to order all messages, even if they are unrelated. we only need to order messages that are related to each other.
    - could be related is defined as could be causally related, i.e. if there is a path of messages that could have caused one message to be sent,
  - total order: everybody sends messages in the same order. 
    - ABCAST: atomic broadcast, a protocol that guarantees atomicity and total ordering.
  - causal ordering: for any particular user/node, the messages that they send are ordered in the same order that were sent. everything is coherent. all the messages that the node sees, then they are in the causal ordering for it.
    - CBCAST: causal broadcast, a protocol that guarantees causal ordering.
    - we can get casual total ordering by using CBCAST and ABCAST together. we can use CBCAST to get causal ordering, and then use ABCAST to get total ordering on top of that.


- In terms of reliability, ISIS focused on atomicity, which is the strongest form of reliability. 
- it is overkill for almost all applications
- both abcast and cbcast are extremely expensive, and do not scale well.


how to build these protocols?

CBCAST

- messages that come from a particular node should be delivered in the order of that node sent.
- we need to create a "buffer" of messages we are going to send to the system. 
  - FIFO buffer, everytime we want to send a message, we drop at the end of the queue
```
--+--+--+--+--+--+--+--+
  |  |  |  |  |A3|A2|A1|
--+--+--+--+--+--+--+--+
```
- this is if node A wanted to send message A3, A2, A1. 
- everytime we want to talk to a node
  - start tcp conn
  - send entire queue or start from the beginning until it stop listening (recv dies or refuses)
  - if the tcp conn dies, we restart from the beginning. 
- trivially meets first rule of casual consistency:
  - any messages received the from the node (the sender!) will be received in the order that the we sent them.
- now we need the meet the second
  - any messages that we send after the receipt of a received message, should be delivered after that message
  - any time we receive a message from anybody else, we must put it in the queue.
```
--+--+--+--+--+--+--+--+
  |  |B1|A4|C1|A3|A2|A1|
--+--+--+--+--+--+--+--+
```
- now this stores every message we have also ever heard. 
- so as other nodes talk to us, they start sending their queue of messages from the beginning. 
- we drop them at the back of the queue. if we have already heard or recived that message, we remove them because we've already seen them before. 
- how do we summarize all the messages we've recived up to some point in the queue? 
  - a vector timestamp. we can label the end of the queue with a vector timestamp that simply descirbes the highest number message of that queue. 
- so if C starts talking to us, then it is very easy to see if it is a new message or not (check the vts!)
- this ensures that if C sends us 7, we check the vector timestamp for what number it is. if we contain 7, then we have it. if the vts is > 7, then we have already seen it.
- what if the vts is lower? how much lower? the vts number must be 6 or higher. if they send 7, then they must have sent 6 already.
- we will then update our vts (we get messages from casual order).
- suppose B sends us (A) messages. suppose we receive messages from D, but we've never talked to D before.
  - what if we heard D5 from B? is this possible? for B to have D5, they must have had D1-4, so they must have talked to D from vts 1.
  - but what if B actually got D5 it from F? so how did F get D5? at some point someone must have talked to D, and we start from D1. 
- obviusly not a total ordering, does it violate causal ordering?
  - does it violate the order D sent the messages? no, someone must have heard D1-4. 
  - could i have already received a message from somebody from D before someone sent their message? no, because when they heard their message frm D, they would have dropped it. and when they talk to us, they would have already sent D1-4 already!
- this gives us a casual order, and an atomic ordering *eventaully*. 
  - why eventually?
  - because we talked to someone who talked to someone ...
  - and we will get all the messages
  - of course, more messages will be generated, but for any subset of messages, they will eventually be casually ordered
- if one messages makes it out of a node before it dies, then 
  - that receiver dies
  - that message is sent before it dies
  - by inudction, we will make it to some last node. and so it will have talked to everyone and be received
- every message either dies with a subset with a nodes that all dead, or escapes this subset and gets delivered. thus it is fully atomic.

to ensure a message reaches everyone, it needs to remember who it has not reached. the node will go to each "remaining destination", `REM_DST`
- eventually the messages in the beginning of the queue will have an empty `REM_DST` set
- ensures performance
- this is a global lower bound 
- hard because there are some nodes that are way behind and are dead... (technical, and hard, but can ignore for now)
- expensive and inefficient
- garbage collection makes it easier (see above). do not send msgs to nodes in the middle of it
- now when we get E1 for the first time, the node that sent by E1 will say "nodes B L Q T already got this message, so no need to send it there)
- kind of like treadmarks
  - the diffs are a form of causality. LRC is a form of causality.
  - we enforce this with lock acquisition, because we get all the updates of the people who previously had/acquired this lock
  - not a total order

ABCAST
- want: atomic, for everybody who gets it they should see it in the same total order but it doesnt have to be causal, because it is a total ordering, we should talk to every node.
- since everybody has the same total ordering, if we both send a message now and we find there is a disagreement, we have a problem. 
- when we want to send a message, we cannot consider it sent until the protocol (all the nodes) has commited. we also cannot renege on messages. 
- therefore we cannot do anything with our message until the message comes back (otherwise we cannot guarantee that other nodes received our message)
  - it can be kind of weird because the client that initiated this message would not see it is done until the total ordering is satisfied.
- just in like CBCAST, every node has a queue.
- whenever we want to send a message, we drop it in our queue.
- unlike CBCAST, we cannot carry on. that message has not been processed by everyone yet. 
  - this message has a flag that says "has this message been decided by the other nodes?", called `deliverable?`
```
--+--+--+--+--+--+--+--+
  |  |  |  |  |  |A2|A1|
--+--+--+--+--+--+--+--+
```
- if we cannot process it, then the queue is clogged. we cannot use the fact that A2 is processed until A1 is processed (total ordering!)
- there are multiple nodes in the system.
- we want to try and get the `deliverable` flag to be set to true so we can continue in the system. so for A, its job is to send this message. the nodes will put (push) this A into their queue. suppose we has this setup:
```
  "end" of queue
     v
A:    b(2a) a(1a)|
B:    a(2b) b(1b)| <- front of queue
C:    b(2c) a(1c)|
```
- we need `ack`s from everyone. they are going to send an `ack` where their thing showed up in their queue. in particualr, A and B ask:
"based on the messages currently clogging up your specific queue, what place in line should my message take?"

- for A, it will receive these two messages from B,C
  - C: `ack`, a is first
  - B: `ack`, a is second
- for B:
  - A: `ack`, b is second
  - C: `ack`, b is first
- for C: no `ack`s

- this message has showed up in everybody's queue. a safe place where it has showed up is "the highest"
- it is always safe to take a message and move it back because eveyone's queue is at least clogged up on the first message.
- when we get all the acks, we take the maximum number. 
```
A: max(1, 2, 1) = 2
B: max(2, 1, 2) = 2
```
- A has decided that A's msg needs to be in 2B since B's msg is the max. it will move it behind B in its queue.
- the highest number wins. in our case, since 2A < 2B, we sort `a` to be in front of `b` in all the queues. we can then consume `a`.
- after we move, this is what our queue looks like:
```
A:   a(2b) b(2a)|  <- from B, we got 2, so move back,    a is now deliverable
B:   a(2b) b(1b)|  <- from A, we got 2, no change,       a is now deliverable
C:   b(2c) a(2b)|  <- form A, we got 2, needs to update, a is now deliverable
```
- A adds deliverable to `a(2b)` but cannot be delivered because it is not at the front of the queue
- B changes `a(2b)` delierverable because they agree on the position

- the senders are not the first to know this, but actually C is
  - this is because A,B did not know that B has lost the race. the fronts are also not deliverable.
  - only C can consume msg `a`.

- let C consume `a`. now we need to decide on the status of the next front
```
A:   a(2b) b(2a)|
B:   a(2b) b(1b)|
C:         b(2c)|
```
- in the fullness of time, i.e. we will being processing b in the future at node B. it will consider the acks, where A provides 2a, and C provides 2c. 
- since 2c > 2a, node B will send b(2c) to everybody, and reorder its queue.
```
A:   a(2b) b(2a)|
B:   b(2c) a(2b)| <- reoreder queue, b is now deliverable
C:         b(2c)|
```
then A will receive it and reoreder its queue
```
A:   b(2c) a(2b)| <- reoreder queue, b is now deliverable
B:   b(2c) a(2b)| 
C:         b(2c)|
```
now, since a is deliverable, both nodes A,B will consume `a` and then all three will consume `b`.

- we ensure total ordering by sending to all nodes and ensuring that all nodes have the same order of messages in their queue.