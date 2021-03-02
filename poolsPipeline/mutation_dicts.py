
"""
Viral strain descriptions based on S-protein

BoJo - B.1.1.7 / VOC-N501Y.V1 / Jolly good England
NeMa - B.1.351 / VOC-N501Y.V2 / South Africa
PaCo - P.1 / VOC-N501Y.V3 / Brasil
Zorro - B.1.429 / GH452R.V1 / California
RoPeMa - B.1.258.17 /  / Slovenia


"""

keys = {
	'default': ["BoJo", "NeMa", "PaCo", "Zorro", "RoPeMa", "SunniAli"],
	'v1': ["BoJo", "NeMa", "PaCo"]
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
		["X", "X", "W152C", 152, "W", "C"]
		["X", "X", "L452R",452, "L", "R"],
		["X", "X", "D614G", 614, "D", "G"],
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
		["X", "X", "F888L", 888, "F", "L"],
	]
	
}
