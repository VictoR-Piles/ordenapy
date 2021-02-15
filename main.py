import os

sys_language = os.getenv('LANG')
# ***** LIST OF SUPPORTED PATH *****
if(sys_language == "es_ES.UTF-8"):
	path = os.environ['HOME'] + '/Descargas/'
	img_path = os.environ['HOME'] + '/Imágenes/'
	txt_path = os.environ['HOME'] + '/Documentos/texto/'
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

	if (extension == ".png" or extension == ".jpg" or extension == ".jpeg" or extension == ".webp" or extension == ".svg"):
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
	elif (extension == ".txt" or extension == ".odt" or extension == ".rtf" or extension == ".docx"):
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
