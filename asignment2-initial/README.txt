Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite
Then type: python run.py test CheckerSuite
Then type: python run.py test CodeGenSuite
1. java -jar ./antlr-4.9.2-complete.jar MT22.g4 
2. javac -classpath ./antlr-4.9.2-complete.jar MT22*.java
3. java -cp ".;./antlr-4.9.2-complete.jar" org.antlr.v4.gui.TestRig MT22 program -gui input.txt 
-------------------
python 



Câu hỏi: 
1. Inherit mình sẽ trả về ID của biến đc inherit phải không ạ. 