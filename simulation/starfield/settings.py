width = 700
height = 700


def map(x, oMin, oMax, nMin, nMax):
	#range check
	if oMin == oMax:
		print('Warning : Zero Input Range')
		return None

	if nMin == nMax:
		print('Warning : Zero Output Range')
		return None

	# Check reverse input range
	reverseInput = False
	oldMin = min(oMin, oMax)
	oldMax = max(oMin, oMax)
	if not oldMin == oMin:
		reverseInput = True

	# Check reverse output range
	reverseOutput = False
	newMin = min(nMin, nMax)
	newMax = max(nMin, nMax)
	if not newMin == nMin:
		reverseOutput = True

	portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
	if reverseInput:
		portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

	result = portion + newMin
	if reverseOutput:
		result = newMax - portion

	return result 


