## TABLE OF CONTENTS

- [Description](#Description)
- [Usage](#Usage)
- [Nitty_gritty](#Nitty_gritty)
- [Intention](#Intention)
- [Future](#Future)
- [Help_me](#Help_me)
- [Notes](#Notes)
- [License](#License)

# Description
This project tries to find the optimal way around solo and hell events depending on your needs
This project is about the game Lords Mobile.

For F2P or low P2P players, speedups are a scarce resource and therefore I always had in mind ways to use the least possible amount of speedups for the maximum reward. In the beginning I trained 4k t4 at a time because I was trying to do the 60k solo events, but with the ACW event I started playing around with 3200 troops (48k points) and I wondered what was the best way to go about this. 
This is my humble try, I simulate the environment of the game where you have troops and pacts, events that may or may not involve those objects and rewards if you get to certain checkpoints.
For now (v1), only speedups (represented in seconds, without separating kinds of speedups) are taken into account.

# Usage
Download opti_event.py
Change the values in variables from lines 6 to 25 (default_troops to HOURS) to your values. 
The default values show what you will train and merge by default
Boosts are the speed boost you get in their respective gear (if you have 630.56% training boost, write 6.3056)
Your values for the items are basically the answer to the question "how many gems would I pay for this?". For example, ancient cores can be bought for 950 gems, but would I waste 5k gems for a pyris? Hell no. (For v1, only speedups are taken into account)
HOURS represents how many hours will get simulated
You can change/add print statements at the end to get more info

# Nitty_gritty
There are 4 relevant kind of events for this project: with pacts, with troops, with both, with none. Since there are 2 events at the same time, we have 4^2 combinations, which I called grids and are represented like this: 
- (None|P) would be a solo event with nothing relevant and a solo event with pacts
- (P+Tr|Tr) would be a solo event with both and hell event with troops
There are also 4^2 combinations of what you can do with objects (troops and pacts), 4 for each:
- Do nothing
- Speed up what you have already training/merging, represented by P or Tr
- Speed up what you have and make extra to get to the closest next step, represented by P+ or Tr+
- Speed up what you have and make extra to get to the next step of both solo and hell events, represented by P++ or Tr++

Nothing else makes sense if you assume that getting from any step to the next one without any troops/pacts already getting produced will never be worth it.
Some of these combinations never make sense, like P++Tr++, because if you have PTr, you can choose to get the next steps for both events with either troops or pacts. If you want a mix, be my guest, but you may as well just do some events with extra troops and some with extra pacts.
Some of these combinations don't make sense in some grids, for example if you're in (P|P), speeding up your troops won't yield any benefit, so you're left with only 4 options (None, P, P+ and P++)

Some of the grids are symmetrical (like (P|None) and (None|P)), and therefore can be treated as the same, that leaves us with 9 different grids (and None|None) depending on if there are pacts and troops in solo and hell events, represented in the code as pact_solo, pact_hell, troop_solo and troop_hell (ps, ph, ts and th inside the speedup function)

So basically it's a loop where it checks that it's not a (None|None) grid and uses the speedup function. The function then checks what grid it belongs to, and calculates all the options inside that grid. Some options don't make sense some times (like Tr++ if you already got solo step 3, because there's no step 4), so I set them to -1000000 to avoid errors in the calculation process. It adds everything relevant to TOTAL variables and finishes the function. 


# Intention
I tried 3 or 4 different ways to calculate every possibility, having to rewrite so many lines of code, so even if this code is redundant sometimes, I'm very happy about it. With previous tries, I was very lost in my own code, so this time my focus was readability (for myself), basically I wanted to know what I was writing and why I was doing it at any point in the code, that's why some values are redundant, why some elif statements could be changed to else but I decided against, etc.
This is the kind of code that you use once thoroughly but then you know your stuff and therefore won't use it again, so I didn't care much about speed. It can calculate a million hours in some seconds, that's more than okay for me. 

# Future
Future improvements I have in mind:

 - Wait to speed up/instead of speeding up:
After speeding up (and therefore starting a new batch), there's a chance that batch of troops/pacts won't find a suitable event and will just finish by themselves. If you wait to speed up, there's a chance that you will catch another event right when it's beginning, and therefore the chance of that batch finishing without rewards gets lower.
- Add energy, gems and other to the calculations to see if speeding up is worth it, and also to try alternative methods like trying to get the 320k training hell event.
- Finish events with lower tiers. For example, if there are 3k points left for a pact event, maybe finish it with pact 3 or less.
- Optimize waiting. Imagine you have 6h left of training and speeding up now gives you 15 min rewards, waiting might be more profitable on average.
- Take into account if you want to finish events with extra troops or pacts if both are possible (or block extra pacts if you want to use those speedups for watcher or something).
- Decide main strategy, getting as many speedups as possible to having the highest net income (or be able to choose between the two inside the code).
- ~Maybe merge ox_rewards, ox_speedups_used and ox variables in each option, to cut down lines of code.~
- Add random relocators and other less important rewards (not rss).

# Help_me
This is my first big project, in github and in python in general, so any kind of help is welcome, be it a way to make the speed_up() function 40 lines long instead of 1200, other implementations that might be interesting, suggestions about the structure of the code or even about the structure of this README or repository in general. You can reach me in telegram (link in my profile) or discord (mikiburgos).

# Notes
- I'm assuming every solo and hell event has an equal chance of appearing
- I'm not sure all events are registered inside the code, I added all the events I found in lordsmobile.fandom.com and also one I found myself in-game. Please send me screenshots of other events that aren't registered (or make a fork or something? I don't really know how github works, nor what the accepted practice in these cases is)
- Rss and other low-value rewards aren't included in rewards
- Watcher/CD medals aren't accounted for, and honestly I find very difficult to find a gem equivalent to it, so you should think about your strategy with that in mind.
- 24h challenges are not taken into account
- It assumes you will restart training and merging as soon as it finishes, as if you were a bot. You need to keep this in mind, it might change what the best option for you is.


# License
This work is licensed under CC BY-NC-SA 4.0
