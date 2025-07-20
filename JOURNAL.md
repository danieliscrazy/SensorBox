---
title: "Sensor Box"
author: "@dld"
description: "A Pi Pico W powered sensor box for my room!"
created_at: "2025-07-20"
---

> I have been working on this for 1 hour.

### July 20th, 2025

4:00 PM: So I've been thinking about what project I could make as my last project, but the issue is, I essentially have 2 days to make it (as well as finish my previous project once its PCB arrives). I additionally can't really go to Micro Center again soon, because my family's car broke down (insert Slack :heavysob: emoji here). So I was gonna make a list of the parts that I have and ask other people what I should make, but as I was making it, I remembered this giant kit of 48 different sensors that I got a while back. Most of them were fairly useless (cough cough traffic light led cough cough "magical light cup" cough cough). However, I noticed a specific module, the MQ3, and thought, "I could make a breathalyzer!" (it's an alcohol sensor) But then I realized that a breathalyzer would make no sense, so I looked to its cousin, the more useful MQ2. The MQ2 detects gas and smoke. I could make a smoke alarm! This'd be great for me, as I recently realized that sleeping with my door closed and with no smoke alarm in my room is not a good idea. But a smoke alarm would be too simple, even with a cool case I wouldn't call that a 6 point project. So I looked to my other sensors. I've also got a DHT11 temperature and humidity detector, so I could make it detect that too. But it still felt too basic. So I'm gonna also add a 16x2 LCD, a button, a piezo buzzer, and potentially more. I'm gonna try to use CircuitPython for this, but I'm not very experienced in CircuitPython, so it may be a bit more difficult for me.

5:00 PM: Trying to just try out the MQ2, and already ran into an issue. I have very few female wires, all of my sensors have pin headers out (90 degree ones that won't fit on a breadboard), and the ones that I am using are currently being used by my other project. It's gonna get a PCB soon (as soon as it arrives at my house), but as of right now it doesn't have one. Debating whether or not to take them out for this project. Looking more like I'll have to.

5:15 PM: I can't look at the time "5:15 PM" without thinking of the second LEGO Movie. So I did end up ripping the wires out, but then I realized something. The MQ2 is 5V, and it's analog. The Pi Pico's GPIO is 3.3V. In order to run it properly, I'd need to use resistors, but I don't have convenient resistor sizes. Hm. 
