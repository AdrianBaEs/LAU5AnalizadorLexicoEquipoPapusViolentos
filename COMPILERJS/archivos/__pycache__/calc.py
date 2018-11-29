
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------
import ply.lex as lex
import ply.lex as lex
import ply.yacc as yacc
tokens = ['IDENTIFICADOR','NUMERO','ASIGNACION','IGUALACION','PLUS',
          'MINUS','DIVISION','DIVINVERSO','MULTIPLICACION','MENORQUE','MAYORQUE',
          'MENORIGUALQUE','MAYORIGUALQUE','COMPARACION',
          'DIFERENTE','PARENTESISDER','PARENTESISIZQ','PUNTO','COMA','PUNTOCOMA','DOSPUNTOS',
          'COMILLASIMPLEDER','COMILLASIMPLEIZQ','COMILLADOBLEDER','COMILLADOBLEDER']

"""Definiendo palabras reservadas de JavaScript..."""
preservadas = {
    'case':'CASE','catch':'CATCH','const':'CONST','continue':'CONTINUE','break':'BREAK','delete':'DELETE',
    'debugger':'DEBUGGER','do':'DO','else':'ELSE','finally':'FINALLY','for':'FOR','funtion':'FUNTION','if':'IF',
    'in':'IN','instanceof':'INSTANCEOF','let':'LET','new':'NEW','return':'RETURN','switch':'SWITCH','this':'THIS',
    'throw':'THROW','try':'TRY','typeof':'TYPEOF','var':'VAR','void':'VOID','while':'WHILE','con':'CON','document':'script',
}
# Tokens

t_numero = r'\d'
t_asignacion = r'='
t_plus = r'\+'
t_minus = r'\-'
t_division = r'/'
t_divinverso = r'\\'
t_multiplicacion = r'\*'
t_menorque = r'<'
t_mayorque = r'>'
t_menorIgualQue = r'<='
t_mayorIgualQue = r'>='
t_comparacion = r'=='
t_diferente = r'!='
t_parentesisDer = r'\)'
t_parentesisIzq = r'\('
t_punto = r'\.'
t_coma = r','
t_puntoComa = r';'
t_dosPuntos = r':'
t_comillaSimpleDer = r'\''
t_comillaSimpleIzq = r'\''
t_comillaDobleDer = r'\"'
t_comillaDobleIzq = r'\"'
t_comentarios = r'//'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in keywords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_COMENTARIO(t):
    r'//.*'
    pass

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ERROR(t):
    print ("Expresion(es) ilegales para el lenguaje: '%s'"%t.value[0])
    t.lexer.sikip(1)

def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    
    for file in files:
        print (str(cont)+". "+file)
        cont = cont+1
    
    while respuesta == False:
        numArchivo = raw_input('\nNúmero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
            break
    print ("Has elegido el archivo \"%s\" \n" %files[int(numArchivo)-1])
    return files[int(numArchivo)-1]

    directorio = '/Users/Adrian/Documentos/ProyectoAnalizadorLex/'
    archivo = buscarFichero(directorio)
    test = directorio+archivo
    fp = codecs.open(test,"r","utf-8")
    cadena = fp.read()
    fp.close()
    analizador.input(cadena)
    while True:
        tok = analizador.token()
        if not tok : break
    print (tok)