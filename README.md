# Jetpack Joyride Terminal Game

## Contents

* [Introduction](#Introduction)
* [How to run the program](#How-to-run-the-program)
* [Controls](#Controls)
* [Directory Structure](#Directory-Structure)
* [OOPS Concepts](#OOPS-Concepts)
    * [Inheritance](#Inheritance)
    * [Polymorphism](#Polymorphism)
    * [Abstraction](#Abstraction)
    * [Encapsulation](#Encapsulation)
* [Gameplay](#Gameplay)
    * [Movement](#Movement)
    * [Background and Scenery](#Background-and-Scenery)
    * [Enemies](#Enemies)
    * [Obstacles](#Obstacles)
    * [Score](#Score)
    * [Lives and Time](#Lives-and-Time)
    * [PowerUps](#PowerUps)
    * [Dragon](#Dragon)
* [Libraries](#Libraries)

## Introduction

>Jetpack Joyride Terminal Game is a basic terminal version of the game Jetpack Joyride. This game is tested only on __Linux__ based OSs.
>
>Din is a mandalorian living in the post-empire era. He is one of the last remaining members of his clan
>in the galaxy and is currently on a mission for the Guild. He needs to rescue The Child, who strikingly
>resembles Master Yoda, a legendary Jedi grandmaster. But there are lots of enemies and obstacles in
>his way, trying to prevent Din from saving Baby Yoda. Din is wearing classic mandalorian armour and
>has a jetpack as well as a blaster with unlimited bullets. You’ve got to help him fight his way through
>and rescue Baby Yoda.

## How to run the program

>* pip3 install -r requirements.txt
>* python3 run.py

## Controls

| Key | Action |
| ----- | ---------- |
| **d** | Move right |
| **a** | Move left |
|**w** | Activate jetpack and move up |
| **s** | Move down (if Dragon is activated) |
| **b** | Shoot bullets |
| **q** | Quit game |
| **\<spacebar>** | Activate shield (if available) |

## Directory Structure

```
.
├── ascii
│   ├── background
│   │   ├── clouds.txt
│   │   ├── mountain.txt
│   │   └── tree.txt
│   ├── characters
│   │   ├── boss_enemy
│   │   │   ├── boss_enemy1.txt
│   │   │   └── boss_enemy2.txt
│   │   ├── dragon.txt
│   │   ├── mandalorian.txt
│   │   └── slave_enemy.txt
│   ├── extras
│   │   ├── congrats.txt
│   │   ├── game_over.txt
│   │   └── time_up.txt
│   └── ostacles
│       ├── fire_beam
│       │   ├── fire_beam-1.txt
│       │   ├── fire_beam-2.txt
│       │   ├── fire_beam-3.txt
│       │   └── fire_beam-4.txt
│       └── magnet.txt
├── background.py
├── base.py
├── board.py
├── characters.py
├── coin.py
├── firing.py
├── functions.py
├── getch.py
├── obstacles.py
├── person.py
├── powerup.py
├── run.py
├── topbar.py
├── README.md
└── requirements.txt
```

## OOPS Concepts

* ### **Inheritance**

  >* The characters (*Mandalorian, Slave Enemy, Boss Enemy*) are inherited from main class *__Person__*
  >* The obstacles (*Fire Beam, Magnet*) are inherited from main class Obstacle
  >* *Bullets, Ice Balls* are inherited from main class *__Firing__*

* ### **Polymorphism**
  >* The method __*reappear*__ of class *__Boss_Enemy__* is overrided
  >* Many other functions are overrided

* ### **Abstraction**
  >* *__Background__* class abstracts the background of the screen which has *clouds, trees and mountains*
  >* *__Board__* class abstracts the board on which all other objects are placed
  >* *__Person__* class abstracts characters of the game
  >* *__Coin__* class abstracts the coins which are placed on board
  >* *__Firing__* class abstracts the *bullets* and *ice balls* shooted by *Mandalorian* and *Boss Enemy* respectively
  >* *__Obstacle__* class abstracts the obstacles (Fire Beam and Magnet)
  >* *__Topbar__* class abstracts the topbar which shows score, lives, time remaining etc,.

* ### **Encapsulation**
  >* *__Background__* class
  >* *__Board__* class
  >* *__Person__* class
  >* *__Coin__* class
  >* *__Firing__* class
  >* *__Obstacle__* class
  >* *__Topbar__* class

## Gameplay

### Movement

>* Press *__a__* to move left
>* Press *__d__* to move right
>
>* Press *__w__* to activate jetpack and move up
>* Press *__s__* to move down when **Dragon** is activated
>* Press *__b__* to fire bullets
>* Press *__spacebar__* to activate shield (if available)
>* When *__w__* key is released, gravitation acts on **Mandalorian**, but not on **Dragon**

### Background and Scenery

>* **Background** class is made to abstract the background with **clouds**, **mountains**, and **trees**
>* **Mandalorian** can't go out of *frame* or *above sky* or *below ground*
>* **Background** moves at constant rate. If **Speed booster** is taken, it moves at faster rate
>* Lots of **coins** are suspended in air. Collecting them will increase your **score**

### Enemies

>* **Slave enemies** come randomly who move only on ground. **One** life will be lost if your **Mandalorian** comes in contact with **Slave Enemies**. You can kill **Slave Enemies** by either *__shooting bullets at them__* or *__jumping on them__*.
>* **Boss Enemy** comes at last. He will throw *ice balls* at you. He adjusts his **position** along y-direction according your movement. **One** life will lost if your **Mandalorian** comes in contact with *ice ball* thrown by **Boss Enemy**. You can decrease the lives of **Boss Enemy** by __*shooting bullets at him*__.

### Obstacles

>* **Fire Beams** appear randomly on screen at different *heights*. **One** life will be lost if your **Mandalorian** comes in contact with **Fire Beam**. You can destroy the **Fire Beam** by *__shooting three bullets at them__*
>* **Magnet** appear randomly on top of the screen. You'll be attracted in both direction to **Magnet** if you come in the range of **Magnet**. You can destroy **Magnet** by *__shooting three bullets at it__*

### Score

>* You get **Five(5)** points for collecting **Coins**
>* You get **Fifty(50)** points for killing **Slave Enemy**
>* You get **Hundred(100)** points for shooting **Boss Enemy**
>* You get **Five Hundred(500)** points for killing **Boss Enemy**

### Lives and Time

>* **Lives** of **Mandalorian** is limited
>* **Time** is also limited. You need to complete the game by killing the **Boss Enemy** before the time exhausts.

### PowerUps

>* **Speed Boost** appears on screen randomly at different heights. Collecting them will increase the *game speed*
>* **Shield** gets activated after 60 seconds from start of game or after deactivating it. Collecting it will protect you from **Slave Enemies**, **Fire Beams**, **Boss Enemy** and his **Ice balls**

### Dragon

>* **Dragon** gets activated when you collect dragon powerup
>* It lasts as long as you don't collide with **enemy** or **obstacles**

## Libraries

>* **Colorama** library is used to add colors to objects of the game
