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

f_part1    = open('melodycho', 'w')
f_part2    = open('harmonycho', 'w')
cnt        = 0
harmonybag = []
melodybag  = []
bcount     = 0

for file in os.listdir('../data1/'):
	print "File name : " + str(file)
	path       = os.path.join('../data1/', file)
	print "File number : " + str(cnt)
	cnt        = cnt+1
	tree       = ET.parse(path)
	root       = tree.getroot()

	part       = root.find('part')

	measures   = part.findall('measure')
	attributes = measures[0].find('attributes')
	div        = int(attributes.find('divisions').text)
	basic_unit = 64
	dur_unit   = basic_unit/(4*div)

	if len(measures[0].findall('backup')) == 0:
		continue

	for i in range(0,len(measures)-1):
		restflag     = 0
		flag         = 0
		backtime     = 0
		backduration = 0
		j            = 0
		str1         = ''
		str2         = ''
		measure      = measures[i]
		l            = list(measures[i].iter())

		backup       = measures[i].find('backup')
		print "Backup Locations : " + str(backup)
		notes        = measure.findall('note')
		print "Notes amount" + str(len(notes))

		if len(notes) is 0 or backup is None:
			 continue

		if backup is not None:
			idx = l.index(backup) #get index of backup tag
		else:
			flag = 1

		backduration = int(backup.find('duration').text)


		#for melody line
		while(j < len(notes) and (flag == 1 or l.index(notes[j]) < idx)):
			if len(notes[j].findall('rest')) == 1:
				temp     = int(notes[j].find('duration').text)
				backtime = backtime + temp
				if (backtime == backduration):
					restflag = 1
				temp     = temp*dur_unit
				for k in range(0, temp):
					str1 = str1 + "rest "
			else: #is a note
				temp     = int(notes[j].find('duration').text)
				temp     = temp*dur_unit

				if notes[j].find('pitch').find('alter') is not None:
					alter = getAlter(notes[j].find('pitch').find('alter').text)
					st    = notes[j].find('pitch').find('step').text + alter
					st    = same(st)
					st    = st + notes[j].find('pitch').find('octave').text
				else:
					st    = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
				while(j<len(notes)-1 and len(notes[j+1].findall('chord'))==1):
					j         = j + 1
					if notes[j].find('pitch').find('alter') is not None:
						alter = getAlter(notes[j].find('pitch').find('alter').text)
						st1   = notes[j].find('pitch').find('step').text + alter
						st1   = same(st1)
						st    = st + st1 + notes[j].find('pitch').find('octave').text
						st2   = st1 + notes[j].find('pitch').find('octave').text
					else:
						st    = st + notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
						st2   = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text

				if st in melodybag and len(st) > 3:
					st   = st2
				elif len(st) > 3:
					melodybag.append(st)
					st   = st2
				for k in range(0, temp):
					str1 = str1 + st + " "
			j = j + 1
		#f_part1.write('\n')
		#for harmony line
		while(flag == 0 and j < len(notes)):
			if len(notes[j].findall('rest')) == 1:
				temp     = int(notes[j].find('duration').text)
				if (backtime == backduration):
					restflag = 1
				temp     = temp*dur_unit
				for k in range(0, temp):
					str2 = str2 + "rest "
			else: #is a note
				temp     = int(notes[j].find('duration').text)
				temp     = temp*dur_unit

				if notes[j].find('pitch').find('alter') is not None:
					alter = getAlter(notes[j].find('pitch').find('alter').text)
					st    = notes[j].find('pitch').find('step').text + alter
					st    = same(st)
					st    = st + notes[j].find('pitch').find('octave').text
				else:
					st    = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
				while(j<len(notes)-1 and len(notes[j+1].findall('chord'))==1):
					j         = j + 1
					if notes[j].find('pitch').find('alter') is not None:
						alter = getAlter(notes[j].find('pitch').find('alter').text)
						st1   = notes[j].find('pitch').find('step').text + alter
						st1   = same(st1)
						st    = st + st1 + notes[j].find('pitch').find('octave').text
						st2   = st1 + notes[j].find('pitch').find('octave').text
					else:
						st    = st + notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
						st2   = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
				if st in harmonybag and len(st) > 3:
					st   = st2
				elif len(st) > 3:
					harmonybag.append(st)
					st   = st2
				for k in range(0, temp):
					str2 = str2 + st + " "

			j = j + 1
		if (restflag == 1):
			continue
		f_part1.write(str1)
		f_part2.write(str2)
		f_part1.write('\n')
		f_part2.write('\n')
f_part1.close()
f_part2.close()
# print harmonybag
# print melodybag
