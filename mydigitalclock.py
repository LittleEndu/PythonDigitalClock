#Made by Endrik "LittleEndu" Tombak
#Made on 2015-11-21

from datetime import datetime
from turtle import *

def drawNr(xx,ll):
	if xx==0:
		setx(xcor()+ll)
		sety(ycor()-ll*2)
		setx(xcor()-ll)
		sety(ycor()+ll*2)
	elif xx==1:
		up()
		setx(xcor()+ll)
		down()
		sety(ycor()-ll*2)
		up()
		goto(xcor()-ll,ycor()+ll*2)
		down()
	elif xx==2:
		setx(xcor()+ll)
		sety(ycor()-ll)
		setx(xcor()-ll)
		sety(ycor()-ll)
		setx(xcor()+ll)
		up()
		goto(xcor()-ll,ycor()+ll*2)
		down()
	elif xx==3:
		setx(xcor()+ll)
		sety(ycor()-ll*2)
		setx(xcor()-ll)
		up()
		sety(ycor()+ll)
		down()
		setx(xcor()+ll)
		up()
		goto(xcor()-ll,ycor()+ll)
		up()
	elif xx==4:
		sety(ycor()-ll)
		setx(xcor()+ll)
		sety(ycor()-ll)
		sety(ycor()+ll*2)
		up()
		setx(xcor()-ll)
		down()
	elif xx==5:
		sety(ycor()-ll)
		setx(xcor()+ll)
		sety(ycor()-ll)
		setx(xcor()-ll)
		up()
		goto(xcor()+ll,ycor()+ll*2)
		down()
		setx(xcor()-ll)
	elif xx==6:
		sety(ycor()-ll*2)
		setx(xcor()+ll)
		sety(ycor()+ll)
		setx(xcor()-ll)
		up()
		goto(xcor()+ll,ycor()+ll)
		down()
		setx(xcor()-ll)
	elif xx==7:
		setx(xcor()+ll)
		sety(ycor()-ll*2)
		up()
		goto(xcor()-ll,ycor()+ll)
		down()
		sety(ycor()+ll)
	elif xx==8:
		sety(ycor()-ll*2)
		setx(xcor()+ll)
		sety(ycor()+ll)
		setx(xcor()-ll)
		setx(xcor()+ll)
		sety(ycor()+ll)
		setx(xcor()-ll)
	elif xx==9:
		sety(ycor()-ll)
		setx(xcor()+ll)
		sety(ycor()-ll)
		setx(xcor()-ll)
		setx(xcor()+ll)
		sety(ycor()+ll*2)
		setx(xcor()-ll)
	else:
		drawNr(xx//10,ll)
		goRight(ll)
		drawNr(xx%10,ll)
def increment(xx,ll,tt=0):
	if xx==0:
		pencolor("#FFFFFF")
		sety(ycor()-ll*2)
		setx(xcor()+ll)
		up()
		sety(ycor()+ll*2)
		down()
		setx(xcor()-ll)
		pencolor("#000000")
	elif xx==1:
		setx(xcor()+ll)
		sety(ycor()-ll)
		setx(xcor()-ll)
		sety(ycor()-ll)
		setx(xcor()+ll)
		pencolor("#FFFFFF")
		sety(ycor()+ll)
		up()
		goto(xcor()-ll,ycor()+ll)
		down()
		pencolor("#000000")
	elif xx==2 and tt!=2:
		up()
		sety(ycor()-ll)
		down()
		pencolor("#FFFFFF")
		sety(ycor()-ll)
		pencolor("#000000")
		setx(xcor()+ll)
		sety(ycor()+ll*2)
		setx(xcor()-ll)
	elif xx==2 and tt==2:
		sety(ycor()-ll*2)
		setx(xcor()+ll)
		sety(ycor()+ll)
		pencolor("#FFFFFF")
		setx(xcor()-ll)
		pencolor("#000000")
		sety(ycor()+ll)
	elif xx==3:
		sety(ycor()-ll)
		up()
		sety(ycor()-ll)
		down()
		pencolor("#FFFFFF")
		setx(xcor()+ll)
		pencolor("#000000")
		up()
		pencolor("#FFFFFF")
		sety(ycor()+ll*2)
		down()
		setx(xcor()-ll)
		pencolor("#000000")
	elif xx==4:
		setx(xcor()+ll)
		pencolor("#FFFFFF")
		sety(ycor()-ll)
		pencolor("#000000")
		sety(ycor()-ll)
		setx(xcor()-ll)
		up()
		sety(ycor()+ll*2)
		down()
	elif xx==5 and tt!=5:
		sety(ycor()-ll*2)
		sety(ycor()+ll*2)
	elif xx==5 and tt==5:
		setx(xcor()+ll)
		sety(ycor()-ll*2)
		setx(xcor()-ll)
		sety(ycor()+ll)
		pencolor("#FFFFFF")
		setx(xcor()+ll)
		pencolor("#000000")
		up()
		goto(xcor()-ll,ycor()+ll)
		down()
	elif xx==6:
		setx(xcor()+ll)
		sety(ycor()-ll)
		setx(xcor()-pensize())
		pencolor("#FFFFFF")
		setx(xcor()-ll+pensize())
		sety(ycor()-ll)
		setx(xcor()+ll)
		pencolor("#000000")
		up()
		goto(xcor()-ll,ycor()+ll*2)
		down()
	elif xx==7:
		up()
		goto(xcor()+ll,ycor()-ll)
		down()
		setx(xcor()-ll)
		sety(ycor()-ll)
		setx(xcor()+ll)
		up()
		goto(xcor()-ll,ycor()+ll*2)
		down()
	elif xx==8:
		sety(ycor()-ll)
		pencolor("#FFFFFF")
		sety(ycor()-ll)
		pencolor("#000000")
		up()
		sety(ycor()+ll*2)
		down()
	elif xx==9:
		sety(ycor()-ll*2)
		up()
		goto(xcor()+ll,ycor()+ll)
		down()
		pencolor("#FFFFFF")
		setx(xcor()-ll)
		pencolor("#000000")
		sety(ycor()+ll)
def goLeft(ll,multi=3):
	up()
	setx(xcor()-pensize()*multi-ll-5)
	down()
def goRight(ll,multi=3):
	up()
	setx(xcor()+pensize()*multi+ll+5)
	down()
def backToZero(ll):
	sety(ycor()-ll*2)
	sety(ycor()+ll)
	pencolor("#FFFFFF")
	setx(xcor()+ll)
	pencolor("#000000")
	up()
	goto(xcor()-ll,ycor()+ll)
	down()
def wrong():
	if	datetime.now().second%10!=digits[5]:
		return True
	elif datetime.now().second//10!=digits[4]:
		return True
	elif datetime.now().minute%10!=digits[3]:
		return True
	elif datetime.now().minute//10!=digits[2]:
		return True
	elif datetime.now().hour%10!=digits[1]:
		return True
	elif datetime.now().hour//10!=digits[0]:
		return True
	else:
		return False

speed(8)
wrongAmount=0
length=50
pensize(6)
up()
goRight(length,1)
up()
sety(-length)
down()
circle(1)
up()
goto(0,0)
goLeft(length*2,1.5)
up()
sety(pensize()*3)
down()
circle(1)
up()
sety(-pensize()*3)
down()
circle(1)
up()
goto(0,0)
sety(length)
goLeft(length*4.1,9)
down()
speed(3)
digits=[] 
digits.append(datetime.now().hour//10)
digits.append(datetime.now().hour%10)
digits.append(datetime.now().minute//10)
digits.append(datetime.now().minute%10)
digits.append(datetime.now().second//10)
digits.append(datetime.now().second%10) #I know this is not necessary but it looks nicer
for i in range(5):
	drawNr(digits[i],length)
	if i%2==1:
		goRight(length*1.6)
	else:
		goRight(length)
drawNr(digits[5],length)

while True:
	if wrongAmount>0 and wrongAmount<5:
		speed(5+wrongAmount)
	if wrong():
		wrongAmount+=1
		increment(digits[5],length)
		digits[5]+=1
		if digits[5]>9:
			digits[5]%=10
			goLeft(length)
			increment(digits[4],length,5)
			digits[4]+=1
			if digits[4]>5:
				digits[4]%=6
				goLeft(length*1.6)
				increment(digits[3],length)
				digits[3]+=1
				if digits[3]>9:
					digits[3]%=10
					goLeft(length)
					increment(digits[2],length,5)
					digits[2]+=1
					if digits[2]>5:
						digits[2]%=6
						goLeft(length*1.6)
						if digits[0]==2 and digits[1]==3:
							digits[0]=0
							digits[1]=0
							goLeft(length)
							increment(2,length,2)
							goRight(length)
							backToZero(length)
						else:
							increment(digits[1],length)
							digits[1]+=1
						if digits[1]>9:
							digits[1]%10
							goLeft(length)
							increment(digits[0],length)
							digits[0]+=1
							goRight(length)
						goRight(length*1.6)				
					goRight(length)
				goRight(length*1.6)
			goRight(length)
	else:
		wrongAmount=0
		speed(5)
	
