def bom_like_friend():
	id = str(input("   [?] Id Target: "))
	if wrong_id(id,p=True):
		print("   [+] Invalid Id")
		enter()
	limit = int(input("   [?] Limit (int): "))
	gas = Like()
	print("\n   [+] Spamming Like To: " + gas.get_name(id))
	gas.dump_sts("https://mbasic.facebook.com/profile.php?id="+id, "Suka", "Lihat Berita Lain", limit, "like.php")
	print("   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar()
	print("   [+] Done!")
	enter()

def bom_like_grup():
	id = str(input("   [?] Id Group: "))
	if wrong_id(id,g=True):
		print("   [+] Invalid Id")
		enter()
	limit = int(input("   [?] Limit (int): "))
	if limit > 1000 or limit <= 0:
		limit = 1000
	gas = Like()
	gas.dump_sts("https://mbasic.facebook.com/groups/"+id, "Suka", "Lihat Postingan Lainnya", limit, "like.php")
	print("\n   [+] Spamming Like To: " + gas.get_name(id))
	print("   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar()
	print("   [+] Done!")
	enter()
	
def bom_like_halaman():
	id = str(input("   [?] Username Fanspage: "))
	if wrong_id(id,f=True):
		print("   [+] Invalid Username")
		enter()
	limit = int(input("   [?] Limit (int): "))
	if limit > 1000 or limit <= 0:
		limit = 1000
	gas = Like()
	gas.dump_sts("https://mbasic.facebook.com/"+id, "Suka", "Tampilkan lainnya", limit, "like.php")
	print("\n   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar()
	print("   [+] Done!")
	enter()

def bom_like_home():
	limit = int(input("   [?] Limit (int): "))
	if limit > 1000 or limit <= 0:
		limit = 1000
	gas = Like()
	print("\n   [+] Spamming Like in Home ")
	gas.dump_sts("https://mbasic.facebook.com/", "Suka", "Lihat Berita Lain", limit, "like.php")
	print("   [+] Total: " + str(len(gas.id)))
	print("   [+] Process")
	gas.hajar()
	print("   [+] Done!")
	enter()
