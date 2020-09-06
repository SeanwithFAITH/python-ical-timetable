import datetime
from datetime import datetime, timedelta

maxWeek = 16+1
classTime = [None, (8, 00), (9, 00), (10, 10), (11, 10), (13, 30), (14, 30),
	(15, 20), (16, 00), (18, 00), (19, 00), (20, 00),None]
weeks = [None]
starterDay = datetime(2020, 9, 7)
for i in range(1, maxWeek):
	singleWeek = [None]
	for d in range(0, 7):
		singleWeek.append(starterDay)
		starterDay = starterDay + timedelta(days = 1)
	weeks.append(singleWeek)

def rgWeek(startWeek, endWeek): return list(range(startWeek, endWeek + 1))
def oeWeek(startWeek, endWeek, mode):
	allWeek = range(startWeek, endWeek + 1)
	oddWeek = []; evenWeek = []
	for w in allWeek:
		if w % 2 == 0: evenWeek.append(w)
		else: oddWeek.append(w)
	if mode: return oddWeek
	else: return evenWeek

classes = [
	# [Name, Teacher, Classmates, Location, classID, classWeek, classWeekday, classOrder]
	# [Name, Location, Teacher, classID, classWeek, classWeekday, classOrder]
	["计算机网络","计算机机房A-主楼803","迟绍翠","2111010021",rgWeek(9,16),3,[1,2]],
	["计算机网络","四十八教A407","田佳音","2111010021",rgWeek(1,16),1,[3,4]],
	["计算机网络","一教414-分屏","田佳音","2111010021",rgWeek(1,4),3,[1,2]],
	["计算机图形学","一教302-分屏","严明","2111030144",rgWeek(1,16),5,[1,2]],
	["计算机图形学","计算机机房A-主楼803","严明","2111030144",rgWeek(9,16),5,[9,10]],
	["机器学习导论","一教514-国际","吴晓雨","2111030165",rgWeek(1,16),4,[3,4]],
	["大数据与数据挖掘技术","一教413-触控","王鑫","2111030249",rgWeek(1,16),2,[5,6]],
	["大数据与数据挖掘技术","数字视频技术实验室-主楼504","王鑫","2111030249",oeWeek(8,14,0),4,[1,2]],
	["大数据与数据挖掘技术","数字视频技术实验室-主楼504","王鑫","2111030249",oeWeek(8,14,0),2,[1,2]],
	["Java程序设计基础","计算机基础公共教学实验室5机房(B108)","刘青","1131020668",[11],4,[9,10]],
	["Java程序设计基础","计算机基础公共教学实验室5机房(B108)","刘青","1131020668",rgWeek(1,5)+rgWeek(6,10),4,[9,11]],
	["数字图像处理A","四十八教A808","杨磊","2111030151",rgWeek(1,16),2,[3,4]],
	["数字图像处理A","数字视频技术实验室-主楼504","雷玲","2111030151",rgWeek(12,15),1,[9,12]],
	["体感交互虚拟系统设计训练*","数字信号处理（DSP）实验室-主楼616","马海燕","2111030184",rgWeek(1,16),1,[1,2]],
	["通信原理B","一教308-分屏","李建平","2111030010",rgWeek(1,16),5,[5,6]],
	["信息论与编码原理B","一教508","张亚娜","2111030074",rgWeek(1,8),5,[3,4]],
	["信息论与编码原理B","一教514-国际","张亚娜","2111030074",rgWeek(1,8),1,[5,6]],
]

iCalHeader = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
PRODID:-//Apple Inc.//Mac OS X 10.14.6//EN
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
END:VTIMEZONE"""

createNow = datetime.now() - timedelta(hours = 8)
dtStamp = createNow.strftime('%Y%m%dT%H%M%SZ')

allvEvent = ""

for Class in classes:
	# [Name, Teacher, Classmates, Location, classID, classWeek, classWeekday, classOrder] = Class[:]
	[Name, Teacher, Location, classID, classWeek, classWeekday, classOrder] = Class[:]
	Title = Name + " - " + Location
# 	if "D1" in Location: customGEO = """LOCATION:重庆大学虎溪校区第一教学楼\\n大学城南路55号重庆大学虎溪校区
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=337.55;X-TITLE=重庆大学虎溪校区
#  第一教学楼\\\\n大学城南路55号重庆大学虎溪校区:geo:29.595578,106.301135"""
# 	if "DZ" in Location: customGEO = """LOCATION:重庆大学虎溪校区综合楼\\n大学城南路55号重庆大学虎溪校区
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=340.61;X-TITLE=重庆大学虎溪校区
#  综合楼\\\\n大学城南路55号重庆大学虎溪校区:geo:29.596055,106.299510"""
# 	if "DYC" in Location: customGEO = """LOCATION:重庆大学虎溪校区艺术楼\\n大学城南路55号重庆大学虎溪校区
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=434.41;X-TITLE=重庆大学虎溪校区
#  艺术楼\\\\n大学城南路55号重庆大学虎溪校区:geo:29.593464,106.304183"""
# 	if "D东大门" in Location: customGEO = """LOCATION:重庆大学虎溪校区(东门)\\n虎溪镇
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=686.05;X-TITLE=重庆大学虎溪校区
#  (东门)\\\\n虎溪镇:geo:29.594176,106.307050"""

	Description = " 任课教师" + Teacher + " 课序号" + classID + "。"
	classStartTime = []; classEndTime = []
	for timeWeek in classWeek:
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime.append(weeks[timeWeek][classWeekday] + timedelta(minutes = startTime[0] * 60 + startTime[1]))
		classEndTime.append(weeks[timeWeek][classWeekday] + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45))

	for i in range(len(classStartTime)):
		vEvent = "\nBEGIN:VEVENT"
		vEvent += "\nDTEND;TZID=Asia/Shanghai:" + classEndTime[i].strftime('%Y%m%dT%H%M%S')
		vEvent += "\nSUMMARY:" + Title
		vEvent += "\nDTSTAMP:" + dtStamp
		vEvent += "\nDTSTART;TZID=Asia/Shanghai:" + classStartTime[i].strftime('%Y%m%dT%H%M%S')
		vEvent += "\nDESCRIPTION:" + Description
		# vEvent += "\n" + customGEO
		vEvent += "\nEND:VEVENT"
		allvEvent += vEvent

jWrite = open("/Users/junyi_lou/Desktop/课表.ics", "w")
jWrite.write(iCalHeader + allvEvent + "\nEND:VCALENDAR")
jWrite.close(); exit()