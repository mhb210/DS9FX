import App
import Foundation

abbrev = "DS9FXGalaxy"
iconName = "DS9FXGalaxy"
longName = "Galaxy"
shipFile = "DS9FXGalaxy"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"

Foundation.ShipDef.DS9FXGalaxy = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DS9FXGalaxy.SubMenu = "Federation Ships"
Foundation.ShipDef.DS9FXGalaxy.fMaxWarp = 9.9 + 0.0001
Foundation.ShipDef.DS9FXGalaxy.fCruiseWarp = 9.2 + 0.0001
Foundation.ShipDef.DS9FXGalaxy.fCrew = 1015

Foundation.ShipDef.DS9FXGalaxy.desc = "------- DESCRIPTION -------\nThe Galaxy class was first introduced in the late 2350s.  It was the largest and one of the most powerful Federation starship classes of its time, with many serving in the Dominion War.  It was designed to be a multi-purpose mission platform, intended to replace all older classes.  The Galaxy class possesses the most advance general purpose scientific and exploration recourses of any Federation starship class; this makes it ideal for long term exploration missions independent of Starfleet resources.  The Galaxy class was also equipped with state of the art weapon and defensive systems when it was launched in the mid 24th century.  Before the advent of the Federation battleships due to the Borg and Dominion threats, the Galaxy class was the choice class for defending the Federation borders and showing the flag as a deterrent for any hostile moves from neighboring species.  Finally, the Galaxy class was also designed for diplomatic, evacuation, and first contact missions, fulfilling its role as the most capable Federation ship.\n\n------- TACTICS -------\nTake advantage of the wide phaser coverage and disable enemy impulse drive to maximise torpedo impacts.  When attacking the Galaxy class, it is best to disable its shield generator as a priority and then continue to take out its sensor array.\n\n------- SHIP STATS -------\n\nHull Rating: 15000\n\nShield Rating:\n     Fore - 15000 @ 15chg\n     Aft - 15000 @ 15chg\n     Dorsal - 15000 @ 15chg\n     Ventral - 15000 @ 15chg\n     Port - 15000 @ 15chg\n     Starboard - 15000 @ 15chg\n\nImpulse Engines:\n     Max Speed - 7.9\n     Max Accel - 1.9\n     Max Ang Velocity - 0.5\n     Max Ang Accel - 0.3\n\nWarp Engines:\n     Max Warp - 9.9\n     Max Cruise Warp - 9.2\n\nCrew Complement: 1015\n\n------- SHIP WEAPONS -------\n\nPhasers:\n   3xD 2xV 4xA 1xPV 1xSV\n     Max Chg - 1\n     Max Dmg - 500\n     Min Firing Chg - 1\n     Rechg Rate - 0.5\n     Max Damage Distance - 100 \n\nTorpedoes:   \n   8xF 6xA\n     Photon Type 6 - 500\n     Photon Type 6 split 3 - 8\n     Reload Delay - 40\n\n------- SHIP PROPERTIES -------\n\nHull:\n     Max Condition - 15000\n     Repair Complexity - 1\n     Disabled Percentage - 0\n\nLife Support System:\n     Max Condition - 25000\n     Repair Complexity - 1\n     Disabled Percentage - 0.1 \n\nMain Shuttlebay:\n     Max Condition - 3000\n     Repair Complexity - 1 \n     Disabled Percentage - 0 \n\nPhaser Arrays:\n     Max Condition - 3000\n     Repair Complexity - 1\n     Disabled Percentage - 0.3\n\nPhaser System:\n     Max Condition - 4000\n     Repair Complexity - 7\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 400\n\nRepair System:\n     Max Condition - 12000\n     Repair Complexity - 2\n     Disabled Percentage - 0.1\n     Maximum Repair Points - 125\n     Repair Teams - 5\n\nSensor Array:\n     Max Condition - 8000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 130\n     Max # of Probes - 10\n     Sensor Base Range - 3220\n\nShield Generator:\n     Max Condition - 10000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 500\n\nShuttlebay 2:\n     Max Condition - 1000\n     Repair Complexity - 1 \n     Disabled Percentage - 0 \n\nShuttlebay 3:\n     Max Condition - 1500\n     Repair Complexity - 1 \n     Disabled Percentage - 0 \n\nTorpedo Bays:\n   3xF 2xA\n     Max Condition - 3500\n     Repair Complexity - 2\n     Disabled Percentage - 0.25\n\nTorpedo System:\n     Max Condition - 10000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 100\n\nTractor Beam Emitters:\n   2xF 2xA 1xV Main Shuttlebay\n     Max Condition - 2500\n     Repair Complexity - 7\n     Disabled Percentage - 0.25\n\nTractor Beam System:\n     Max Condition - 5000\n     Repair Complexity - 7\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 600\n\nWarp Core:\n     Max Condition - 11000\n     Repair Complexity - 3\n     Disabled Percentage - 0.3 \n     Power Output/Sec - 1900\n     Main Battery Limit - 270000\n     Backup Battery Limit - 100000\n     Main Conduit Capacity - 2000\n     Backup Battery Capacity - 300\n\n------- ENGINE PROPERTIES --------\n\nImpulse Engines:\n     Max Condition - 5000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 250\n\n   Center Impulse:\n     Max Condition - 4000\n     Repair Complexity - 2\n     Disabled Percentage - 0.3 \n\n   Port Impulse:\n     Max Condition - 3000\n     Repair Complexity - 2\n     Disabled Percentage - 0.25 \n\n   Star Impulse:\n     Max Condition - 3000\n     Repair Complexity - 2\n     Disabled Percentage - 0.25  \n\nWarp Engines:\n     Max Condition - 10000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25\n\n   Port Warp:\n     Max Condition - 7000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25 \n\n   Star Warp:\n     Max Condition - 7000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25"

if menuGroup:           Foundation.ShipDef.DS9FXGalaxy.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXGalaxy.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]