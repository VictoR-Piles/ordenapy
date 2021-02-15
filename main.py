import os

sys_language = os.getenv('LANG')
# ***** LIST OF SUPPORTED PATH *****
if(sys_language == "es_ES.UTF-8"):
	path = os.environ['HOME'] + '/Descargas/'
	img_path = os.environ['HOME'] + '/Imágenes/'
	audio_path = os.environ['HOME'] + '/Música/'
	video_path = os.environ['HOME'] + '/Vídeos/'
	txt_path = os.environ['HOME'] + '/Documentos/texto/'
	pdf_path = os.environ['HOME'] + '/Documentos/pdf/'
	comp_path = os.environ['HOME'] + '/Otros/Comprimidos/'
	font_path = os.environ['HOME'] + '/.fonts/'
	pkg_path = os.environ['HOME'] + '/Otros/Paquetes/'
	iso_path = os.environ['HOME'] + '/Documentos/iso/'
	tmp_path = os.environ['HOME'] + '/Plantillas/'
	other_path = os.environ['HOME'] + '/Otros/'
else:
	print("Este programa solo soporta lenguage es_ES.UTF-8")
	exit(1)

print("Ordenando para el directorio -> " + path)

content = os.listdir(path)

print("Contenido de " + path + ": ")
print(content)

for file in content:
	filename, extension = os.path.splitext(file)

	if (extension == ".png" or extension == ".jpg" or extension == ".jpeg" or extension == ".webp" or extension == ".svg" or extension == ".ico" or extension == ".gif"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + img_path)
		try:
			os.rename(path + file, img_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(img_path)
			os.rename(path + file, img_path + file)
		except:
			print("Ha ocurrido un error")
	elif (extension == ".mp3" or extension == ".aif" or extension == ".mid" or extension == ".midi" or extension == ".ogg" or extension == ".wav"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + audio_path)
		try:
			os.rename(path + file, audio_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(audio_path)
			os.rename(path + file, audio_path + file)
		except:
			print("Ha ocurrido un error")

	elif (extension == ".mp4" or extension == ".mkv" or extension == ".avi"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + video_path)
		try:
			os.rename(path + file, video_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(video_path)
			os.rename(path + file, video_path + file)
		except:
			print("Ha ocurrido un error")
	elif (extension == ".txt" or extension == ".odt" or extension == ".rtf" or extension == ".docx" or extension == ".xml"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + txt_path)
		try:
			os.rename(path + file, txt_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(txt_path)
			os.rename(path + file, txt_path + file)
		except:
			print("Ha ocurrido un error")
	elif (extension == ".pdf"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + pdf_path)
		try:
			os.rename(path + file, pdf_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(pdf_path)
			os.rename(path + file, pdf_path + file)
		except:
			print("Ha ocurrido un error")
	elif (extension == ".7z" or extension == ".rar" or extension == ".tar" or extension == ".zip"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + txt_path)
		try:
			os.rename(path + file, txt_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(txt_path)
			os.rename(path + file, txt_path + file)
		except:
			print("Ha ocurrido un error")
	elif (extension == ".fnt" or extension == ".fon" or extension == ".otf" or extension == ".ttf"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + font_path)
		try:
			os.rename(path + file, font_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(font_path)
			os.rename(path + file, font_path + file)
		except:
			print("Ha ocurrido un error")
	elif (extension == ".deb" or extension == ".rpm" or extension == ".pkg" or extension == ".tar.gz"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + pkg_path)
		try:
			os.rename(path + file, pkg_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(pkg_path)
			os.rename(path + file, pkg_path + file)
		except:
			print("Ha ocurrido un error")
	elif(extension == ".iso"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + iso_path)
		try:
			os.rename(path + file, iso_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(iso_path)
			os.rename(path + file, iso_path + file)
		except:
			print("Ha ocurrido un error")
	elif (extension == ".ott"):
		print(filename + " es un archivo " + extension)
		print("Moviendo a -> " + tmp_path)
		try:
			os.rename(path + file, tmp_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(tmp_path)
			os.rename(path + file, tmp_path + file)
		except:
			print("Ha ocurrido un error")
	else:
		print(filename + " es un archivo con formato desconocido")
		print("Moviendo a -> " + other_path)
		try:
			os.rename(path + file, other_path + file)
		except FileNotFoundError:
			# Crate the directory if not exists
			os.mkdir(other_path)
			os.rename(path + file, other_path + file)
		except:
			print("Ha ocurrido un error")
