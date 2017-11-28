inp = open("input.txt", "r");

i = 0;
j = 0;

array = [[int(n) for n in line.rstrip("\n").split(",")]for line in inp];	
n = array[0][0];
m = array[0][1];
lights = [0]*m
switches =[[0]*m]*n
for i in range(m):
	lights[i] = array[1][i]
for i in range(n):
	switches[i] = array[i+2]
