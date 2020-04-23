# PyRacer:   
<img src="images/menuframes/frame1.png" alt="Game Title Screen" width="400" height="250"/>
<img src="images/screenshots/mainmenu.png" alt="Main Menu Screenshot" width="400" height="250"/>   
   
## Running The Game:   
In order to run PyRacer you will have to first install Pygame, as this is the library much of this code is based on.   
To install run the following code that best fits your situation in your terminal:   
Globally on your OS- `python3 -m pip install -U pygame`   
For a singular user- `python3 -m pip install -U pygame --user`   
   
Once PyGame is installed open the directory in which the game files are saved and run `python3 scripts/main.py` in the terminal of that directory.   
   
## Gameplay Overview:   
Here, we have a 2.5D car racing game, in which you have to drive your selected car through obstacles, and on the road in order to complete the track.   

The goal of this game is to beat all 6 stages to unlock the last car. Each stage of this racing game is a track, that a car that completes 3 rounds through a selected track chosen in the menu.   

For car choices, we have an option of the fastest car, but low durability, a medium speed car with medium durabiility, and a low speed car with high durability, and your objective is to complete the stage without your car getting destroyed.   

There are laserbeams coming overhead which enact damage to your car if it comes in contact. We have turbochargers as icons, which signify the number of stages you have completed. A golden turbocharger means you have completed one of the six stages.   

In order to reset number of turbochargers, simply press "R" in the menu.   
In the folder, if you navigate to data>gamedata.txt, you will see any collection of six numbers that are either 0's or 1's, which represent the completion values of each course completed. Changing them to 0, changes it to uncompleted.   

You also have differnet background music for each of the stages, as well as a HUD and stage completion idicator, giving you all the information you need to finish the stage.   

In summation, this game is a modern adaptation of the classic SEGA game 'Outrun', with a remix to the original gameplay where the you can choose between 3 different cars and race along 6 different courses. The primary objective of this game is to complete all six courses successfuly, and if this goal is achieved you will be rewared with the special 4th car. Below are the basic descriptions of each car.   

### The Sprinter:   
This car is the fastest but least durable.   
<img src="images/player/side1.png" alt="Sprinter Profile View" width="94" height="31"/>   

### The Sport-Utility:   
This car is somewhere in between in terms of speed and durability.   
<img src="images/player/side2.png" alt="Sport-Utility Profile View" width="96" height="36"/>   

### The Big Rig:   
This car is the slowest but most durable.   
<img src="images/player/side3.png" alt="Big Rig Profile View" width="100" height="50"/>   

### The ?????? ??????:   
???   
<img src="images/player/side4.png" alt="?????? ?????? Profile View" width="95" height="26"/>   


## Under The Hood:   
This game utilizes the PyGame library to acomplish several tasks; from rendering images and playing music to displaying the head-up display and handling user input. Used in accordance with object-oriented programming this game is brought to life.   
<img src="images/screenshots/gameplay.png" alt="Gameplay Screenshot" width="400" height="250"/>   

### Classes & Methods:   
There are five files and four classes that help create the game, with some handling the objects in the game and others handling the data the game uses.   

#### The 'Player' Class & File:  
desc   
+------------------------------------------------------------------------------------------------------------------+   
breakdown   

#### The 'Road' Class & File:  
desc   
+------------------------------------------------------------------------------------------------------------------+   
breakdown   

#### The 'Laserbeam' Class & File:  
desc   
+------------------------------------------------------------------------------------------------------------------+   
breakdown   

#### The 'TrackGenerator' Class & File:  
desc   
+------------------------------------------------------------------------------------------------------------------+   
breakdown   

##### In addition to these classes there is the fundamental 'main' function.   

#### The 'main' Function:   
This is the main function...   


## Usage Rights:
Look into this



