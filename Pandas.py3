##PANDAS (operaciones basicas carga y lectura dataframe) Usaremos un dataset con datos de flores de ejemplo
	#un dataframe se puede conseguir de dos maneras: desde internet (como csv) o con sklearn (como diccionario)

	import pandas as pd #alias de facto que usa toda la comunidad
	from sklearn import datasets

	#LEER UN CSV ya descargado
	# pd.read_csv ("C:\Users\Sergio\Desktop\archivo.csv", delimiter="\t", header=None) #si no ponemos header=None asumira por defecto que la primera row son el nombre de las columnas


	#LEER CSV desde internet
	iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

	#ir viendo las siguientes líneas una por una y comentar el resto
	iris #asi podemos ver el csv
	type(iris) #pandas.core.frame.DataFrame
	iris.describe() #estadisticas del contenido
	iris.groupby("species").describe()#estadísticas basadas en una de las columnas (el csv habla de 3 especies diferentes, asi las separamos)
	iris.mean() #calculas medias de cada columna
	iris['sepal_length'].median() #media de una columna en concreto
	iris.sepal_length #lista los valores de esta columna uno por uno

	# iris2 = datasets.load_iris()
	# iris2 #mismo contenido en 'modo dataset' que es un diccionario


##DATAFRAME INDEXING (filtrar datos del dataframe)
	# [] para un indice de row
	# : rango de rows o columnas
	# df.iloc[,] 

	iris[1:3] #mostrara columna segunda y tercera
	iris[0:5]['sepal_length'] #mostrara el valor de esta columna en concreto en 5 filas

	iris.iloc[0:4,0:2] #con iloc el primer parametro son las filas y el segundo las columnas
	iris.iloc[:4,:2] #equivalente a la anterior (se omiten los 0)

	iris[iris.petal_length > 5] #filtrar por  una condición

	iris.loc[iris['petal_length'] == 4.3] #localiza filas con este valor en esta columna
	iris.loc[iris['petal_length'].isin([4.3,5.2])] #localiza filas con estos valores en esta columna
	iris.loc[~iris['petal_length'].isin([4.3,5.2])] #con virgulilla localizamos las que NO cumplan la condición


##OTHER IMPORTANT LOGIC (modificar datos, remplazar datos, categorizar información)
	#ejemplo1
	for row, value in iris.iterrows():
	    if sum(value[:2]) > 5: #suma el valor de la columna 0 a la tercera
	        iris.iloc[row,4] = "NUEVO" #si cumple esa condicion cambiamos la columna5
	iris #para ver el resultado
	        
	#ejemplo2
	iris.replace("NUEVO", "XXX")
	iris #para ver el resultado

	#ejemplo3, es normal separar la info en variables segun interese
	x = iris[["sepal_length", "petal_width"]]
	y = iris["species"]
	x

	#ejemplo4
	iris.head() #que enseñe solo las primeras rows
	iris.dtypes #mostrar el tipo de datos de cada columna. Dira objeto si no sabe lo que es por ejemplo cadenas de texto

	#ejemplo5: convertir un campo de texto en categoria (porque el numero de posibles valores es limitado)
	iris["species"] = iris["species"].astype('category') #cambiamos de objeto a categoria. Le decimos que no hay muchos datos diferentes en esa columna y que nos lo convierta en categoria
	iris["species"].cat.codes #muestra los códigos de esa columna, cada numero se corresponde con una categoria. Una specie en este caso

##PROBLEMA
	from sklearn import datasets
	dicc = datasets.load_iris()

	# dicc # el diccionario entero

	data=dicc['data']
	# data #solo la columna 'data' que es la que nos interesa

	columnas=dicc['feature_names'] #el feature_names es una lista dentro del diccionario dicc con 4 miembros

	#construimos el dataframe https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
	dataframe = pd.DataFrame(data, col=columnas)
	dataframe['species'] = dicc['target']
	dataframe

  # dicc.keys() #devuelve todas las llaves: dict_keys(['key1', 'key2'])
  # dicc.values() #devuelve todos los valores
