#function to get initials of name.
def to_initials(name):
	li = name.split(" ")
	initials = ""
	for ele in li:
		initials += ele[0][0]
	return initials
	
#print(to_initials("Kelvin Bridges"))
#print(to_initials("Michaela Yamamoto"))
#print(to_initials("Mary La Grange"))

# finding the element that appears first in the array.
def first_in_array(arr, el1,el2):
	for ele in arr:
		if ele == el1:
			return el1
		if ele == el2:
			return el2
	return none
	
#print(first_in_array(["a", "b", "c", "d"], "d", "b"))
#print(first_in_array(["cat", "bird" ,"dog", "mouse" ], "dog", "mouse"))

#abbreviate sentence by removing the vowels if the length of the word is greater than 4.
def abbreviate_sentence (sent):
	list = sent.split(" ")
	vowels = ['a','e','i', 'o','u']
	result = []
	for ele in list:
		if len(ele) > 4:
			temp = []
			for i in range(len(ele)):
				if ele[i] not in vowels:
					temp.append(ele[i])
			fstr = "".join(temp)
			result.append(fstr)
		else:
			result.append(ele)
	final = ''
	final = " ".join(result)
	return final
	
#print(abbreviate_sentence("follow the yellow brick road"))
#print(abbreviate_sentence("what a wonderful life"))

def format_name(str):
	list = str.split(" ")
	final = []
	for ele in list:
		l_letter = []
		word = format_word(ele)
		final.append(word)
	ffinal = " ".join(final)
	return ffinal

def format_word(word):
	list = []
	for i in range(len(word)):
		list.append(word[i])
	list[0] = list[0].upper()
	for i in range(1,len(list)):
		list[i] = list[i].lower()
	final = "".join(list)
	return final

#print(format_word('musTAfa'))
#print(format_name("chase WILSON"))
#print(format_name("brian CrAwFoRd scoTT"))

def is_valid_name(str):
	cond1 = True
	cond2 = True
	list = str.split(" ")
	if len(list) < 2:
		cond1 = False
		return False
	for ele in list:
		if valid_word(ele) == False:
			cond2 = False
			return False
	if cond1 == True and cond2 == True:
		return True
	else:
		return False

def valid_word(word):
	bool = True
	list = []
	for i in range(len(word)):
		list.append(word[i])
	if list[0] != list[0].upper():
		return false
	for i in range(1,len(list)):
		if list[i] != list[i].lower():
			bool = False
			return False
	return bool

#print(is_valid_name("Kush Patel"))
#print(is_valid_name("Daniel"))
#print(is_valid_name("Robert Downey Jr"))
#print(is_valid_name("ROBERT DOWNEY JR"))

def is_valid_email(str):
	cond1 = True
	cond2 = True
	cond3 = True
	list = str.split('@')
	if len(list) != 2:
		cond1 = False
		return False
	bef_at = list[0]
	for l in bef_at:
		if l != l.lower():
			cond2 = False
			return False
		if l.isnumeric() == True:
			cond2 = False
			return False
	dots = 0
	aft_at = list[1]
	for c in aft_at:
		if c == ".":
			dots += 1
	if dots != 1:
		cond3 = False
		return False
	return True 
	
#print(is_valid_email("abc@xy.z"))         # => true
#print(is_valid_email("jdoe@gmail.com"))   # => true
#print(is_valid_email("jdoe@g@mail.com"))  # => false
#print(is_valid_email("jdoe42@gmail.com")) # => false
#print(is_valid_email("jdoegmail.com"))    # => false
#print(is_valid_email("az@email"))         # => false

def array_translate(array):
	final = ""
	for i in range(0, len(array), 2):
		final += array[i] * array[i+1]
	return final
	
#print(array_translate(["Cat", 2, "Dog", 3, "Mouse", 1]))
#print(array_translate(["red", 3, "blue", 1]))

def reverse_words(sent):
	final = []
	list = sent.split(" ")
	for ele in list:
		rword = reverse_word(ele)
		final.append(rword)
	ffinal = " ".join(final)
	return ffinal
	
def reverse_word(word):
	result = ""
	for i in range(len(word)-1, -1, -1):
		result += word[i]
	return result
	
#print(reverse_words("keep coding"))
#print(reverse_words("simplicity is  prerequisite for reliability"))

#rotating array method 1
def rotate_array(arr, num):
	for i in range(num):
		arr = rotate(arr)
	return arr

def rotate(arr):
	new_arr = []
	new_arr.append(arr[len(arr)-1])
	for i in range(len(arr)-1):
		new_arr.append(arr[i])
	arr = new_arr
	return arr
#print(rotate(["a", "b", "c", "d" ]))
#print(rotate_array([ "Matt", "Danny", "Mashu", "Matthias" ], 1))
#print(rotate_array([ "a", "b", "c", "d" ], 2))

#rotating array method 2
def rotate_array(arr, num):
	for i in range(num):
		arr = rotate(arr)
	return arr

def rotate(arr):
	new_arr = []
	new_arr.append(arr[len(arr)-1])
	new_arr = new_arr + arr[:len(arr)-1]
	arr = new_arr
	return arr
#print(rotate(["a", "b", "c", "d" ]))
#print(rotate_array([ "Matt", "Danny", "Mashu", "Matthias" ], 1))
#print(rotate_array([ "a", "b", "c", "d" ], 2))

def pig_latin_word(word):
	result = ""
	vowels = ['a','e','i','o','u']
	st = 'yay'
	if word[0] in vowels:
		result = word + st
		return result
	else:
		ind = 0
		for i in range(len(word)):
			if word[i] in vowels:
				ind = i 
				break
		result = word[i:len(word)]
		result += word[:i]
		result += 'ay'
	return result
	
#print(pig_latin_word("apple"))   # => "appleyay"
#print(pig_latin_word("eat"))     # => "eatyay"
#print(pig_latin_word("banana"))  # => "ananabay"
#print(pig_latin_word("trash"))   # => "ashtray"

def combinations(arr):
	result = []
	for i in range(len(arr)):
		for j in range(len(arr)):
			if j > i:
				result.append([arr[i],arr[j]])
	return result

#print(combinations(["a", "b", "c"]))
#print(combinations([0, 1, 2, 3]))

#find the number of pairs whos sum is equal to zero.
def opposite_count(nums):
	pairs = 0
	for i in range(len(nums)):
		for j in range(len(nums)):
			if j > i:
				if nums[i] + nums[j] == 0:
					pairs += 1
	return pairs

#print(opposite_count([ 2, 5, 11, -5, -2, 7 ]))
#print(opposite_count([ 21, -23, 24 -12, 23 ]))

def two_d_sum(arr):
	sum = 0
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			sum += arr[i][j]
	return sum

array_1 = [
  [4, 5],
  [1, 3, 7, 1]
]
array_2 = [
  [3, 3],
  [2],
  [2, 5]
]
#print(two_d_sum(array_1))
#print(two_d_sum(array_2))

def two_d_translate(arr):
	result = []
	for i in range(len(arr)):
		for j in range(arr[i][1]):
			result.append(arr[i][0])
	return result
	
arr_1 = [
  ['boot', 3],
  ['camp', 2],
  ['program', 0]
]

arr_2 = [
  ['red', 1],
  ['blue', 4]
]
#print(two_d_translate(arr_1))
#print(two_d_translate(arr_2))

def get_double_age(hash):
	for k in hash:
		if k == "age":
			return hash[k] * 2

#print(get_double_age({"name":"App Academy", "age":5}))
#print(get_double_age({"name":"Ruby", "age":23}))

def get_full_name(hash):
	str = ""
	str += hash['first'] + " "
	str += hash['last']
	str += ", "
	str += hash['title']
	return str

hash1 = {"first":"Michael", "last":"Jordan", "title": "GOAT"}
#print(get_full_name(hash1)) # => "Michael Jordan, the GOAT"
hash2 = {"first":"Fido", "last":"McDog", "title": "Loyal"}
#print(get_full_name(hash2)) #

def word_lengths(sentence):
	hash = {}
	words = sentence.split(" ")
	for word in words:
		hash[word] = len(word)
	return hash

#print(word_lengths("this is fun")) #=> {"this"=>4, "is"=>2, "fun"=>3}
#print(word_lengths("When in doubt, leave it out")) #=> {"When"=>4, "in"=>2, "doubt,"=>6, "leave"=>5, "it"=>2, "out"=>3}

def retrieve_values(hash1, hash2, key):
	result = []
	for k in hash1:
		if k == key:
			result.append(hash1[k])
	for k in hash2:
		if k == key:
			result.append(hash2[k])
	return result

dog1 = {"name":"Fido", "color":"brown"}
dog2 = {"name":"Spot", "color":"white"}

#print(retrieve_values(dog1, dog2, "name"))
#print(retrieve_values(dog1, dog2, "color"))

def cat_builder(name_str, color_str, age_num):
	d = {}
	d['name'] = name_str
	d['color'] = color_str
	d['age'] = age_num
	return d

#print(cat_builder("Whiskers", "orange", 3))
#print(cat_builder("Salem", "black", 100))

def ae_count(str):
	a = 0
	e = 0
	d = {}
	for l in str:
		if l == 'a':
			a += 1
		if l == 'e':
			e += 1
	d["a"] = a
	d["e"] = e
	return d
	
#print(ae_count("everyone can program"))
#print(ae_count("keyboard"))

def element_count(arr):
	hash = {}
	for ele in arr:
		c = 0
		for val in arr:
			if ele == val:
				c += 1
		if ele not in hash:
			hash[ele] = c
	return hash
	
#print(element_count(["a", "b", "a", "a", "b"]))
#print(element_count(["red", "red", "blue", "green"]))

def select_upcase_keys(hash):
	d = {}
	for key in hash:
		if key == key.upper():
			d[key] = hash[key]
	return d
	
#print(select_upcase_keys({"make":"Tesla", "MODEL":"S", "Year": 2018, "SEATS": 4}))
#print(select_upcase_keys({"DATE":"July 4th","holiday": "Independence Day", "type":"Federal"}))

def hand_score(hand):
	score = 0
	hash = {"A":4,"K":3,"Q":2,"J":1}
	for c in hand:
		score += hash[c.upper()]
	return score

#print(hand_score("AQAJ"))
#print(hand_score("jJka"))

def frequent_letters(string):
	result = []
	hash = {}
	for l in string:
		n = 0
		for c in string:
			if c == l:
				n += 1
		if l not in hash:
			hash[l] = n
	for k,i in hash.items():
		if i > 2:
			result.append(k)
	return result
	
#print(frequent_letters('mississippi'))
#print(frequent_letters('bootcamp'))

def hash_to_pairs(hash):
	result = []
	for k,i in hash.items():
		result.append([k,i])
	return result
	
#print(hash_to_pairs({"name":"skateboard", "wheels":4, "weight":"7.5 lbs"}))
#print(hash_to_pairs({"kingdom":"animalia", "genus":"canis", "breed":"German Shepherd"}))

def unique_elements(arr):
	result = []
	hash = {}
	for l in arr:
		if l not in hash:
			n = 0
			for c in arr:
				if c == l:
					n += 1
			hash[l] = n
	for k,v in hash.items():
		result.append(k)
	return result

#print(unique_elements(['a', 'b', 'a', 'a', 'b', 'c']))

def element_replace(arr, hash):
	for i in range(len(arr)):
		if  arr[i] in hash:
			arr[i] = hash[arr[i]]
	return arr

arr1 = ["LeBron James", "Lionel Messi", "Serena Williams"]
hash1 = {"Serena Williams":"tennis", "LeBron James":"basketball"}
#print(element_replace(arr1, hash1))

arr2 = ["dog", "cat", "mouse"]
hash2 = {"dog":"bork", "cat":"meow", "duck":"quack"}
#print(element_replace(arr2, hash2))


def map_by_name(arr):
	result = []
	for hash in arr:
		result.append(hash["name"])
	return result
	
pets = [
  {"type":"dog", "name":"Rolo"},
  {"type":"cat", "name":"Sunny"},
  {"type":"rat", "name":"Saki"},
  {"type":"dog", "name":"Finn"},
  {"type":"cat", "name":"Buffy"}
]
#print(map_by_name(pets))

def isPrime(num):
	p = True
	if num < 2:
		return False
	for i in range(2,num):
		if num%i != 0:
			p = True
		else:
			p = False
			return p
	return p
	
def next_prime(num):
	f = False
	p = 0 
	while f == False:
		num += 1
		if isPrime(num) == True:
			p = num
			f = True
	return p

def rep_prime(xs):
	for i in range(len(xs)):
		if isPrime(xs[i]):
			x = next_prime(xs[i])
			xs[i] = x
	return xs

xs = [1,3,5,4,7]
#print(rep_prime(xs)) 


def map_by_key(arr, key):
	result = []
	for hash in arr:
		result.append(hash[key])
	return result
	
locations = [
  {"city":"New York City", "state":"New York", "coast":"East"},
  {"city":"San Francisco", "state":"California", "coast":"West"},
  {"city":"Portland", "state":"Oregon", "coast":"West"},
]
#print(map_by_key(locations, "state"))

def yell_sentence(sent):
	str = ""
	list = sent.split(" ")
	new = []
	for i in range(len(list)):
		temp = list[i].upper() + "!"
		new.append(temp)
	str = " ".join(new)
	return str

#print(yell_sentence("I have a bad feeling about this"))
#Have to use Hash.
def whisper_words(words):
	hash = {}
	li = []
	for i in range(len(words)):
		hash[words[i].lower()] = "..."
	for k,v in hash.items():
		li.append(k+v)
	return li

#print(whisper_words(["KEEP", "The", "NOISE", "down"]))

def o_words(sentence):
	list = []
	li = sentence.split(" ")
	for el in li:
		if "o" in el:
			list.append(el)
	return list

#print(o_words("How did you do that?"))
'''
def last_index(str, char):
	index = -1
	for i in range(len(str)):
		if str[i] == char:
			index = i
	return index
	'''
def last_index(str, char):
	index = -1
	for i in range(len(str) - 1, -1, -1):
		if str[i] == char:
			index = i
			break
	return index
#print(last_index("abca", "a"))
#print(last_index("mississipi", "i"))
#print(last_index("octagon", "o"))
#print(last_index("programming", "m"))

def most_vowels(sentence):
	vowels = ['a', 'e', 'i', 'o', 'u']
	list = sentence.split(" ")
	hash = {}
	for word in list:
		vow = 0
		for i in range(len(word)):
			if word[i] in vowels:
				vow += 1
		hash[word] = vow
	max = ""
	cou = 0
	for k,v in hash.items():
		if v > cou:
			cou = v
			max = k
	return max
#print(most_vowels("what a wonderful life"))

def prime(num):
	for i in range(2,num):
		if num%i == 0:
			return False
	return True

def pick_primes(numbers):
	list = []
	for num in numbers:
		if isPrime(num) == True:
			list.append(num)
	return list
	
#print(pick_primes([2, 3, 4, 5, 6]))
#print(pick_primes([101, 20, 103, 2017]))

def prime_factors(nums):
	prime_fac = []
	for i in range(2,nums):
		if prime(i) == True:
			if nums%i == 0:
				prime_fac.append(i)
	return prime_fac
#print(prime_factors(24))
#print(prime_factors(60))

def even(num):
	if num%2 == 0:
		return True
	return False

def greatest_factor_array(arr):
	for i in range(len(arr)):
		if even(arr[i]) == True:
			arr[i] = arr[i]//2
	return arr
	
#print(greatest_factor_array([16, 7, 9, 14]))
#print(greatest_factor_array([30, 3, 24, 21, 10]))

def perfect_square(num):
	bool = False
	for i in range(1,num//2):
		if i * i == num:
			bool = True
			return bool
	return bool

#print(perfect_square(5))
#print(perfect_square(12))
#print(perfect_square(30))
#print(perfect_square(9))
#print(perfect_square(25))
 
def triple_sequence(start, length):
	result = [start]
	i = 0
	while i < length-1:
		result.append(result[i] * 3)
		i += 1
	return result
#print(triple_sequence(2,4))
#print(triple_sequence(4,5))

def summation_sequence(start, length):
	result = []
	result.append(start)
	k = 0
	while k < length-1:
		ele = 0
		for i in range(result[-1] + 1):
			ele += i
		result.append(ele)
		k += 1
	return result
#print(summation_sequence(3, 4))
#print(summation_sequence(5, 3))

def fibonacci(length):
	if length == 0:
		return []
	if length == 1:
		return [1]
	if length == 2:
		return [1,1]
	result = [1,1]
	a = 1
	b = 1
	i = 0
	while i < length-2:
		result.append(result[i]+result[i+1])
		i += 1
	return result
#print(fibonacci(0))
#print(fibonacci(1))
#print(fibonacci(6))
#print(fibonacci(8))

def caesar_cipher(str, num):
	result = ""
	abc = "abcdefghijklmnopqrstuvwxyz"
	for i in range(len(str)):
		for j in range(len(abc)):
			if str[i] == abc[j]:
				if (j+num) >= len(abc):
					nind = (j+num) - 26
					result += abc[nind]
				else:
					result += abc[j+num]
	return result
#print(caesar_cipher("apple", 1))
#print(caesar_cipher("bootcamp", 2))
#print(caesar_cipher("zebra", 4))

def vowel_cipher(string):
	result = ""
	vowels = ['a','e','i','o','u']
	hash = {'a':'e', 'e':'i','i':'o','o':'u', 'u':'a'}
	for i in range(len(string)):
		if string[i] in vowels:
			result += hash[string[i]]
		else:
			result += string[i]
	return result
#print(vowel_cipher("bootcamp"))
#print(vowel_cipher("paper cup"))

def double_letter_count(string):
	counter = 0
	for i in range(len(string) - 1):
		l = string[i]
		if l == string[i+1]:
			counter += 1
	return counter
#print(double_letter_count("the jeep rolled down the hill"))
#print(double_letter_count("bootcamp"))

def adjacent_sum(arr):
	result = []
	for i in range(len(arr)-1):
		result.append(arr[i] + arr[i+1])
	return result
#print(adjacent_sum([3, 7, 2, 11]))
#print(adjacent_sum([2, 5, 1, 9, 2, 4]))
def uplevel(arr):
	r = []
	for i in range(len(arr)-1):
		r.append(arr[i] + arr[i+1])
	return r
def pyramid_sum(base):
	result = [base]
	i = 1
	while i < len(base):
		temp = uplevel(result[0])
		result.insert(0, temp)
		i += 1
	return result
#print(pyramid_sum([1, 4, 6]))
#print(pyramid_sum([3, 7, 2, 11]))

def all_else_equal(arr):
	s = sum(arr)
	for num in arr:
		if num == s/2:
			return num
	return None
#print(all_else_equal([2, 4, 3, 10, 1]))
#print(all_else_equal([6, 3, 5, -9, 1]))
#print(all_else_equal([1, 2, 3, 4])) 

def anagrams(word1, word2):
	if len(word1) != len(word2):
		return False
	hash1 ={}
	hash2 ={}
	for i in range(len(word1)):
		if word1[i] in hash1:
			hash1[word1[i]] = hash1[word1[i]] + 1
		else:
			hash1[word1[i]] = 1
	for i in range(len(word2)):
		if word2[i] in hash2:
			hash2[word2[i]] = hash2[word2[i]] + 1
		else:
			hash2[word2[i]] = 1
#	print(hash1)
#	print(hash2)
	for k,v in hash1.items():
		if k in hash2:
			if v != hash2[k]:
				return False
		else:
			return False
	return True

#print(anagrams("cat", "act"))
#print(anagrams("restful", "fluster"))
#print(anagrams("cat", "dog"))
#print(anagrams("boot", "bootcamp")) 

def consonant_cancel(str):
	result = ""
	vowels = ['a','e','i','o','u']
	list = str.split(" ")
	for word in list:
		for i in range(len(word)):
			if word[i] in vowels:
				result += word[i:]
				result += " "
				break
	return result

#print(consonant_cancel("down the rabbit hole"))
#print(consonant_cancel("writing code is challenging"))

def same_char_collapse(str):
	col = True
	s = str
	while col == True:
		for i in range(len(s)-1):
			t = str[i]
			if t != str[i+1]:
				col = False
			else:
				col = False
				s = ""
				s += s[:i] + s[:i+2]
				#print(s)
				break
	return s

def same_char_collapse(str):
	chars = list(str)
	print(chars)
	colapsing = True
	i = 0
	while i < (len(chars) - 1):
		print(chars[i], chars[i+1], i)
		if chars[i] == chars[i+1]:
			chars.pop(i)
			chars.pop(i)
			if i != 0:
				i -= 1
		else:
			i += 1
	return "".join(chars)

#print(same_char_collapse("zzzxaaxy"))
#print(same_char_collapse("uqrssrqvtt"))

def generate(num):
	triangle = [[1],[1,1]]
	row = []
	return 0
	
def t(n):
	tri = []
	for n in range(1, n+1):
		row = [1]
		for i in range(1,n-1):
			row.append(0)
		row.append(1)
		tri.append(row)
	return tri
def pas(n):
	tri = t(n)
	for i in range(len(tri)):
		for j in range(len(tri[i])):
			if tri[i][j] == 0:
				tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
	return tri
	
print(pas(4))