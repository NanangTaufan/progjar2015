#clienttugas2.py
#Nanang Taufan Budiansyah
#5113100183

#inisiasi socket dan string
import sys
import socket
import select
import time
import string

def chat_client():
	host = 'localhost'

	#print out port dan inputan port
	sys.stdout.write('Port : ')
	port = int(sys.stdin.readline())

	# membuat socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# menghubungkan ke server
	try :
		s.connect((host, port))
	except :
		print 'Gagal'
		sys.exit()

	print 'Client sudah terhubung'
	sys.stdout.write('Pesan: '); sys.stdout.flush()

	while 1:
		socket_list = [sys.stdin, s]

		# mendapatkan socket list yang terdaftar
		ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
		for sock in ready_to_read:
			if sock == s:
				# menunggu jawaban dari server apakah sudah terhubung dengan server atau belum
				data = sock.recv(2048)
				if not data :
					print '\nAnda tidak terhubung'
					sys.exit()
				else :
					#print data uang diterima
					sys.stdout.write(data)
					sys.stdout.write('Pesan: '); sys.stdout.flush()
			else :
				# user menuliskan pesannya
				msg = []
				temp = sys.stdin.readline()
				temp1 = string.split(temp[:-1]) #dimulai dari index ke 0
				
				# menghitung jumlah inputan
				kata=len(temp1)
				#jika inputan index ke 0 adalah login
				if temp1[0]=="login" :
					if kata<2:
						print('Masukkan username untuk login')
					elif kata>2:
						print('Username hanya satu kata saja')
					else:
						s.send(temp)
				#jika index ke 0 adalah send
				elif temp1[0]=="send" :
					if kata<3:
						print('Perintah salah, tentukan user tujuan dan isikan pesan anda setelahnya')
					else:
						s.send(temp)
				#jika index ke 0 adalah sendall/broadcast
				elif temp1[0]=="sendall" :
					if kata<2:
						print("Perintah salah")
					else:
						s.send(temp)
				#untuk menampilkan list user yang aktif saat itu
				elif temp1[0]=="list" :
					if kata>1:
						print('Perintah salah')
					else:
						s.send(temp)
				#jika perintah diluar 4 yang diatas maka perintah dinyatakan salah
				else:
					print ('Perintah salah')
					
				sys.stdout.write('Pesan: '); sys.stdout.flush()
chat_client()
