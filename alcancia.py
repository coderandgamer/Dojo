print "canto quieres ahorrar?";
sumatoria=0;
dinero=int(raw_input());
while True:
	print "canto quieres depositar";
	cantidad=int(raw_input());
	sumatoria=sumatoria+cantidad;
	if sumatoria >=dinero:
		print "feliicidades";
		break; 
	else:
		print "te falta",(dinero-sumatoria)	
