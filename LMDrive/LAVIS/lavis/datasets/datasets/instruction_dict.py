INSTRUCTION_DICT={0: ['Proceed ahead and make a left turn.', 'Just up ahead, take a left.', 'Left ahead.', 'Hang a left up front.', 'Prepare to turn left up ahead.', 'Your next action is a left turn, just ahead.', 'Up ahead, just take a left.', 'A left turn is required up ahead.'], 1: ['Proceed ahead and make a right turn.', 'Just up ahead, take a right.', 'Right ahead.', 'Hang a right up front.', 'Prepare to turn right up ahead.', 'Your next action is a right turn, just ahead.', 'Up ahead, just take a right.', 'A right turn is required up ahead.'], 2: ['After [x] meters, execute a left turn.', 'After [x] meters, take a left.', 'Left in [x] meters.', 'After [x] meters, hang a left.', 'In [x] meters, prepare to turn left.', 'Continue for [x] meters, then turn left.', 'Go [x] meters, then just take a left.', 'After [x] meters, a left turn is required.'], 3: ['After [x] meters, execute a right turn.', 'After [x] meters, take a right.', 'Right in [x] meters.', 'After [x] meters, hang a right.', 'In [x] meters, prepare to turn right.', 'Continue for [x] meters, then turn right.', 'Go [x] meters, then just take a right.', 'After [x] meters, a right turn is required.'], 4: ['Please execute a left turn at the forthcoming intersection.', "You're going to be turning left at the next junction, alright?", 'Next intersection, turn left.', 'Hang a left at the next crossroads.', 'It is obligatory to take a left turn at the forthcoming intersection.', 'When you reach the next intersection, you will need to steer your vehicle to the left.', 'Next intersection, just swing a left.', 'You must turn left at the next intersection.'], 5: ['Please execute a right turn at the upcoming intersection.', "At the next junction, you'll want to turn right, please.", 'Next intersection, turn right.', 'Hang a right at the next crossroads.', 'It is mandatory to take a right turn at the imminent intersection.', 'As you approach the next intersection, prepare to make a right turn.', 'Next intersection, just swing a right.', 'A right turn is necessary at the forthcoming intersection.'], 6: ['Please proceed straight at the next intersection.', 'Just keep on going straight at the next junction, okay?', 'Next intersection, go straight.', 'Straight through the next crossroads.', 'It is required to maintain your direction straight at the approaching intersection.', 'At the next intersection, continue to progress straight without altering your direction.', 'At the next intersection, just keep heading straight, no turn.', 'Maintain your course straight at the next intersection.'], 7: ['After traveling [x] meters, you are directed to make a left turn at the intersection.', "Just another [x] meters, then you'll be turning left at the junction, okay?", 'After [x] meters, left turn at intersection.', 'Go [x] meters then hook a left at the crossroads.', 'After navigating [x] meters, a left turn at the intersection is obligatory.', 'After travelling a distance of [x] meters, you will need to steer your vehicle to the left at the intersection.', 'After [x] meters, go left at the intersection, easy peasy.', 'Upon completing [x] meters, a left turn at the intersection is compulsory.'], 8: ['After advancing [x] meters, you are directed to make a right turn at the intersection.', 'After going another [x] meters, take a right at the junction, please.', 'After [x] meters, right turn at intersection.', 'Go [x] meters then hook a right at the crossroads.', 'Upon traversing [x] meters, a right turn at the intersection is mandatory.', 'After moving forward [x] meters, prepare to make a right turn at the intersection.', 'After [x] meters, go right at the intersection, no big deal.', 'After a distance of [x] meters, a right turn at the intersection is necessary.'], 9: ['After covering a distance of [x] meters, please continue straight at the intersection.', 'Keep going straight for [x] meters and then continue straight at the junction, alright?', 'After [x] meters, straight at intersection.', 'Go [x] meters then cruise straight at the crossroads.', 'After travelling [x] meters, maintaining your direction at the intersection is required.', 'After covering [x] meters, continue to progress straight at the intersection without altering your direction.', '[x] meters more, then straight on at the intersection, piece of cake.', 'After travelling [x] meters, it is critical to continue straight at the intersection.'], 10: ['Please execute a left turn at the subsequent traffic signal.', "You're going to turn left at the next light, alright?", 'Next light, left.', 'Take a left at the next light.', 'It is required to make a left turn at the next traffic signal.', 'When you reach the next traffic signal, you will need to turn left.', 'Next light, just swing a left.', 'You must turn left at the next traffic signal.'], 11: ['Please execute a right turn upon reaching the upcoming traffic signal.', "At the next light, you'll want to make a right, okay?", 'Next light, right.', 'Take a right at the next light.', 'It is imperative to make a right turn at the next traffic signal.', 'At the next traffic signal, you should make a right turn.', 'Next light, just swing a right.', 'A right turn at the next traffic signal is non-negotiable.'], 12: ['Please maintain your course straight at the next traffic signal.', 'Just keep on going straight at the next light, okay?', 'Next light, straight.', 'Keep straight at the next light.', 'Continue straight at the subsequent traffic signal.', 'At the subsequent traffic signal, you should continue straight.', 'At the next light, just keep heading straight.', 'Continue straight at the subsequent traffic signal, without deviation.'], 13: ['Upon traversing [x] meters, execute a left turn at the traffic signal.', "Just another [x] meters, then you'll be turning left at the light, okay?", '[x] meters, left at light.', 'After [x] meters, take a left at the light.', 'Upon covering [x] meters, make a left turn at the traffic signal.', 'Upon advancing [x] meters, you should turn left at the traffic signal.', 'After [x] meters, go left at the light.', 'Upon covering [x] meters, a left turn at the traffic signal is mandatory.'], 14: ['After covering a distance of [x] meters, execute a right turn at the traffic signal.', 'After going another [x] meters, take a right at the light, alright?', '[x] meters, right at light.', 'After [x] meters, take a right at the light.', 'After a distance of [x] meters, make a right turn at the traffic signal.', 'After moving forward [x] meters, make a right turn at the traffic signal.', 'After [x] meters, go right at the light.', 'After a distance of [x] meters, a right turn at the traffic signal is obligatory.'], 15: ['After traveling [x] meters, maintain your course straight at the traffic signal.', 'Keep going straight for [x] meters and then continue straight at the light, alright?', '[x] meters, straight at light.', 'After [x] meters, keep straight at the light.', 'After traversing [x] meters, continue straight at the traffic signal.', 'After traveling [x] meters, you should proceed straight at the traffic signal.', '[x] meters more, then straight on at the light.', "After traversing [x] meters, it's crucial to continue straight at the traffic signal."], 16: ['At the ensuing T-intersection, make a left turn.', "You'll be turning left at the next T-junction, alright?", 'Next T-junction, turn left.', 'Next T, hang a left.', 'A left turn is necessary at the ensuing T-intersection.', 'When you reach the following T-intersection, you will need to turn left.', 'At the next T, swing a left, piece of cake.', 'A left turn is obligatory at the ensuing T-intersection.'], 17: ['At the forthcoming T-intersection, execute a right turn.', "At the next T-junction, you'll want to turn right, okay?", 'Next T-junction, turn right.', 'Next T, hang a right.', 'At the upcoming T-intersection, a right turn is compulsory.', 'At the next T-intersection, you should turn right.', 'Next T, just swing a right, no problem.', 'A right turn is mandatory at the upcoming T-intersection.'], 18: ['At the upcoming T-intersection, proceed straight.', 'Just keep on going straight through the next T-junction, sound good?', 'Next T-junction, go straight.', 'Next T, keep straight.', "It's critical to keep straight at the forthcoming T-intersection.", 'At the ensuing T-intersection, you should continue straight.', 'Next T, just keep straight, smooth sailing.', 'Maintaining a straight course is imperative at the forthcoming T-intersection.'], 19: ['After traversing [x] meters, execute a right turn at the T-intersection.', "After [x] meters, you'll want to turn right at the T-junction, okay?", '[x] meters, left at T-junction.', 'In [x] meters, hang a left at the T.', 'Upon covering [x] meters, a left turn at the T-intersection is necessary.', "After covering a distance of [x] meters, you'll arrive at a T-intersection, at which point you need to turn left.", 'In [x] meters, swing a left at the T, easy peasy.', 'Upon reaching a distance of [x] meters, a left turn at the T-intersection is obligatory.'], 20: ['Upon covering [x] meters, make a left turn at the T-intersection.', "In another [x] meters, you'll be turning left at the T-junction, alright?", '[x] meters, right at T-junction.', 'After [x] meters, hang a right at the T.', "After a distance of [x] meters, it's compulsory to turn right at the T-intersection.", 'After traveling for [x] meters, you will come to a T-intersection where you should turn right.', 'After [x] meters, take a right at the T, no biggie.', 'After completing [x] meters, a right turn at the T-intersection is mandatory.'], 21: ['After advancing [x] meters, continue straight at the T-intersection.', 'After going [x] meters, just keep on going straight through the T-junction, sound good?', '[x] meters, straight at T-junction.', 'After [x] meters, go straight through the T.', "After traversing [x] meters, it's critical to go straight at the T-intersection.", 'Upon advancing [x] meters, maintain your direction and proceed straight at the T-intersection.', 'After [x] meters, straight through the T, no sweat.', 'After a distance of [x] meters, maintaining a straight course at the T-intersection is imperative.'], 22: ['Depart at the first exit on the roundabout.', 'Find your way out at the first exit on the roundabout, please.', 'First exit.', 'Head out on the first exit.', 'Proceed to the first exit on the roundabout.', 'Carefully navigate to the first exit as you approach the roundabout.', 'Just slide out at the first exit on the roundabout.', "It's imperative that you take the first exit on the roundabout."], 23: ['Depart at the second exit on the roundabout.', "You'll want to take the second exit on the roundabout.", 'Second exit.', 'Roll out on the second exit.', 'Proceed to the second exit on the roundabout.', "As you reach the roundabout, you'll need to take the second exit.", 'No sweat, just hit the second exit on the roundabout.', 'You are required to take the second exit on the roundabout.'], 24: ['Depart at the third exit on the roundabout.', 'Please take a turn at the third exit on our roundabout.', 'Third exit.', 'Shoot out on the third exit.', 'Proceed to the third exit on the roundabout.', 'Upon reaching the roundabout, make your way to the third exit.', 'Cool, now catch the third exit on the roundabout.', 'It is necessary for you to take the third exit on the roundabout.'], 25: ['After making a left turn at the current intersection, make a left turn at the next intersection.', "After you've made a left at this intersection, your next move is a left at the following intersection.", 'Left, then left again.', 'Take a left here, then another left at the next one.', 'After executing a left turn at the current intersection, execute a left turn at the succeeding intersection.', "After you've successfully made a left turn at the current intersection, your next step should be to make a left turn at the upcoming intersection.", "After you've turned left at this one, swing a left at the next one.", 'Upon executing a left turn at the current intersection, execute a left turn at the subsequent intersection.'], 26: ['After making a left turn at the current intersection, make a right turn at the next intersection.', "After you've made a left at this intersection, you'll be turning right at the next one.", 'Left, then right.', 'Take a left here, then a right at the next one.', 'After executing a left turn at the current intersection, execute a right turn at the succeeding intersection.', "After you've successfully made a left turn at the current intersection, your next step should be to make a right turn at the upcoming intersection.", "After you've turned left at this one, swing a right at the next one.", 'Upon executing a left turn at the current intersection, execute a right turn at the subsequent intersection.'], 27: ['After making a left turn at the current intersection, continue straight at the next intersection.', "After you've made a left at this intersection, just keep going straight at the next one.", 'Left, then straight.', 'Take a left here, then go straight at the next one.', 'After executing a left turn at the current intersection, persist straight at the succeeding intersection.', "After you've successfully made a left turn at the current intersection, your next step should be to continue in a straight direction at the upcoming intersection.", "After you've turned left at this one, just keep on trucking straight at the next one.", 'Upon executing a left turn at the current intersection, remain on a straight course at the subsequent intersection.'], 28: ['After making a right turn at the current intersection, make a left turn at the next intersection.', "Once you've made a right at this intersection, your next move is a left at the following intersection.", 'Right, then left.', 'Take a right here, then hang a left at the next one.', 'After executing a right turn at the current intersection, execute a left turn at the succeeding intersection.', "After you've successfully made a right turn at the current intersection, your next step should be to make a left turn at the upcoming intersection.", "Once you've turned right at this one, swing a left at the next one.", 'Upon executing a right turn at the current intersection, execute a left turn at the subsequent intersection.'], 29: ['After making a right turn at the current intersection, make a right turn at the next intersection.', "Once you've made a right at this intersection, you'll be turning right at the next one.", 'Right, then right again.', 'Take a right here, then another right at the next one.', 'After executing a right turn at the current intersection, execute a right turn at the succeeding intersection.', "After you've successfully made a right turn at the current intersection, your next step should be to make a right turn at the upcoming intersection.", "Once you've turned right at this one, swing a right at the next one.", 'Upon executing a right turn at the current intersection, execute a right turn at the subsequent intersection.'], 30: ['After making a right turn at the current intersection, continue straight at the next intersection.', "Once you've made a right at this intersection, just keep going straight at the next one.", 'Right, then straight.', 'Take a right here, then go straight at the next one.', 'After executing a right turn at the current intersection, persist straight at the succeeding intersection.', "After you've successfully made a right turn at the current intersection, your next step should be to continue in a straight direction at the upcoming intersection.", "Once you've turned right at this one, just keep on trucking straight at the next one.", 'Upon executing a right turn at the current intersection, remain on a straight course at the subsequent intersection.'], 31: ['After proceeding straight through the current intersection, make a left turn at the next intersection.', "Once you've gone straight through this intersection, your next move is a left turn at the following intersection.", 'Straight, then left.', 'Go straight through here, then hang a left at the next one.', 'After proceeding in a straight direction through the current intersection, execute a left turn at the succeeding intersection.', "After you've successfully proceeded straight through the current intersection, your next step should be to make a left turn at the upcoming intersection.", "Once you're through this intersection, swing a left at the next one.", 'Following a straight course through the current intersection, execute a left turn at the subsequent intersection.'], 32: ['After proceeding straight through the current intersection, make a right turn at the next intersection.', "Once you've gone straight through this intersection, you'll be turning right at the next one.", 'Straight, then right.', 'Go straight through here, then hang a right at the next one.', 'After proceeding in a straight direction through the current intersection, execute a right turn at the succeeding intersection.', "After you've successfully proceeded straight through the current intersection, your next step should be to make a right turn at the upcoming intersection.", "Once you're through this intersection, swing a right at the next one.", 'Following a straight course through the current intersection, execute a right turn at the subsequent intersection.'], 33: ['After proceeding straight through the current intersection, continue straight at the next intersection.', "Once you've gone straight through this intersection, just keep going straight at the next one.", 'Straight, then straight again.', 'Go straight through here, then straight again at the next one.', 'After proceeding in a straight direction through the current intersection, persist straight at the succeeding intersection.', "After you've successfully proceeded straight through the current intersection, your next step should be to continue in a straight direction at the upcoming intersection.", "Once you're through this intersection, just keep on trucking straight at the next one.", 'Following a straight course through the current intersection, remain on a straight course at the subsequent intersection.'], 34: ['Transition to the left lane for travel.', 'You might want to switch to the left lane.', 'Switch to left lane.', 'Get over to the left lane.', 'Change your route to the left-hand lane.', 'Please adjust your course to the left-most lane.', 'Just head for the left lane.', 'Reposition to the left lane.'], 35: ['Transition to the right lane for travel.', 'You might want to switch to the right lane.', 'Switch to right lane.', 'Get over to the right lane.', 'Change your route to the right-hand lane.', 'Please adjust your course to the right-most lane.', 'Just head for the right lane.', 'Reposition to the right lane.'], 36: ['After [x] meters, transition to the left lane for travel.', "In about [x] meters, you'll want to switch to the left lane.", 'In [x] meters, switch to left lane.', 'In about [x] meters, get over to the left lane.', 'In [x] meters, change your route to the left-hand lane.', 'After proceeding for [x] meters, adjust your course to the left-most lane.', 'In [x] meters, just head for the left lane.', 'In [x] meters, reposition to the left lane.'], 37: ['After [x] meters, transition to the right lane for travel.', "In about [x] meters, you'll want to switch to the right lane.", 'In [x] meters, switch to right lane.', 'In about [x] meters, get over to the right lane.', 'In [x] meters, change your route to the right-hand lane.', 'After proceeding for [x] meters, adjust your course to the right-most lane.', 'In [x] meters, just head for the right lane.', 'In [x] meters, reposition to the right lane.'], 38: ['Proceed along this route.', "Keep going on this road, you're doing great!", 'Continue on this road.', 'Keep cruising down this road.', 'Maintain your course along this route.', 'Continue driving straight on this particular road.', 'Just keep on rolling down this road.', 'Do not deviate from this route.'], 39: ['Proceed along the highway.', "Keep going on the highway, you're on the right track!", 'Continue on the highway.', 'Keep cruising down the highway.', 'Maintain your course along the highway.', 'Continue driving straight on the designated highway.', 'Just keep on rolling down the highway.', 'Do not deviate from the highway.'], 40: ['Proceed along this route for [x] meters.', "Keep going on this road for [x] meters, you're almost there!", 'Continue for [x] meters.', 'Cruise down this road for about [x] meters.', 'Maintain your course along this route for precisely [x] meters.', 'Continue driving straight on this particular road for exactly [x] meters.', 'Roll on down this road for about [x] meters.', 'Do not deviate from this route, continue for [x] meters.'], 41: ['Proceed along the highway for [x] meters.', "Keep going on the highway for [x] meters, you're doing awesome!", 'Continue for [x] meters on the highway.', 'Cruise down the highway for about [x] meters.', 'Maintain your course along the highway for precisely [x] meters.', 'Continue driving straight on the designated highway for exactly [x] meters.', 'Roll on down the highway for about [x] meters.', 'Do not deviate from the highway, continue for [x] meters.'], 42: ['Maintain your current course.', "Just keep going straight, you're doing great!", 'Keep straight.', 'Just keep on moving straight.', 'Preserve your current trajectory.', 'Continue in a straight line along your current path.', 'Just keep rolling straight.', 'Do not deviate from your current course.'], 43: ['Maintain your current course until the upcoming intersection.', "Keep going straight until you reach the next junction, you're on the right track!", 'Stay straight until the next intersection.', 'Keep on going straight till you hit the next intersection.', 'Preserve your current trajectory until the forthcoming intersection.', 'Continue in a straight line along your current path until you reach the upcoming intersection.', 'Keep on rolling straight till you get to the next junction.', 'Do not deviate from your current course until the next intersection.'], 44: ['Maintain your current course for [x] meters.', "Keep going straight for [x] meters, you're almost there!", 'Keep straight for [x] meters.', 'Go straight for about [x] meters.', 'Preserve your current trajectory for exactly [x] meters.', 'Continue to drive straight for exactly [x] meters.', 'Roll straight for about [x] meters.', 'Maintain your straight course for [x] meters.'], 45: ['Maintain your current course until the upcoming intersection for [x] meters.', "Keep going straight until you reach the next junction for [x] meters, you're on the right track!", 'Stay straight for [x] meters until the next intersection.', 'Keep on going straight for about [x] meters till you hit the next intersection.', 'Preserve your current trajectory for exactly [x] meters until the forthcoming intersection.', 'Continue in a straight line along your current path for exactly [x] meters until you reach the upcoming intersection.', 'Keep on rolling straight for about [x] meters till you get to the next junction.', 'Do not deviate from your current course for [x] meters until the next intersection.'], 46: ['Veering to the left, prepare to enter the highway.', 'Just move to the left and get ready to join the highway.', 'Left, ready to enter.', 'Slide left and plan to hop on the highway.', 'Execute a left maneuver, prepare for highway entry.', 'Position your vehicle to the left in preparation for your entry onto the highway.', 'Ease on to the left and get set to join the highway.', 'Proceed to the left, prepare for immediate highway entry.'], 47: ['Veering to the right, prepare to exit the highway.', 'Just move to the right and get ready to leave the highway.', 'Right, ready to exit.', 'Slide right and plan to hop off the highway.', 'Execute a right maneuver, prepare for highway exit.', 'Position your vehicle to the right in preparation for your exit from the highway.', 'Ease on to the right and get set to quit the highway.', 'Proceed to the right, prepare for immediate highway departure.'], 48: ['In [x] meters, veer to the left, prepare to exit the highway.', 'In [x] meters, move to the left and get ready to leave the highway.', 'In [x]m, left, ready to exit.', 'In [x] meters, slide left and plan to hop off the highway.', 'In [x] meters, execute a left maneuver, prepare for highway exit.', 'In [x] meters, position your vehicle to the left in preparation for your exit from the highway.', 'In about [x] meters, ease on to the left and get set to quit the highway.', 'In [x] meters, proceed to the left, prepare for immediate highway departure.'], 49: ['In [x] meters, veer to the right, prepare to exit the highway.', 'In [x] meters, move to the right and get ready to leave the highway.', 'In [x]m, right, ready to exit.', 'In [x] meters, slide right and plan to hop off the highway.', 'In [x] meters, execute a right maneuver, prepare for highway exit.', 'In [x] meters, position your vehicle to the right in preparation for your exit from the highway.', 'In about [x] meters, ease on to the right and get set to quit the highway.', 'In [x] meters, proceed to the right, prepare for immediate highway departure.'], 50: ['Be mindful of pedestrians ahead.', 'Please watch out for the pedestrians up ahead.', 'Pedestrians ahead.', 'Watch for walkers up front.', 'Please be alert of the pedestrians in the vicinity ahead.', 'Please be aware of the pedestrians moving in the area directly in front of you.', 'Just a heads up, there are some pedestrians ahead.', 'Attention is required for the pedestrians ahead.'], 51: ['Be mindful of the bicycle ahead.', 'Please watch out for the bicycle up ahead.', 'Bicycle ahead.', 'Watch for the bike up front.', 'Please be alert of the bicycle in the vicinity ahead.', 'Please be aware of the bicycle moving in the area directly in front of you.', "Just a heads up, there's a bike ahead.", 'Attention is required for the bicycle ahead.'], 52: ['Be mindful of the vehicle performing an abrupt stop ahead.', "Please watch out for the vehicle that's suddenly stopped up ahead.", 'Vehicle stopped suddenly ahead.', "Watch for the car that's just stopped up front.", 'Please be alert of the vehicle executing a sudden stop in the vicinity ahead.', 'Please be aware of the vehicle that has performed an immediate stop in the area directly in front of you.', "Just a heads up, a car's stopped suddenly ahead.", 'Attention is required for the vehicle stopping abruptly ahead.'], 53: ['Be mindful of the vehicle crossing on a red light to your left.', 'Please watch out for the car running the red light to your left.', 'Car ran red light on left.', "Watch for the car that's skipped the red on your left.", 'Please be alert of the vehicle infringing the red light on your left.', 'Please be aware of the vehicle that is crossing against the red light on your immediate left.', 'Just a heads up, a car is running a red to your left.', 'Attention is required for the vehicle crossing on a red light to your left.'], 54: ['Be mindful of the vehicle crossing on a red light ahead.', 'Please watch out for the car running the red light up ahead.', 'Car ran red light ahead.', "Watch for the car that's skipped the red up front.", 'Please be alert of the vehicle infringing the red light in the vicinity ahead.', 'Please be aware of the vehicle that is crossing against the red light in the area directly in front of you.', 'Just a heads up, a car is running a red ahead.', 'Attention is required for the vehicle crossing on a red light ahead.'], 55: ['Be mindful of the rough road surface ahead.', 'Please watch out for the bumpy road up ahead.', 'Bumpy road ahead.', 'Watch for the rough road up front.', 'Please be alert of the uneven road surface in the vicinity ahead.', 'Please be aware of the rough and uneven road surface in the area directly in front of you.', "Just a heads up, the road's a bit bumpy ahead.", 'Attention is required for the rugged road surface ahead.'], 56: ['Be mindful of the forthcoming tunnel.', 'Please watch out for the tunnel coming up.', 'Tunnel ahead.', 'Watch for the tunnel coming up.', 'Please be alert of the approaching tunnel.', 'Please be aware of the upcoming tunnel directly in front of you.', "Just a heads up, there's a tunnel coming up.", 'Attention is required for the impending tunnel.'], 57: ['Be mindful of the red light ahead.', 'Please watch out for the red light up ahead.', 'Red light ahead.', 'Watch for the red light up front.', 'Please be alert of the red traffic signal ahead.', 'Please be aware of the red traffic signal directly in front of you.', "Just a heads up, there's a red light ahead.", 'Attention is required for the red light ahead.'], 58: ['Be mindful of the green light ahead.', 'Please watch out for the green light up ahead.', 'Green light ahead.', 'Watch for the green light up front.', 'Please be alert of the green traffic signal ahead.', 'Please be aware of the green traffic signal directly in front of you.', "Just a heads up, there's a green light ahead.", 'Attention is required for the green light ahead.'], 59: ['Be mindful of the yellow light ahead.', 'Please watch out for the yellow light up ahead.', 'Yellow light ahead.', 'Watch for the yellow light up front.', 'Please be alert of the yellow traffic signal ahead.', 'Please be aware of the yellow traffic signal directly in front of you.', "Just a heads up, there's a yellow light ahead.", 'Attention is required for the yellow light ahead.'], 60: ['Please commence driving.', 'Feel free to start driving.', 'Start driving.', 'Go ahead and start driving.', 'It is advised to commence the drive.', 'Please initiate your driving operation.', 'Alright, you can start driving.', 'It is imperative to commence driving.'], 61: ['Please decelerate immediately.', 'Could you slow down right away, please?', 'Slow down now.', 'Easy on the gas, slow down.', 'It is advised to reduce your speed immediately.', 'Please implement an immediate reduction in your speed.', 'You might want to slow down a bit now.', 'It is imperative to decelerate immediately.'], 62: ['Please halt your vehicle immediately.', 'Could you stop your car right away, please?', 'Stop now.', 'Hit the brakes, stop now.', 'It is advised to bring your vehicle to a stop immediately.', 'Please execute an immediate stop of your vehicle.', 'Might be a good time to stop your car.', 'It is imperative to halt your vehicle immediately.'], 63: ['You are permitted to drive freely.', 'Feel free to drive as you wish.', 'Drive freely.', 'Drive as you like.', 'You may navigate freely.', 'Please proceed to drive at your own discretion.', 'Feel free to drive around.', 'You are authorized to drive freely.'], 64: ['Please proceed towards the navigation point; the following point is [x] meters ahead and [y] meters to your left/right.', 'Could you head towards the navigation point? Your next stop is [x] meters straight ahead and [y] meters to your left/right.', "Head to the point, next one's [x] meters ahead, [y] meters left/right.", "Get to the point, the next one's just [x] meters ahead and [y] meters to your left/right.", 'Please navigate towards the designated point, which is [x] meters in front of you and [y] meters to your left/right.', 'Please follow the direction towards the navigation point located [x] meters in front and [y] meters to your left/right.', "Head towards the point, the next one's about [x] meters up front, [y] meters to your left/right.", 'Navigate towards the designated point. The next point is located [x] meters ahead and [y] meters to your left/right.']}
