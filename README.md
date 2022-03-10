# cse210-05
Polymorphism: Teach One Another

Algorithm proposed by Nas

N.B Beware of the best use of the encapsulation
****************************************************************************************
Folder : Designs
#Pyray
Class Keyboard input
Class Video Service (that draws everything)
****************************************************************************************
Folder : Actors
Class Actor
#create the main characteristics of each actor using getter and setter method, create an interface
color, font-size, cell-size, position, text(the interface), velosity, move-next(this method allows the actor to move)(allow player to move from side to side of the screen)
Who are the Actors?: players, and the Banners for each player.
                  ********************************************
class Player(Actor):
#inheritance and polymorphism
#create their characteristics by overriding the method from the Actor class
#text and the design the player actor.
#a method to grow one trail (as they move)
                  ********************************************
class cast:
#regrouping each actor into their group.
#creating the group by using the getter and setter method
#initiate the list of the group
#A method to remove and add an element to the group
who are the groups? groups of the players and the banners
****************************************************************************************
Folder: Directing
class Director
#keep track of the sequence of the game
#start the game
                  ********************************************
- open the window
(while the window is open:)
--get_input
#receive mainly the keyboard input,
--do_update
#update the players position
#the player's tail doesn't grow until one of the player start give input,
#the trail grow automatically based on a condition (a timer(optional), or based on the frame of the video)
#set a maximum of trails and it stops growing
#compute when collision
--if the head of the player collide with an opponent trail:
--then
----this player lose, and the opponent win
----the Players'banner will be displayed accordingly, for example Player One: Lose, Player two: Win at the top of the screen,but if the head of the player hits the head of the oppenent, each player is a draw.
----the game over's bannner is displayed in the middle of the screen.
----the background will turn white (optional: we can have a black background, overlapped with a white half transparent background)
----Players keep moving and turning but don't run into each other, it means #disabling the keyboard input, #stop the continuity of the trail's growth, #automatic random move (loop) without colliding each other, prevent the random move of each players not to hit the opponent.
--show_output
#draw everything from the video service class
#loop closed
- close the window
****************************************************************************************
Folder : References
Point: coordinate the position, the position scale, the point collision.
Color (optional): will hold the color informations
****************************************************************************************
The _main_.py
#create all the characteristics of the actors
#start the game
