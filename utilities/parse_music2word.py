import xml.etree.ElementTree as ET

tree = ET.parse('/home/vasudha/Desktop/Output.xml')
root = tree.getroot()

part = root.find('part')

measures = part.findall('measure')
attributes = measures[0].find('attributes')
div = int(attributes.find('divisions').text)
basic_unit = 64
dur_unit = basic_unit/(4*div)

f_part1 = open('part1', 'w')
f_part2 = open('part2', 'w')

for i in range(0,len(measures)):
	measure = measures[i]
	l = list(measures[i].iter())
	backup = measures[i].find('backup')
	idx = l.index(backup) #get index of backup tag
	notes = measure.findall('note')
	j = 0
	#for melody line
	while(l.index(notes[j]) < idx):
		if len(notes[j].findall('rest')) == 1:
			temp = int(notes[j].find('duration').text)
			temp = temp*dur_unit
			for k in range(0, temp):
				f_part1.write('rest')
				f_part1.write(' ')
		else: #is a note
			temp = int(notes[j].find('duration').text)
			temp = temp*dur_unit
			st = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
			while(j<len(notes)-1 and len(notes[j+1].findall('chord'))==1):
				j = j + 1
				st = st + notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
			for k in range(0, temp):
				f_part1.write(st)
				f_part1.write(' ')
		j = j+1

	#for harmony line
	while(j < len(notes)):
		if len(notes[j].findall('rest')) == 1:
			temp = int(notes[j].find('duration').text)
			temp = temp*dur_unit
			for k in range(0, temp):
				f_part2.write('rest')
				f_part2.write(' ')
		else: #is a note
			temp = int(notes[j].find('duration').text)
			temp = temp*dur_unit
			st = notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
			while(j<len(notes)-1 and len(notes[j+1].findall('chord'))==1):
				j = j + 1
				st = st + notes[j].find('pitch').find('step').text + notes[j].find('pitch').find('octave').text
			for k in range(0, temp):
				f_part2.write(st)
				f_part2.write(' ')
		j = j+1

f_part1.close()
f_part2.close()
