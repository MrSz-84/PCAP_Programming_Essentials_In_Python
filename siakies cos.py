def czy_przestepny(rok):
	if rok % 4 != 0:
		return False
	elif rok % 100 != 0:
		return True
	elif rok % 400 != 0:
		return False
	else:
		return True

def dni_w_miesiacu(rok, miesiac):
	if rok < 1582 or miesiac < 1 or miesiac > 12:
		return None
	dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	wyn = dni[miesiac - 1]
	if miesiac == 2 and czy_przestepny(rok):
		wyn = 29
	return wyn

def dzien_w_roku(rok, miesiac, dzien):
	dni = 0
	for m in range(1, miesiac):
		md = dni_w_miesiacu(rok, m)
		if md == None:
			return None
		dni += md
	md = dni_w_miesiacu(rok, miesiac)
	if dzien >= 1 and dzien <= md:
		return dni + dzien
	else:
		return None

print(dzien_w_roku(2000, 12, 31))