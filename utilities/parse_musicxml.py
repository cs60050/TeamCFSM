import xml.etree.ElementTree as ET

tree = ET.parse('/home/shaswat/Desktop/Output.xml')
root = tree.getroot()

parts = root.findall('part')
part1 = parts[0]
part2 = parts[1]

part1_measures = part1.findall('measure')
part2_measures = part2.findall('measure')

f_part1 = open('part1', 'w')
f_part2 = open('part2', 'w')

for i in range(0,len(part1_measures)):
	measure1 = part1_measures[i]
	measure2 = part2_measures[i]

	#for part1
	notes1 = measure1.findall('note')
	for j in range(0, len(notes1)):
		if len(notes1[j].findall('rest')) == 1:
			if j==len(notes1)-1:
				f_part1.write('rest')
				f_part1.write('-')
				temp = int(notes1[j].find('duration').text)#/10080
				f_part1.write(str(temp))
			else:
				f_part1.write('rest')
				f_part1.write('-')
				temp = int(notes1[j].find('duration').text)#/10080
				f_part1.write(str(temp))
				f_part1.write(' ')
		else: #is a note
			f_part1.write(notes1[j].find('pitch').find('step').text)
			f_part1.write(notes1[j].find('pitch').find('octave').text)
			f_part1.write('-')
			f_part1.write(str(int(notes1[j].find('duration').text)))

			if j<len(notes1)-1:
				if len(notes1[j+1].findall('chord'))==0:
					f_part1.write(' ')
	#f_part1.write('\n')

	#for part2
	notes2 = measure2.findall('note')
	for j in range(0, len(notes2)):
		if len(notes2[j].findall('rest')) == 1:
			if j == len(notes2)-1:
				f_part2.write('rest')
				f_part2.write('-')
				temp = int(notes2[j].find('duration').text)#/10080
				f_part2.write(str(temp))
			else:
				f_part2.write('rest')
				f_part2.write('-')
				temp = int(notes2[j].find('duration').text)#/10080
				f_part2.write(str(temp))
				f_part2.write(' ')
		else: #is a note
			f_part2.write(notes2[j].find('pitch').find('step').text)
			f_part2.write(notes2[j].find('pitch').find('octave').text)
			f_part2.write('-')
			f_part2.write(str(int(notes2[j].find('duration').text)))

			if j<len(notes2)-1:
				if len(notes2[j+1].findall('chord'))==0:
					f_part2.write(' ')
	#f_part2.write('\n')

f_part1.close()
f_part2.close()