#가상의 이메일 전송 함수
def send_mail(from_mail, to_mail, subject,contents):
	print("from: \t" + from_mail)
	print("To : \t" + from_mail)
	print("subject : "+subject)
	print("*"*20)
	print(contents)
	print("*"*20)
	print("*"*20)
my_email = "skyjjw79@hanmail.net"

users.append({'name':'Boo','email':'jwjw232358@gmail.com'})
users.append({'name':'John','email':'jwjw5858@naver.com'})
'''
			user0				user1
	  ---------------------|-------------------
name		Boo					John
email jwjw232358@gmail.com	jwjw5858@naver.com
'''
contents = '''this is DSM
my leader is Eo young bo young
i love you
'''
for user in users:
	title = 'Dear.' + user['name']
	send_mail(my_email,user['email'], title, contents)