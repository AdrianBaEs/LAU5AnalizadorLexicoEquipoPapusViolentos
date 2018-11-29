
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc
tokens = ('IDENTIFICADOR','NUMERO','ASIGNACION','IGUALACION','PLUS',
          'MINUS','DIVISION','DIVINVERSO','MULTIPLICACION','MENORQUE','MAYORQUE',
          'MENORIGUALQUE','MAYORIGUALQUE','COMPARACION',
          'DIFERENTE','PARENTESISDER','PARENTESISIZQ','PUNTO','COMA','PUNTOCOMA','DOSPUNTOS',
          'COMILLASIMPLEDER','COMILLASIMPLEIZQ','COMILLADOBLEDER','COMILLADOBLEDER')

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

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
# Parsing rules

precedence = (
    ('t_numero','t_asignacion','t_plus','t_minus','t_division','t_divinverso','t_multiplicacion','t_menorque','t_mayorque'),
    ('t_menorIgualQue','t_mayorIgualQue','t_comparacion','t_diferente','t_parentesisDer','t_parentesisIzq','t_punto','t_coma'),
    ('t_puntoComa','t_dosPuntos','t_comillaSimpleDer','t_comillaSimpleIzq','t_comillaDobleDer','t_comillaDobleIzq','t_comentarios'),
    )

# dictionary of names
"""names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0
        """
archivo = open("prueba1.pl0", "r")
for linea in archivo.readlines():
        print (linea)
splitValues = linea.split(" ")
def p_error(t):
    print("Syntax error at '%s'" % t.value)
while True:
    try: linea   # Use raw_input on Python 2
    except EOFError:
        break
archivo.close()    