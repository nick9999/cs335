#!/usr/bin/python
from ply import lex
#import debug as debug

#reserved words
reserved={
	'if' : 'IF',
	'else':'ELSE',
	'elsif':'ELSIF',
	'unless':'UNLESS',
	'switch':'SWITCH',
	'case':'CASE',
	'while':'WHILE',
	'until':'UNTIL',
	'for':'FOR',
	'foreach':'FOREACH',
	'do':'DO',
	'next':'NEXT',
	'last':'LAST',
	'continue':'CONTINUE'
}
# I am bored avikalp please complete the list

#some tokens we are gonna use 
tokens=[
		"STRING",
		"NUMBER",
		"PLUS_OP",
		"MINUS_OP",
		"MULTIPLACATION_OP",
		"DIVISION_OP",
		"MODULUS_OP",
		"NOT_OP",
		"AND_OP",
		"OR_OP",
		"NOT_EQUALS_OP",
		"EQUALS_OP",
		"GREATER_EQUAL_OP",
		"GREATER_OP"
		"LESS_EQUAL_OP",
		"LESS_OP",
		"ASSIGNMENT_OP",
		"SEMICOLON",
		"BLOCK_BEGIN",
		"BLOCK_ENDS",
		"OPEN_BRACKET",
		"CLOSE_BRACKET",
		"OPEN_PARANTHESIS",
		"CLOSE_PARANTHESIS",
		"COMMA",
		"SEMICOLON",
		"IDENTIFIER",
		"WHITEAPACE",
		"COMMENT"
		] + list(reserved.values())

t_ignore_WHITESPACE=r"\s"


def t_STRING(t):
	r"(?P<start>\"|')[^\"']*(?P=start)"
	t.value=t.value.replace("\"","").replace("'","")
	return t
	
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_PLUS_OP(t):
	r"\+"
	return t

def t_MINUS_OP(t):
	r"-"
	return t

def t_MULTIPLICATION_OP(t):
	r"\*"
	return t

def t_DIVISION_OP(t):
	r"/"
	return t

def t_MODULUS_OP(t):
	r"%"
	return t
def t_SEMICOLON(t):
	r";"
	return t

def t_BLOCK_BEGIN(t):
	r"\{"
	return t

def t_BLOCK_ENDS(t):
	r"\}"
	return t

def t_OPEN_BRACKET(t):
	r"\["
	return t

def t_CLOSE_BRACKET(t):
	r"\]"
	return t

def t_OPEN_PARANTHESIS(t):
	r"\("
	return t

def t_CLOSE_PARANTHESIS(t):
	r"\)"
	return t

def t_COMMA(t):
	r","
	return t



def t_ASSIGNMENT_OP(t):
	r"=|"r"\+=|"r"-=|"r"\*=|"r"/=|"r"%="
	return t

	
def t_error(t):
	print "Illegal character %s" % t.value[0]
	t.lexer.skip(1)

#identifier
def t_IDENTIFIER(t):
    r"[\$@% ][a-zA-Z$_][\w$]*"
    t.type = reserved.get(t.value,'IDENTIFIER')    
    return t

lexer=lex.lex()
def runlexer(inputfile):
	program=open(inputfile).read()
	lexer.input(program)
	print "Type \t\t\t\t\t Value"
	print "---- \t\t\t\t\t ------"
	for tok in iter(lexer.token, None):
		print "%s \t\t\t\t\t %s" %(repr(tok.type),repr(tok.value))
	

if __name__=="__main__":
	from sys import argv 
	filename, inputfile = argv
	runlexer(inputfile)
