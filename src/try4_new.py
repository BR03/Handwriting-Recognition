from final_pre_process_2 import *
import cv2

outlist = []

l = ["name", "email", "no", "date", "rate"]

for i in l:
	img = cv2.imread("../check/"+i+".png", cv2.IMREAD_GRAYSCALE)
	outlist.append(img)

hopefully_ans = RowOCR(outlist)
print("hopefully_ans",hopefully_ans)
f = open("Data.txt","w+")
entry = ''
for i in hopefully_ans:    
	for j in i[1:]:
		entry += j+","
	entry = entry[:-1]

f.write(entry)
