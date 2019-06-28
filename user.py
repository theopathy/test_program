import hashlib, uuid
PASSWORD_HASHED = 0
PASSWORD_UNHASHED = 1




def debugPrint(a):
	if (User.debug):
		print(a)
	
class User (object):
	count = 0 
	debug = True # SET THIS TO TRUE TO SEE OUTPUTS ON EACH ACTION
	Users = {}
	@property
	def name(self):
		return self.firstName + " " + self.lastName
	@property
	def Name(self):
		return self.firstName + " " + self.lastName
	def __init__(self, username, password = "Password", firstName="",lastName="",dob="",permissions=0,bool_SetValues=False):
		username=username.lower()
		if (( username in User.Users)): 
			debugPrint("already exists refering to user")
		else:
			debugPrint("Created user: "+username)
			User.count = User.count + 1
			self._username = username.lower()
			self.dob = dob
			self.salt = uuid.uuid4().hex
			self._password = hashlib.sha512(password.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()
			self.firstName = firstName
			self.lastName = lastName
			self.permissions = permissions
		User.Users[username] = self

		
	@property
	def username(self):
		return self._username.lower()
	@username.setter
	def username(self, value):
		del User.Users[self._username] 
		print("Username went from: '"  + self._username + "' to: '"+value+"'")
		self._username=value.lower()
		User.Users[self._username.lower()] = self
	@property
	def password(self):
		debugPrint("You can not get the password for security reasons")
		return ""
	@password.setter
	def password(self, value):
		self.salt = uuid.uuid4().hex
		self._password = hashlib.sha512(value.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()
	def authPassword(self,password,method=1): 
		debugPrint((hashlib.sha512(password.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()))
		return  (((hashlib.sha512(password.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()), password)[method==1])  == self._password
	def __del__ (self):

		User.count = User.count - 1


def Users(x = ""):
	if (x != ""):
		if (x.lower() in User.Users):
			return User.Users[x.lower()]	
		else:
			return 0
	else:
		return User.Users		
