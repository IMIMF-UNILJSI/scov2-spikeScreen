
"""
Viral strain descriptions based on S-protein

BoJo - B.1.1.7 / VOC-N501Y.V1 / Jolly good England
NeMa - B.1.351 / VOC-N501Y.V2 / South Africa
PaCo - P.1 / VOC-N501Y.V3 / Brasil
Zorro - B.1.429 / GH452R.V1 / California
RoPeMa - B.1.258.17 /  / Slovenia
SunniAli - B.1.525 / Nigeria-Denmark - "Hamlet"
Napoleon - A.27 /France-Mayotte /
FrankSinatra - B.1.526 / USA NY
SunniBaru - B.1.1.318 / Nigeria-USA-UK
MahatmaGandhi_1 B.1.617.1 / Incredible India
MahatmaGandhi_2 B.1.617.2 / VOC-21APR-02 / Incredible India
MahatmaGandhi_3 B.1.617.3 / Incredible India
Delta_plus B.1.617.2 +K417N / Incredible India
Mu B1.621 and B.1.621.1 /South America
AY.4.2 "aka delta plus plus"/ Jolly good England
Omikron - B.1.1.529 / SA
"""

keys = {
	'default': ["BoJo", "NeMa", "PaCo", "Zorro", "RoPeMa", "SunniAli", "SunniBaru", "Napoleon", "FrankSinatra", "MahatmaGandhi_1","MahatmaGandhi_2", "MahatmaGandhi_3", "Delta_plus", "Mu", "AY.4.2.", "Omikron"],
	'v1': ["BoJo", "NeMa", "PaCo"],
	'v2': ["MahatmaGandhi_1", "MahatmaGandhi_2", "MahatmaGandhi_3", "Delta_plus", "Mu", "AY.4.2", "Omikron"]
	}


positions_dict = {
	"BoJo": [
		["A", "-TACATG", "del69_70", 68, "TACATG", ""],
		["T", "-TTA", "del144", 143, "TTA", ""],
		["A", "T", "N501Y", 501, "N", "Y"],
		["C", "A", "A570D", 570, "A", "D"],
		["A", "G", "D614G", 614, "D", "G"],
		["C", "A", "P681H", 681, "P", "H"],
		["C", "T", "T716I", 716, "T", "I"],
		["T", "G", "S982A", 982, "S", "A"],
		["G", "C", "D1118H", 1118, "D", "H"]
	], 
	"NeMa": [
		["X", "X", "D80A", 80, "D", "A"],
		["X", "X", "D215G", 215, "D", "G"],
		["X", "X", "K417N", 417, "K", "N"],
		["X", "X", "E484K", 484, "E", "K"],
		["X", "X", "N501Y", 501, "N", "Y"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "A701V", 701, "A", "V"]
	], 
	"PaCo": [
		["X", "X", "L18F", 18, "L", "F"],
		["X", "X", "T20N", 20, "T", "N"],
		["X", "X", "P26S", 26, "P", "S"],
		["X", "X", "D138Y", 138, "D", "Y"],
		["X", "X", "R190S", 190, "R", "S"],
		["X", "X", "K417T", 417, "K", "T"],
		["X", "X", "E484K", 484, "E", "K"],
		["X", "X", "N501Y", 501, "N", "Y"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "H655Y", 655, "H", "Y"],
		["X", "X", "T1027I", 1027, "T", "I"],
		["X", "X", "V1176F", 1176, "V", "F"]
	],
	"Zorro": [
 		["X", "X", "S13I",13, "S", "I"],
		["X", "X", "W152C", 152, "W", "C"],
		["X", "X", "L452R",452, "L", "R"],
		["X", "X", "D614G", 614, "D", "G"]
  	],
	"RoPeMa": [
		["X", "X", "N439K", 439, "N", "K"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "V772I", 772, "V", "I"]
	],	
	"SunniAli": [
		["X", "X", "Q52R", 52, "Q", "R"],
		["X", "X", "E484K", 484, "E", "K"],
		["X", "X", "Q677H", 677, "Q", "H"],
		["X", "X", "F888L", 888, "F", "L"]
	],
	"SunniBaru": [
		["X", "X", "T95I ", 95, "T", "I"],
		["T", "-TTA", "del144", 143, "TTA", ""],
		["X", "X", "E484K", 484, "E", "K"],
		["X", "X", "D614G", 614, "D", "G"],
		["C", "A", "P681H", 681, "P", "H"],
		["X", "X", "D796H ", 796, "D", "H"]
	],
	"Napoleon": [
		["X", "X", "D796Y ", 796, "D", "Y"],
		["X", "X", "G1219V", 1219, "G", "V"],
		["X", "X", "A653V", 653, "A", "V"],
		["X", "X", "H655Y", 655, "H", "Y"],
		["X", "X", "N501Y", 501, "N", "Y"]
	],
	"FrankSinatra": [
		["X", "X", "T95I ", 95, "T", "I"],
		["X", "X", "D253G", 253, "D", "G"],
		["X", "X", "D614G", 614, "D", "G"]
	],	
	"MahatmaGandhi_1": [
		["X", "X", "L452R", 452, "L", "R"],
		["X", "X", "E484Q", 484, "E", "Q"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "P681R", 681, "P", "R"],
		["X", "X", "Q1071H", 1071, "Q", "H"]
	],	
	"MahatmaGandhi_2": [
		["X", "X", "T19R ", 19, "T", "R"],
		["X", "X", "L452R", 452, "L", "R"],
		["X", "X", "T478K", 478, "T", "K"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "P681R", 681, "P", "R"],
		["X", "X", "D950N", 950, "D", "N"]
	],
	"MahatmaGandhi_3": [
		["X", "X", "T19R ", 19, "T", "R"],
		["X", "X", "L452R", 452, "L", "R"],
		["X", "X", "E484Q", 484, "E", "Q"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "P681R", 681, "P", "R"]
	],
	"Delta_plus": [
		["X", "X", "T19R ", 19, "T", "R"],
		["X", "X", "K417N", 417, "K", "N"],
		["X", "X", "L452R", 452, "L", "R"],
		["X", "X", "T478K", 478, "T", "K"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "P681R", 681, "P", "R"],
		["X", "X", "D950N", 950, "D", "N"]
	],
	"Mu": [
		["X", "X", "T95I ", 95, "T", "I"],
		["X", "X", "Y144S ",144, "Y", "S"],
		["X", "X", "Y145N ",145, "Y", "N"],
		["X", "X", "R346K", 346, "R", "K"],
		["X", "X", "E484K", 484, "E", "K"],
		["A", "T", "N501Y", 501, "N", "Y"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "P681H", 681, "P", "H"],	
		["X", "X", "D950N", 950, "D", "N"]
	],
	"AY.4.2.": [
		["X", "X", "Y145H ",145, "Y", "H"],
		["X", "X", "A222V ",222, "A", "V"]
	],
	"Omikron": [
		["X", "X", "A67V", 67, "A", "V"],
		["A", "-TACATG", "del69_70", 68, "TACATG", ""],
		["X", "X", "T95I", 95, "T", "I"],
		["X", "X", "G142D", 142, "G", "D"],
		["X", "X", "L212I", 212, "L", "I"],
		["X", "X", "G339D", 339, "G", "D"],
		["X", "X", "S371L", 371, "S", "L"],
		["X", "X", "S373P", 373, "S", "P"],
		["X", "X", "S375F", 375, "S", "F"],
		["X", "X", "K417N", 417, "K", "N"],
		["X", "X", "N440K", 440, "N", "K"],
		["X", "X", "G446S", 446, "G", "S"],
		["X", "X", "S477N", 477, "S", "N"],
		["X", "X", "T478K", 478, "T", "K"],
		["X", "X", "E484A", 484, "E", "A"],
		["X", "X", "Q493K", 493, "Q", "K"],
		["X", "X", "G496S", 496, "G", "S"],
		["X", "X", "Q498R", 498, "Q", "R"],
		["A", "T", "N501Y", 501, "N", "Y"],
		["X", "X", "Y505H", 505, "Y", "H"],
		["X", "X", "T547K", 547, "T", "K"],
		["X", "X", "D614G", 614, "D", "G"],
		["X", "X", "H655Y", 655, "H", "Y"],
		["X", "X", "N679K", 679, "N", "K"],
		["X", "X", "P681H", 681, "P", "H"],
		["X", "X", "N764K", 764, "N", "K"],
		["X", "X", "D796Y", 796, "D", "Y"],
		["X", "X", "N856K", 856, "N", "K"],
		["X", "X", "Q954H", 954, "Q", "H"],
		["X", "X", "N969K", 969, "N", "K"],
		["X", "X", "L981F", 981, "L", "F"]
	]

}

