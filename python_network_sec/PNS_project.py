import hashlib
  

def project1(str2hash):
	print("\nProject 1: md5 hash")
	result = hashlib.md5(str2hash.encode())
	print("md5 hash = ", result)
	print("md5's hexadecimal equivalent: ", result.hexdigest())


def project2(str2hash):
	print("\nProject 2: hashes using any 3 algorithms from hashlib Library")
	result = hashlib.sha256(str2hash.encode())
	print("1. SHA256:\n\tSHA256 hash = ", result)
	print("\tSHA256's hexadecimal equivalent: ", result.hexdigest())
	result = hashlib.sha1(str2hash.encode())
	print("2. SHA1\n\tSHA1 hash = ", result)
	print("\tSHA1's hexadecimal equivalent: ", result.hexdigest())
	result = hashlib.blake2b(str2hash.encode())
	print("3. BLAKE2b\n\tBLAKE2b hash = ", result)
	print("\tBLAKE2b's hexadecimal equivalent: ", result.hexdigest())


def project3(str2hash, salt, itr=5):
	print("\nAdding salts and iterations to hashes")
	print("\tSalt added: ", salt)
	print("\tIterations: ", itr)
	print("\tHashing algo: md5")
	str2hash += salt
	print("\tSalted string = " + str2hash)

	for i in range(1, itr+1):
		str2hash = hashlib.md5(str2hash.encode()).hexdigest()
		print("\t	Iteration " + str(i) + ":" + str2hash)


if __name__ == "__main__":
	print("TESTING... Will conduct a test before asking for input.\n")
	s = "ShGanesh"
	print("TEST String = ", s)
	project1(s)
	project2(s)
	project3(s, "<ye_namak_hataa_dena>", 5)

	print("\n\nTESTING DONE. NOW you can use your own input if you want.")
	
	s = input()
	print("String = ", s)
	project1(s)
	project2(s)
	project3(s, "<ye_namak_hataa_dena>", 5)
