#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def panduanhusu(a,b):
	if a < b:
		a,b=b,a
	while b != 0:
		flag = a%b
		a = b
		b = flag
	if (a,b) == (1,0):
		return 1
	else:
		return 0

def  aks_sushupanding(n):
	flag = 0
	a = 2
	a1 = pow(a,n,n)
	a2 = pow(a,1,n)
	if a1 == a2:
		return 1
	else:
		return 0

def get_suijisushu():
	flag = 0
	while not flag:
		n = random.randrange(200,500)
		if (n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%13 == 0):
			continue
		flag = aks_sushupanding(n)
	return n

def benyuanyuan(p, euler_n):
	flag = 0
	tmp = 1
	j = 1
	while not flag:
		flag = 1
		g = random.randrange(2,euler_n)
		while j <= euler_n:
			j = j + 1
			tmp *= g
			tmp = tmp % p
			if tmp == 1:
				break
		if 	j == euler_n:
			break
	return g

def get_x(p):
	x = random.randrange(2,p)
	return x

def get_y(g,x,p):
	y = pow(g,x,p)
	return y

def sign_ver(x,y,g,p):
	k = get_suijisushu()
	a = pow(g,k,p)
	t = []
	t = input('请输入需要签名的信息：')
	m = []
	for i in t:
		m.append(ord(i))
	s = 0
	for i in m:
		s = s + i
	q = s % (p - 1)
	b = 1
	while 1:
		if q == (x * a + k * b) % (p - 1):
			break
		else:
			b = b + 1
	if (y**a * a**b) % p == pow(g,s,p):
		print('验证通过')

def elgamal_jiami_jimi(x,y,g,p):
	m = input('输入明文加密： ')	
	k = get_suijisushu()
	a = pow(g,k,p)
	b = []
	for i in m:
		b.append (ord(i) * pow(y,k,p))
	print ('密文： ',(a,b))	
	c = []
	for i in b:
		c.append(i // pow(a,x,p))
	n = ''
	for i in c:
		n = n + chr(i)
	print ('明文： ',n)

def elgamal():
	p = get_suijisushu()
	euler_n = p - 1
	g = benyuanyuan(p, euler_n)
	x = get_x(p)
	y = get_y(g,x,p)
	print ('公钥：',y,g,p)
	print ('私钥：',x)
	sign_ver(x,y,g,p)
	elgamal_jiami_jimi(x,y,g,p)

if __name__=='__main__':
	elgamal()

