# Game Doc

## Game Play
The player wakes up in a room, without any memory of where they are
or how they go there. Players can observe the room to see what items
are in it, they can interact with items, including adding them to their
inventory.

Small objects can be added to the players inventory or stored in other objects,
such as closets or kitchen drawers. Larger objects can be moved.

Different adversaries will appear at different times, often without warning.
Players can fight them off, using weapons, or flee, or hide until they go away.

Game play is turn based. Players have an option of waiting to see what happens
next.

The key: the game is different every time.

## Implementation

### Implementation of Alpha version.

Alpha version will be very simple. A player wakes up in a room with a limited
number of doors. Only one is an exit. Others are closets or are locked.

Alpha focuses on interation with objects, and leaves out any adversaries.
The player will be able to survey his enviroment to see what is around.

The room and its objects are randomly generated.

### Implementation of Beta version.

The beta version will introduce a monster, who can appear at arbitrary moments
in the game loop. The beta version will also introduce player attributes, such
as health and strength.

### Implementation of V1

V1 will create an entire building. Each room will be randomly generated. The
player's goal will be to escape.

## Types of Objects

There will be a number of different types of objects. For example, wrenches,
books, lantern oil, matches, cabinets. Some objects will be able to contain
other objects: for example, the Cabinet will be able to contain small objects.

Objects can not only be used by players, they can be used in concert with each
other. E.g., matches can light flammable things on fire.

## Types of Monsters

There will be a number of types of monsters, which may have particular
vulnerabilities. For example, vampires are vulnerable to garlic and sunlight.

## Player model
The player will have various attributes, such as health and strength. Some of
these attributes will be randomly set at the creation of the game.

## Game Loop
Each action should (eventually) have a lapse of time associated with it. The
game loop will run at every action. So, for instance, if they player decides
to look under the bed. In later versions, the player can be 

## Pulling in Open Data
Aside from the random generation of the rooms, it would be nice to pull in
open data. For instance, the player could come across books on a bookshelf and
be able to read them, while the content is pulled from gutenberg books.
