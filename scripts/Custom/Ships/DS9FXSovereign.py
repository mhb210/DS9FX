import App
import Foundation

abbrev = "DS9FXSovereign"
iconName = "DS9FXSovereign"
longName = "Sovereign"
shipFile = "DS9FXSovereign"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"

Foundation.ShipDef.DS9FXSovereign = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DS9FXSovereign.SubMenu = "Federation Ships"
Foundation.ShipDef.DS9FXSovereign.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.DS9FXSovereign.fCruiseWarp = 9.7 + 0.0001
Foundation.ShipDef.DS9FXSovereign.fCrew = 885
Foundation.ShipDef.DS9FXSovereign.dTechs = {
   "Fed Ablative Armor": {"Plates": ["Forward Armor","Aft Armor","Port Armor","Starboard Armor"]}
}

Foundation.ShipDef.DS9FXSovereign.desc = "------- DESCRIPTION -------\nHeavily armed, the design philosophy for the Sovereign class was shaped by the discovery of the Borg. The Sovereign Project attempted to push the envelope as far as possible when it came to computer power, shields, armament, and systems capabilities. The Sovereign class starship combined the creature comforts associated with the larger Galaxy-class vessels with the tactical power of the new Prometheus-class. The vessel included some of Starfleet\'s most recent technological advances. Primary amongst these was a large quantum torpedo launcher mounted forward of the deflector dish above the Captain\'s yacht, which was capable of firing at least four rounds per second. Backup to the quantum torpedoes was provided by photon tubes. The warp engines of the Sovereigns were of a new design which eliminated subspace distortion effects inherent to standard warp drives without the use of variable geometry nacelles. One of the Sovereign class\' first major engagements came in 2373, when the USS Enterprise saw action in the Borg incursion into Sector 001, and was instrumental in the destruction of the attacking cube. Shortly after the resolution of the Dominion War, a refitting of the Sovereign class took place. These included three extra aft facing torpedo tubes, along with one more forward facing tube; a twin launcher aft of the bridge, single launchers above the aft hangar deck, and at the base of the forward bridge terracing. Additionally, four extra phaser arrays were added to the nacelle pylons to cover an existing blind spot. The Enterprise was able to deploy these new systems in 2379 when it faced the Reman Scimitar in the Bassen Rift. \n\n------- TACTICS -------\nAttack enemy ships by concentrating its burst phasers and deploying its rapid firing photon and quantum torpedoes. When attacking the Sovereign it is advisable to do so as part of a dual attack force to divert the ships weapons. Disabling the Sovereigns shields would leave the ship vulverable allowing its weapon systems to be disabled.\n\n------- SHIP STATS -------\n\nAblative Armor Rating: 6000\n\nHull Rating: 18000\n\nShield Rating:\n     Fore - 16000 @ 16chg\n     Aft - 16000 @ 16chg\n     Dorsal - 16000 @ 16chg\n     Ventral - 16000 @ 16chg\n     Port - 16000 @ 16chg\n     Starboard - 16000 @ 16chg\n\nImpulse Engines:\n     Max Speed - 9.98\n     Max Accel - 4.9\n     Max Ang Velocity - 0.6\n     Max Ang Accel - 0.6\n\nWarp Engines:\n     Max Warp - 9.99\n     Max Cruise Warp - 9.7\n\nCrew Complement: 885\n\n------- SHIP WEAPONS -------\n\nPhasers:\n   15xD 11xV 4xA\n     Max Chg - 0.75\n     Max Dmg - 1000\n     Min Firing Chg - 0.75\n     Rechg Rate - 0.75\n     Max Damage Distance - 100\n\nQuantum Pulse Turrets:\n   4xF\n     Max Chg - 1\n     Max Dmg - 1300\n     Min Firing Chg - 1\n     Rechg Rate - 0.34\n     Cooldown Time - 45\n\nTorpedoes:\n   6xF 6xA\n     Enhanced Photon Type 6 - 500\n     Reload Delay - 60\n\n\n------- SYSTEMS STATS -------\n\nAblative Armor:\n     Max Condition - 6000\n     Repair Complexity - 7\n     Disabled Percentage - 0.5\n\nHull:\n     Max Condition - 18000\n     Repair Complexity - 1\n     Disabled Percentage - 0\n\nLife Support System:\n     Max Condition - 35000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.1\n\nPhaser Arrays:\n     Max Condition - 1000\n     Repair Complexity - 7 \n     Disabled Percentage - 0.75 \n\nPhaser System:\n     Max Condition - 8000\n     Repair Complexity - 7 \n     Disabled Percentage - 0.75  \n     Normal Power/Sec - 400\n\nQuantum Pulse Turrets:\n     Max Condition - 2000\n     Repair Complexity - 1\n     Disabled Percentage - 0.5\n\nQuantum Pulse Turret System:\n     Max Condition - 2200\n     Repair Complexity - 1\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 1\n\nRepair System:\n     Max Condition - 1200\n     Repair Complexity - 1\n     Disabled Percentage - 0.01\n     Maximum Repair Points - 100\n     Repair Teams - 7\n\nSensor Array:\n     Max Condition - 8000\n     Repair Complexity - 1\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 150\n     Max # of Probes - 10\n     Sensor Base Range - 2400\n\nShield Generator:\n     Max Condition - 16000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 600\n\nTorpedo Bays:\n   3xF 6xA\n     Max Condition - 2200\n     Repair Complexity - 3\n     Disabled Percentage - 0.75\n\nTorpedo System:\n     Max Condition - 6000\n     Repair Complexity - 3\n     Disabled Percentage - 0.75\n     Normal Power/Sec - 150\n\nTractor Beam Emitters:\n   2xF 2xA   \n     Max Condition - 1500\n     Repair Complexity - 7\n     Disabled Percentage - 0.75\n\nTractor Beam System:\n     Max Condition - 3000\n     Repair Complexity - 7\n     Disabled Percentage - 0.75\n     Normal Power/Sec - 700\n\nWarp Core:\n     Max Condition - 7000\n     Repair Complexity - 2\n     Disabled Percentage - 0.5\n     Power Output/Sec - 2000\n     Main Battery Limit - 200000\n     Backup Battery Limit - 100000\n     Main Conduit Capacity - 2500\n     Backup Battery Capacity - 300\n\n------- ENGINE PROPERTIES -------\n\nImpulse Engines:\n     Max Condition - 3000\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 200\n\n   Port Impulse:\n     Max Condition - 3000\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n\n   Star Impulse:\n     Max Condition - 3000\n     Repair Complexity - 3\n     Disabled Percentage - 0.5 \n\nWarp Engines:\n     Max Condition - 8000\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n\n   Port Warp:\n     Max Condition - 1500\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n\n   Star Warp:\n     Max Condition - 1500\n     Repair Complexity - 3\n     Disabled Percentage - 0.5"

if menuGroup:           Foundation.ShipDef.DS9FXSovereign.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXSovereign.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]