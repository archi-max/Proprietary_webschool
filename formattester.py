from WordFormatter import WordFormatter
from pygments import highlight
from pygments.lexers import get_lexer_by_name
code= 'print("ok")'
lexer = get_lexer_by_name("python", stripall=True)
formatter = WordFormatter(linenos=True, cssclass="source")
result = highlight(code, lexer, formatter)