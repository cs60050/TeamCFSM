import xml.etree.ElementTree as ET
import os

def getAlter(alter): #for flats and sharps
	if alter == '1':
		alter = '#'
	elif(alter == '-1'):
		alter = 'b'
	elif(alter == '2'):
		alter = 'x'
	elif(alter == '-2'):
		alter = 'y'
	return alter

def same(st): #for notes representing the same thing
	if(st == 'Db' or st == 'Bx'):
		st = 'C#'
	elif(st == 'Eb' or st == 'Fy'):
		st = 'D#'
	elif(st == 'E#' or st == 'Gy'):
		st = 'F'
	elif(st == 'Fb' or st == 'Dx'):
		st = 'E'
	elif(st == 'Gb' or st == 'Ex'):
		st = 'F#'
	elif(st == 'Ab'):
		st = 'G#'
	elif(st == 'Bb' or st == 'Cy'):
		st = 'A#'
	elif(st == 'B#' or st == 'Dy'):
		st = 'C'
	elif(st == 'Cb' or st == 'Ax'):
		st = 'B'
	elif(st == 'Ey' or st == 'Cx'):
		st = 'D'
	elif(st == 'Ay' or st == 'Fx'):
		st = 'G'
	elif(st == 'By' or st == 'Gx'):
		st = 'A'
	return st

f_part1 = open('part1', 'w')
f_part2 = open('part2', 'w')
cnt = 0
for file in os.listdir('/home/vasudha/TeamCFSM/data/'):
	print(file)
	path = os.path.join('/home/vasudha/TeamCFSM/data/', file)
	print(cnt)
	cnt = cnt+1
	tree = ET.parse(path)
	root = tree.getroot()

	part = root.find('part')

	measures = part.findall('measure')
	attributes = measures[0].find('attributes')
	div = int(attributes.find('divisions').text)
	basic_unit = 64
	dur_unit = basic_unit/(4*div)
	
	for i in range(0,len(measures)):
		flag = 0
		measure = measures[i]
		l = list(measures[i].iter())
		backup = measures[i].find('backup')
		notes = measure.findall('note')
		if notes is None: continue
		if backup is not None:
			idx = l.index(backup) #get index of backup tag
		else: flag = 1
		j = 0
		#for melody line
		while(j < len(notes) and (flag == 1 or l.index(notes[j]) < idx)):
			if len(notes[j].findall('rest')) == 1:
				temp = int(notes[j].find('duration').text)
				temp = temp*dur_unit
				for k in range(0, temp):
					f_part1.write('rest')
					f_part1.write(' ')
			else: #is a note
				temp = int(notes[j].find('duration').text)
				temp = temp*dur_unit
				
				if notes[j].find('pitch').find('alter') is not None:
					alter = getAlter(notes[j].find('pitch').find('alter').text)				
					st = notes[j].find('pitch').find('step').text + alter
					st = same(st)
					st = st + notes[j].find('pitch').find('octave').text
				else:
					st = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
				while(j<len(notes)-1 and len(notes[j+1].findall('chord'))==1):
					j = j + 1
					
					if notes[j].find('pitch').find('alter') is not None:
						alter = getAlter(notes[j].find('pitch').find('alter').text)			
						st1 = notes[j].find('pitch').find('step').text + alter
						st1 = same(st1)
						st = st + st1 + notes[j].find('pitch').find('octave').text
					else:
						st = st + notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
				for k in range(0, temp):
					f_part1.write(st)
					f_part1.write(' ')
			j = j+1

		#for harmony line
		while(flag == 0 and j < len(notes)):
			if len(notes[j].findall('rest')) == 1:
				temp = int(notes[j].find('duration').text)
				temp = temp*dur_unit
				for k in range(0, temp):
					f_part2.write('rest')
					f_part2.write(' ')
			else: #is a note
				temp = int(notes[j].find('duration').text)
				temp = temp*dur_unit
				
				if notes[j].find('pitch').find('alter') is not None:
					alter = getAlter(notes[j].find('pitch').find('alter').text)				
					st = notes[j].find('pitch').find('step').text + alter
					st = same(st)
					st = st + notes[j].find('pitch').find('octave').text
				else:
					st = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
				while(j<len(notes)-1 and len(notes[j+1].findall('chord'))==1):
					j = j + 1
					
					if notes[j].find('pitch').find('alter') is not None:
						alter = getAlter(notes[j].find('pitch').find('alter').text)				
						st1 = notes[j].find('pitch').find('step').text + alter
						st1 = same(st1)
						st = st + st1 + notes[j].find('pitch').find('octave').text
					else:
						st = st + notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
				for k in range(0, temp):
					f_part2.write(st)
					f_part2.write(' ')
			j = j+1
	
f_part1.close()
f_part2.close()
