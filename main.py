stos = []
stale = ['a', 'b', 'c', 'd','e']
funk = ['f','g','h','i','j','k','l','m','n']
pred = ['p','q','r','s','t','u','w','y','z','x','v']
zmien = ['A', 'B', 'C', 'D', 'E','F','G,','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','X']
neg = ['¬', '~', "NOT"]
kon = ["AND", '∧', '&']
alt = ["OR", '∨', '|']
imp = ["IMPLIES",'→']
row = ["IFF", '↔']
xor = ["XOR", '⊕']
ogl = ["FORALL", '∀']
egz = ["EXISTS", '∃']
while(1):
	try:
		form = input().split(" ")
		kt = -1
		for i in form:
			if i in stale or i in zmien:
				stos.append(i)
				kt += 1
			elif i[0] in funk or i[0] in pred:
				ile = int(i[2])
				i = i[0]
				i += "("
				while ile:
					ile -= 1
					i += stos[len(stos)-1-ile]
					stos.pop(len(stos)-1-ile)
					kt -= 1
					if ile > 0:
						i += ", "
					else:
						i += ")"
				stos.append(i)
				kt += 1
			elif i in neg:
				i = "(" + i + " "
				i += stos[len(stos)-1]
				i += ")"
				stos.pop()
				stos.append(i)
			elif i in ogl or i in egz:
				elem = None
				for j in range(kt, -1, -1):
					if stos[j] in zmien:
						elem = stos[j]
						stos.pop(j)
						kt -= 1
						break
				stos.append("(" + i + " " + elem + " " + stos[kt]+")")
				stos.pop(kt)
				del elem
				kt += 1
				kt -= 1
			else:
				a = stos[len(stos)-1]
				stos.pop()
				b = stos[len(stos)-1]
				stos.pop()
				kt -= 2
				stos.append("(" + b + " " + i + " " + a + ")")
				kt += 1
		print(stos[0])
		stos = []
	except EOFError:
		break