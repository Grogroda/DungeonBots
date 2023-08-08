# DungeonBots

DungeonBots is a repository containing many discord bots to help players and dungeon masters manage their D&D 5e campaigns and (mainly) Discord Guilds. You can use a set of these bots in many ways you want, but in most cases you'll probably need many more tools to run your campaign, these bots are thought to help you do simple quick things during a session or help manage a Discord ingame guild in between sessions, but again you can use it as you like it. 

I currently do not intend to make these bots public since I don't want to pay for a server to run it, I'm just doing this as a creative project to learn a few things and practice my programming skills, but if I think this project is worth spreading to the world I'll find a way to do so.

As always, I recommend Linux users install and use the "tree" software to visually see the directory structure on this repo before working on it, I always try to keep my repos very organized and that takes some time to plan, so if you're going to work on this repo I ask that you maintain everything very well organized and pay attention to all details and gotchas, such as the (very important) .gitignore file. 

With all that out of the way, let's take a look at some of the details of this repo.

## Software Requirements

I'm writing all of these bots on Ubuntu 22.04 (currently) in Python 3.9.12. As of the last commit made, I'm using the following packages, modules and libraries:

- discord.py (installation: `pip3 install -U discord.py`);
- pandas (installation: `pip3 install -U pandas`);
- dotenv (installation: `pip3 install -U python-dotenv`).

## Bots

Many of the main directories of this repo are the bots themselves, in these directories I'll leave the main codes used to run the bots, assets specific to that bot (modules for instance) and everything specific to that bot. Here is a brief overview of what each bot is supposed to do:

- ShopGen: This bot is supposed to (semi-)randomly create and manage shop inventories for the DM according to their needs. Basically, no shop has everything, so instead of a player getting into a random shop in the middle of nowhere and having access to the entire arsenal of items in the Player's Handbook or the DM having to roll to see if a certain item is in that shop's inventory, the DM should be able to call this bot and give a category of shop (blacksmith, small shop, caravan, etc) and the bot should randomly generate the inventory of this shop and manage it during the game session; 
