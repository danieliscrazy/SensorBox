---
title: "Sensor Box"
author: "@dld"
description: "A Pi Pico W powered sensor box for my room!"
created_at: "2025-07-20"
---

> I have been working on this for 11 hours.

### July 20th, 2025

4:00 PM: So I've been thinking about what project I could make as my last project, but the issue is, I essentially have 2 days to make it (as well as finish my previous project once its PCB arrives). I additionally can't really go to Micro Center again soon, because my family's car broke down (insert Slack :heavysob: emoji here). So I was gonna make a list of the parts that I have and ask other people what I should make, but as I was making it, I remembered this giant kit of 48 different sensors that I got a while back. Most of them were fairly useless (cough cough traffic light led cough cough "magical light cup" cough cough). However, I noticed a specific module, the MQ3, and thought, "I could make a breathalyzer!" (it's an alcohol sensor) But then I realized that a breathalyzer would make no sense, so I looked to its cousin, the more useful MQ2. The MQ2 detects gas and smoke. I could make a smoke alarm! This'd be great for me, as I recently realized that sleeping with my door closed and with no smoke alarm in my room is not a good idea. But a smoke alarm would be too simple, even with a cool case I wouldn't call that a 6 point project. So I looked to my other sensors. I've also got a DHT11 temperature and humidity detector, so I could make it detect that too. But it still felt too basic. So I'm gonna also add a 16x2 LCD, a button, a piezo buzzer, and potentially more. I'm gonna try to use CircuitPython for this, but I'm not very experienced in CircuitPython, so it may be a bit more difficult for me.

5:00 PM: Trying to just try out the MQ2, and already ran into an issue. I have very few female wires, all of my sensors have pin headers out (90 degree ones that won't fit on a breadboard), and the ones that I am using are currently being used by my other project. It's gonna get a PCB soon (as soon as it arrives at my house), but as of right now it doesn't have one. Debating whether or not to take them out for this project. Looking more like I'll have to.

5:15 PM: I can't look at the time "5:15 PM" without thinking of the second LEGO Movie. So I did end up ripping the wires out, but then I realized something. The MQ2 is 5V, and it's analog. The Pi Pico's GPIO is 3.3V. In order to run it properly, I'd need to use resistors, but I don't have convenient resistor sizes. Hm. 

### July 21st, 2025

10:15 AM: I gave up last night. But I've been working for a bit and it seems that a sufficient divider is 100K and 200K (2 100K resistors because that's all I have). So next step is to try out the MQ2. Heard it takes a bit to warm up so I'll give it that. It also smells a bit when I turn it on, but apparently that's because it's powered by a heating element and I haven't used it before. _Technically_ you're supposed to give it about 3 days to warm up completely, but I don't have that kind of time unfortunately. Will give it a little bit though.

12:00 PM: So I've gotten it working... on an Arduino Mega 2560. My voltage divider doesn't seem to be working right. I feel like maybe I could risk it with just hooking the MQ2 directly up to the Pi Pico, because I don't think it's gonna get all the way to 5V, but I don't think I should. There's one, extremely janky option I can think of, which would be using a Raspberry Pi Zero instead of a Pico, and using an OTG cable do serial communication. Actually, wait, I just checked Amazon, there's a level shifter that should arrive by tomorrow! I'll order that and get it tomorrow, and for now I'll work on other stuff.

12:30 PM: So I got the DHT11 sensor working on the Pico, but now I'm encountering an issue where something on my PC is causing the Pico to reboot every second. Means I'm gonna have to use my crappy MacBook. Sigh. It's working somewhat. I've got basic code that sends the data to Adafruit IO every 15 seconds. Stopping work until probably around 4 PM.

<img width="508" height="307" alt="image" src="https://github.com/user-attachments/assets/b134c006-8ad5-4d4f-bc99-a6a12eb1fc4f" />

> The graph over time of the temp (celsius) and humidity. As you can see, there hasn't been much time nor change.

4:30 PM: Took a bit of a break. Temperature now reports in Fairenheit! Trying to now work on the LCD. Only issue with that is, _I can't find my goddamn breadboards!_ I can't interface with it yet! I'm counting time for looking for my breadboards, don't dock points for that please. Wait. Nevermind. Literally 60 seconds after typing the last thing I found 2 breadboards. They were with my soldering stuff and I just forgot. 

5:00 PM: Found a length of solid core wire from Undercity when unpacking, feel really bad but then again... this is genuinely some of the cleanest wiring I've ever done, which is good because this needs to be relatively flat. Genuinely want to get more, hope that this is enough for the whole project. It is a bit tedious though, so I'm gonna take a bit of a break.

5:30 PM: I lied. No rest for the weary. 

### July 31st, 2025

10:00 AM: Talk about cutting it close! Currently in a car, so not able to do the most in depth work. I'm fairly sure I got the LCD working, but I don't think I have the LCD... working. Some pixels only show up when the display is darker, some only show up when it's lighter. Worried it's the module being damaged. Actually, that's what it is, grabbed a different one and it worked. Gonna work on getting the humidity and temp to display on the LCD now. I also should note I have the level shifter now, so after I get humidity and temp working with the LCD, I'll try to test the MQ2, although I might not get the most accurate results, being in a car.

11:00 AM: Got it displaying temp and humidity on the LCD! Currently trying to figure out what resistance needs to be for the backlight, because my potentiometer is crap. Sorry I can't get pictures or code right now.

4:30 PM: I really need to lock in. Got LCD and temp + humidity working with Adafruit IO. Now working on MQ2. 

5:30 PM: Having... issues. Not getting consistent readings from the MQ2. I think it's issues with the level shifter, it works fine on an Arduino Mega. Need to leave for about an hour.

8:00 PM: MQ2 isn't working. I'm not doing the greatest, and I don't have much time before the deadline. I'm scrapping the MQ2 unfortunately, and I'm gonna redo some of the wiring to make it go flat, and work on 3D modeling. Also, if you're paying close attention to commits you may notice a 2 hour discrepancy. I forgot to log time for 4:30 to 5:30, and I did do work from 11:00 to 12:00, I just didn't make a journal entry (most of that was wiring).

9:30 PM: I'm tired and distracted. I modeled and placed all the parts. Now case making time!

<img width="955" height="669" alt="image" src="https://github.com/user-attachments/assets/2100aa25-11d8-4300-b085-d24f68aa1e99" />

> The parts!

10:00 PM: Figured I should show a picture at this point. Here's the picture! What I think I'll end up doing to accomodate the wires is get a crimping kit from Amazon or something (my own money), and get custom length DuPont wires.

<img width="1231" height="753" alt="image" src="https://github.com/user-attachments/assets/e2d21050-4561-4078-8605-a4b93366283a" />

> The setup!

### August 1st, 2025

9:45 AM: I know what you're thinking. "Daniel, why the hell are you still working on this? It's August 1st!" Well, I couldn't stay awake last night. Because I knew that I couldn't work any more, and knowing that review wouldn't happen for an absolute minimum of a day, I submitted my project without CAD, so I'm gonna do it right now. I'm gonna work until 11 (Daydream kickoff call), and if I still have work to do, I'll keep working at 12.

10:15 AM: Made the bottom part of the case, which is relatively simple. Currently trying to figure out where I want the DHT11 to go. I have a case thing I made before that should fit it, just need to figure out where to put it.

<img width="919" height="602" alt="image" src="https://github.com/user-attachments/assets/82deb500-09cd-43b0-91b3-f9f7c385d6eb" />

> Bottom case!

10:45 AM: Made a really basic top case part, with a screen cut out. Need to add holes for wires, and need to add the DHT11. I really want to find a way to polish this design more, because with the MQ2 having to be scrapped, and with it the buzzer scrapped as well, this project doesn't feel that deserving of 6 points. I'll continue to brainstorm, but I have to go to the Daydream kickoff call now.

<img width="1131" height="677" alt="image" src="https://github.com/user-attachments/assets/f73b5462-b681-4e9d-b2b0-8431ec7507a0" />
