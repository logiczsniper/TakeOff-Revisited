# TakeOff Version 2
A remake of my first ever programming project: a game, 'TakeOff', in which
the user controls a small rocket as it flies into space, dodging obstacles
as it flies.

#### Updates
The following is a list of all of the upgrades made to the original 'TakeOff' in terms
of the game itself; the changes to the code is comparable to night vs. day.
1. The mouse is used to control the player. <br>
In the original game, the user interacts with the arrow keys to control the rocket. Now,
the rocket follows the movement of the mouse. This results in much more accurate control
over the movement of the rocket.
2. Collision detection is now pixel perfect. <br>
Previously, rectangles were drawn around each sprite and those were used in detecting whether
or not the player collided with, for example, an enemy. This produced very frustrating deaths
that appeared unfair as what you saw did not collide, but the rectangles did. Now, masks are
created over the non-transparent parts of each sprite and those are used for collisions.
3. Animation, animation, animation. <br>
In the first 'TakeOff', the only animation detectable was the change in size of the flame every time
you press an up or down arrow key and a change in rotation of the rocket when you hit a left
or right arrow key. This change is significant- in this new 'TakeOff', every sprite is well
animated to appear as a regular game should, as well as that the background is downward scrolling
which better portrays the effect that you are indeed flying upwards.
4. Simple controls. <br>
In this version of the game, you only need to use the mouse throughout the entire game. Depending
on which Scene the user is in, the buttons on the mouse play a different role, for example, on the
title scene a left-click starts the game and while playing, a click induces the pause scene.
This is very different from the last version, which has the user using escape key, arrow keys,
mouse movement and mouse click to play the game.


All of these upgrades... yet 168 less lines.