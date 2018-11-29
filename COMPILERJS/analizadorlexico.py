# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*- 
# -----------------------------------------------------------------------------
#
#
# Analizador léxico de JAVASCRIPT
# -----------------------------------------------------------------------------

# importa el primer módulo del ply
import ply.lex as lex
import re
import codecs
import os
import sys


# 1. Definición de tokens
tokens = [
    'MAYORIGUAL','MENORIGUAL','MENORQUE','MAYORQUE',
    'ILOGICO','OLOGICO','IGUALIGUAL','DIFERENTE',
    'LKEY','RKEY','LPAR','RPAR','LCOR','RCOR',
    'NEGBOOL','UMINUS','MEN','SUM','MULT','DIV','MOD','IGUAL','DOT', 'COMMA', 'DOTCOMMA',
    'RESERVADAS','CAD','IDENTIFICADOR','NUMERO','ASIGNACION','IGUALACION','PLUS',
    'MINUS','DIVISION','DIVINVERSO','MULTIPLICACION',
    'MENORIGUALQUE','MAYORIGUALQUE','COMPARACION',
    'PARENTESISDER','PARENTESISIZQ','PUNTO','COMA','PUNTOCOMA','DOSPUNTOS',
    'COMILLASIMPLEDER','COMILLASIMPLEIZQ','COMILLADOBLEDER','COMSIMDER','COMSIMIZQ','COMDOBDER','COMDOIZQ','COMENTARIO', 'COMMIT',
    'INTEGER','DOUBLE', 'APERFIN', 'APERINI', 'VAR' #, 'BOOLEANF', 'BOOLEANT'
    ]

#tokens_unused = ['BINARIO', 'NEWLINE', 'COMENTARIO']
#reservadas_unused = {'void':'VOID'}

#las palabras reservadas se reconocen sin necesidad de formar una expresion regular
reservadas = {
	'return':'RETURN',
	'this':'THIS',
	'extends':'EXTENDS',
	'if':'IF',
	'new':'NEW',
	'else':'ELSE',
	'length':'LENGTH',
	'int':'INT',
	'while':'WHILE',
	'true':'TRUE',
	'boolean':'BOOLEAN',
	'break':'BREAK',
	'false':'FALSE',
	'string':'STRING',
	'continue':'CONTINUE',
	'null':'NULL',
	'case':'CASE',
	'catch':'CATCH',
	'const':'CONST',
	'continue':'CONTINUE',
	'break':'BREAK',
	'delete':'DELETE',
    'debugger':'DEBUGGER',
    'do':'DO',
    'else':'ELSE',
    'finally':'FINALLY',
    'for':'FOR',
    'funtion':'FUNTION',
    'if':'IF',
    'in':'IN',
    'instanceof':'INSTANCEOF',
    'let':'LET','new':'NEW',
    'return':'RETURN',
    'switch':'SWITCH',
    'this':'THIS',
    'throw':'THROW',
    'try':'TRY',
    'typeof':'TYPEOF',
    'var':'VAR',
    'void':'VOID',
    'while':'WHILE',
    'con':'CON',
    'script':'SCRIPT',
}
tokens = tokens + list(reservadas.values())

# 2. Implementación con cadenas como Expresiones Regulares
#t_COMENTARIO = '\/\/.*'
#t_COMENTARIO = r'\/\*.*\n\*\/'
#t_COMENTARIOALT = r'\/\*\s*([^\s]*)\s*\s*\/'
t_APERFIN=r'</?\w+[>]'
t_APERINI=r'[<]+[\w]+[>]'
t_MAYORIGUAL='>='
t_MENORIGUAL='<='
t_MENORQUE = '<'
t_MAYORQUE = '>'
t_ILOGICO='&&'
t_OLOGICO=r'\|\|'
t_IGUALIGUAL=r'=='
t_DIFERENTE='!='
t_LKEY = '\{'
t_RKEY = '\}'
t_LPAR = '\('
t_RPAR = '\)'
t_LCOR = '\['
t_RCOR = r'\]'
t_NEGBOOL = '!'
t_MEN = '-'
t_UMINUS = '\-'
t_SUM = '\+'
t_MULT = '\*'
t_DIV = r'/'
t_MOD  = '%'
t_IGUAL = '='
t_DOT = r'\.'
t_COMMA = ','
t_DOTCOMMA = ';'
t_DOSPUNTOS = r':'
t_COMSIMDER = r'\''
t_COMSIMIZQ = r'\''
t_COMDOBDER = r'\"'
t_COMDOIZQ = r'\"'
t_ignore_COMENTARIO = '\/\/.*'
#t_VAR= r'[var( )[a-zA-Z_]+'
t_DOUBLE= r'[.,]?\d+'
#t_BOOLEANF = r'false'
#t_BOOLEANT= r'true'

# 2. Implementación de tokens con funciones en donde se implementa
#    la expresión regular

#ID---------------------------------------------------
#detecta que es un identificador y que no lo es
#un identificador no puede empezar por ñ
#un identificador puede reconocer vocales tildadas
#un identificador puede contener letras incluida la ñ y numeros en el area intermedia
#un identificador debe terminar en letras
#las letras ñ y las vocales tildadas se reemplazan por guin bajo
def t_RESERVADAS(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t    

def t_COMENTARIO(t):

	r'(/\*(.|\n|\r|\t)*?\*/)|//.*'
	#t.value = str(t.value)
	return t
def t_COMMIT(t):
	r'(<!--)[a-zA-Z_]*( )*[\w]*'
	return t
#BINARIO-----------------------------------------------
#def t_BINARIO(t):
#	r'[b]\'[01]+\''
#	t.value = int(t.value[2:-1],2)
	#t.value = str(t.value)
#	return t

#-----------------------------------------------------------------
#def t_error_CAD(t):
#    r'"([\x20-\x7E]|\\\\|\\n|\\t|\\r)*'
#    print"la cadena no quedo bien cerrada"


def t_COMILLADOBLEDER(t):

	r'"([\x20-\x7E]|\t|\r)*"'
	t.value = str(t.value)
	return t
def t_COMILLASIMPLEDER(t):

	r"'([\x20-\x7E]|\t|\r)*'"
	t.value = str(t.value)
	return t
	
def t_ERROR(t):
   	print "Expresion(es) ilegales para el lenguaje: '%s'"%t.value[0]
   	t.lexer.skip(1)
   	return t
   	#t.value = re.sub(r'[a-zA-Z_][a-zA-Z0-9_]*','_',t.value)
	#t.type = reservadas.get(t.value,'RESERVADAS')
	
#ERROR ID ---------------------------------------------
#def t_error_RESERVADAS(t):
#	r'[ñÑáÁéÉíÍÓóúÚ\d][A-Za-z]([0-9a-zA-ZñÑáÁéÉíÍÓóúÚ]*[A-Za-z])?'
#	t.value = re.sub(r'[ñÑáÁéÉíÍÓóúÚ]','_',t.value)
#	print"El identidicador %s no es valido" %t.value
#	t.type = reservadas.get(t.value,'RESERVADAS')
#	t.lexer.skip(1)
#	t.value = str(t.value)

#ID---------------------------------------------------
#def t_ID(t): #done
#	r'[A-Za-z]'
	
	#reemplazando la ñ y los caracteres tildados 
#	t.value = re.sub(r'[ñÑáÁéÉíÍÓóúÚ]','_',t.value)
#	t.type = reservadas.get(t.value,'RESERVADAS')
#	t.value = str(t.value)
#	return t

#NUMERO-----------------------------------------------
#reconoce los token como caracteres y la convertimos a un numero para escribirlo, si no es un numero tira una exepcion
def t_NUMEROALT(t):

	r'(-?[0-9]+(\.[0-9]+)?)([eE]-?\+?[0-9]+)?'

	try:
		t.value = float(t.value) #coge la cadena y se convierte en numero
		if t.value < -2147483648.0 or t.value > 2147483647.0:
			print "ERROR valor fuera de rango en la linea %d" %t.lineno
			t.value = 0

	except ValueError:
		print "El valor no es correcto %d", t.value
		t.value = 0
	#t.value = str(t.value)
	return t

#RETURN-----------------------------------------------
#detecta la palabra reservada return
#NOTA: no hay necesidad de realizar esta funcion, puesto que esta dentro de las palabras reservadas
#def t_RETURN(t):
#    r'return'
#    t.value = str(t.value)
#    return t
#IF---------------------------------------------------
#def t_IF(t):
#    r'if'
#    return t


# 3. Caracteres que se reconocen e ignoran
t_ignore = " \t" #aca se esta ignorando el espacio

#NEWLINE----------------------------------------------
#reconoce un salto de linea y cuenta los saltos de linea para saber cuantas lineas hay
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    t.value = str(t.value)
    
#ERROR------------------------------------------------
#entra aca si no concuerda con ningun caracter, es decir si no reconoce un token
def t_error(t): 
    #print(" No se reconoce el caracter '%s'" % t.value[0])
    t.lexer.skip(1) #salta para que el analizador siga reconociendo mas
    t.value = str(t.value)

    
#buscarFicheros---------------------------------------
def buscarFicheros(directoriomio):
 	ficheros = []
 	numArchivo = ''
 	respuesta = False
 	cont = 1

 	for base, dirs, files in os.walk(directorio):
 		ficheros.append(files)
	
 	for file in files:
 		print str(cont)+". "+file
 		cont = cont+1

 	while respuesta == False:
 		numArchivo = raw_input('\nNumero del Test: ')
 		for file in files:
 			if file == files[int(numArchivo)-1]:
 				respuesta = True
 				break

 	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]
	return files[int(numArchivo)-1]
	

#END FUNCTIONS-------------------------------------------------------
#5. Construye el analizador
analizador=lex.lex() #coge todos los automatas y los junta en uno sol


print "\nBienvenido al Analizador Lexico."
print "Por favor, elige la prueba"
print "Presiona Ctrl+z para salir\n"


directorio = "C:/Users/carl-/OneDrive/Escritorio/COMPILERJS/test/"
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
cadena = str(cadena)
fp.close()


analizador.input(cadena)

# Muestra la lista de tokens
while True:
     tok = analizador.token()
     if not tok: break      #fin de la lista
     print tok



