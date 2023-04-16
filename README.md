# Web-3.0-Recruitment-Task
## Overview
This is my attempt to make a Class Car in a python environment to stimulate its working. The car is assumed to have a 2D square shape and we assume that a collision occurs whenever the two squares touch or overlap with each other.As mentioned in the Recruitment Task the following Attributes have been implemented.  
## Attributes
***make*** :- Basic input of the name of the car.

***model***:- Basic input of the model of the car.

***year***:-Basic input of the manufacturing year of the car.

***speed***:-Basic input of the speed of the car.

***X***:- The X coordinate of the car.

***Y***:- The Y coordinate of the car.

***size***:- The length and width (since we assume the shape as a square we just define the side length as size) of the car.

## Methods
***Accelerate***:- Since we are implementing this in a 2D plane we divide the attributes into two sub-attributes giving us accelerate_x and accelerate_y where we simply increase the speed by the increment parameter.

***Brake***:- We just decrease the speed in the same way given above.

***detect_Collision*** :- As stated in the overview we assume the Car to be of a square shape and collision occurs when the two square touch or intersect.

***time_to_collision***:- We can detect the collisions by using the relative velocity concept. Though if no collision is occurring at the moment we may simply return -1 from the function defined in the class.
