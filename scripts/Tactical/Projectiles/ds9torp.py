import App
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 163.0 / 255.0, 0.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 205.0 / 130.0, 100.0 / 255.0, 1.000000)
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					0.2,	 
					"data/Textures/Tactical/ds9torp.tga", 
					kGlowColor,
					2.3,	
					0.5,	 
					0.8,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.4,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)
	return(0)

def GetLaunchSpeed():
	return 45.0

def GetLaunchSound():
	return "ds9torp"

def GetPowerCost():
	return 10.0 

def GetName():
	return "Photon Type 6"

def GetDamage():
	return 850.0

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 3.0
