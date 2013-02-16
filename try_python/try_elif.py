#!/usr/bin/env python

#declare lists
oem=['ASUS','Samsung','LG']
flagship=['Padafone','SIII','Optimus G']

#ask OEM and flagship
ques=raw_input('Enter the OEM: ')
ans=raw_input('Enter the flagship:')

#check if they correspond correctly
if ques in oem:
	position=oem.index(ques)
	if oem[position]==ans[position]
		print "Hey, you got the correct answer..!!"
		print "The device %s is manufactured by %s.." %ans %ques
	else:
		print "Oops..!! You are wrong.."
else:
	print "You entered the invalid arguments..!!"
