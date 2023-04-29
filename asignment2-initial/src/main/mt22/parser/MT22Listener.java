// Generated from MT22.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MT22Parser}.
 */
public interface MT22Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MT22Parser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MT22Parser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MT22Parser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#decllist}.
	 * @param ctx the parse tree
	 */
	void enterDecllist(MT22Parser.DecllistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#decllist}.
	 * @param ctx the parse tree
	 */
	void exitDecllist(MT22Parser.DecllistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(MT22Parser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(MT22Parser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#vardecl}.
	 * @param ctx the parse tree
	 */
	void enterVardecl(MT22Parser.VardeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#vardecl}.
	 * @param ctx the parse tree
	 */
	void exitVardecl(MT22Parser.VardeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#varnoinit}.
	 * @param ctx the parse tree
	 */
	void enterVarnoinit(MT22Parser.VarnoinitContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#varnoinit}.
	 * @param ctx the parse tree
	 */
	void exitVarnoinit(MT22Parser.VarnoinitContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#varassign}.
	 * @param ctx the parse tree
	 */
	void enterVarassign(MT22Parser.VarassignContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#varassign}.
	 * @param ctx the parse tree
	 */
	void exitVarassign(MT22Parser.VarassignContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#vartype}.
	 * @param ctx the parse tree
	 */
	void enterVartype(MT22Parser.VartypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#vartype}.
	 * @param ctx the parse tree
	 */
	void exitVartype(MT22Parser.VartypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#atomic_type}.
	 * @param ctx the parse tree
	 */
	void enterAtomic_type(MT22Parser.Atomic_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#atomic_type}.
	 * @param ctx the parse tree
	 */
	void exitAtomic_type(MT22Parser.Atomic_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#idlist}.
	 * @param ctx the parse tree
	 */
	void enterIdlist(MT22Parser.IdlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#idlist}.
	 * @param ctx the parse tree
	 */
	void exitIdlist(MT22Parser.IdlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(MT22Parser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(MT22Parser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#arraydecl}.
	 * @param ctx the parse tree
	 */
	void enterArraydecl(MT22Parser.ArraydeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#arraydecl}.
	 * @param ctx the parse tree
	 */
	void exitArraydecl(MT22Parser.ArraydeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#arrayinit}.
	 * @param ctx the parse tree
	 */
	void enterArrayinit(MT22Parser.ArrayinitContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#arrayinit}.
	 * @param ctx the parse tree
	 */
	void exitArrayinit(MT22Parser.ArrayinitContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#arraylit}.
	 * @param ctx the parse tree
	 */
	void enterArraylit(MT22Parser.ArraylitContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#arraylit}.
	 * @param ctx the parse tree
	 */
	void exitArraylit(MT22Parser.ArraylitContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#arrayVal}.
	 * @param ctx the parse tree
	 */
	void enterArrayVal(MT22Parser.ArrayValContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#arrayVal}.
	 * @param ctx the parse tree
	 */
	void exitArrayVal(MT22Parser.ArrayValContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#arrayParam}.
	 * @param ctx the parse tree
	 */
	void enterArrayParam(MT22Parser.ArrayParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#arrayParam}.
	 * @param ctx the parse tree
	 */
	void exitArrayParam(MT22Parser.ArrayParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#dimension}.
	 * @param ctx the parse tree
	 */
	void enterDimension(MT22Parser.DimensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#dimension}.
	 * @param ctx the parse tree
	 */
	void exitDimension(MT22Parser.DimensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void enterFuncdecl(MT22Parser.FuncdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void exitFuncdecl(MT22Parser.FuncdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#base_funcdecl}.
	 * @param ctx the parse tree
	 */
	void enterBase_funcdecl(MT22Parser.Base_funcdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#base_funcdecl}.
	 * @param ctx the parse tree
	 */
	void exitBase_funcdecl(MT22Parser.Base_funcdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#returntype}.
	 * @param ctx the parse tree
	 */
	void enterReturntype(MT22Parser.ReturntypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#returntype}.
	 * @param ctx the parse tree
	 */
	void exitReturntype(MT22Parser.ReturntypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(MT22Parser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(MT22Parser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#paramlist}.
	 * @param ctx the parse tree
	 */
	void enterParamlist(MT22Parser.ParamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#paramlist}.
	 * @param ctx the parse tree
	 */
	void exitParamlist(MT22Parser.ParamlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#paramprime}.
	 * @param ctx the parse tree
	 */
	void enterParamprime(MT22Parser.ParamprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#paramprime}.
	 * @param ctx the parse tree
	 */
	void exitParamprime(MT22Parser.ParamprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(MT22Parser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(MT22Parser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#paramHead}.
	 * @param ctx the parse tree
	 */
	void enterParamHead(MT22Parser.ParamHeadContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#paramHead}.
	 * @param ctx the parse tree
	 */
	void exitParamHead(MT22Parser.ParamHeadContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#parambase}.
	 * @param ctx the parse tree
	 */
	void enterParambase(MT22Parser.ParambaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#parambase}.
	 * @param ctx the parse tree
	 */
	void exitParambase(MT22Parser.ParambaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#paramtype}.
	 * @param ctx the parse tree
	 */
	void enterParamtype(MT22Parser.ParamtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#paramtype}.
	 * @param ctx the parse tree
	 */
	void exitParamtype(MT22Parser.ParamtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#blocklist}.
	 * @param ctx the parse tree
	 */
	void enterBlocklist(MT22Parser.BlocklistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#blocklist}.
	 * @param ctx the parse tree
	 */
	void exitBlocklist(MT22Parser.BlocklistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(MT22Parser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(MT22Parser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#allowed_blockstmt}.
	 * @param ctx the parse tree
	 */
	void enterAllowed_blockstmt(MT22Parser.Allowed_blockstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#allowed_blockstmt}.
	 * @param ctx the parse tree
	 */
	void exitAllowed_blockstmt(MT22Parser.Allowed_blockstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#assignstmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignstmt(MT22Parser.AssignstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#assignstmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignstmt(MT22Parser.AssignstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void enterIfstmt(MT22Parser.IfstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void exitIfstmt(MT22Parser.IfstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#if_noelsestmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_noelsestmt(MT22Parser.If_noelsestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#if_noelsestmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_noelsestmt(MT22Parser.If_noelsestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#ifelsestmt}.
	 * @param ctx the parse tree
	 */
	void enterIfelsestmt(MT22Parser.IfelsestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#ifelsestmt}.
	 * @param ctx the parse tree
	 */
	void exitIfelsestmt(MT22Parser.IfelsestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#forstmt}.
	 * @param ctx the parse tree
	 */
	void enterForstmt(MT22Parser.ForstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#forstmt}.
	 * @param ctx the parse tree
	 */
	void exitForstmt(MT22Parser.ForstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#whilestmt}.
	 * @param ctx the parse tree
	 */
	void enterWhilestmt(MT22Parser.WhilestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#whilestmt}.
	 * @param ctx the parse tree
	 */
	void exitWhilestmt(MT22Parser.WhilestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#dowhile_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDowhile_stmt(MT22Parser.Dowhile_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#dowhile_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDowhile_stmt(MT22Parser.Dowhile_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnstmt(MT22Parser.ReturnstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnstmt(MT22Parser.ReturnstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#callstmt}.
	 * @param ctx the parse tree
	 */
	void enterCallstmt(MT22Parser.CallstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#callstmt}.
	 * @param ctx the parse tree
	 */
	void exitCallstmt(MT22Parser.CallstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void enterContinuestmt(MT22Parser.ContinuestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void exitContinuestmt(MT22Parser.ContinuestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakstmt(MT22Parser.BreakstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakstmt(MT22Parser.BreakstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#blockstmt}.
	 * @param ctx the parse tree
	 */
	void enterBlockstmt(MT22Parser.BlockstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#blockstmt}.
	 * @param ctx the parse tree
	 */
	void exitBlockstmt(MT22Parser.BlockstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#loopstmt}.
	 * @param ctx the parse tree
	 */
	void enterLoopstmt(MT22Parser.LoopstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#loopstmt}.
	 * @param ctx the parse tree
	 */
	void exitLoopstmt(MT22Parser.LoopstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#scalar_variable}.
	 * @param ctx the parse tree
	 */
	void enterScalar_variable(MT22Parser.Scalar_variableContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#scalar_variable}.
	 * @param ctx the parse tree
	 */
	void exitScalar_variable(MT22Parser.Scalar_variableContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#exprlist}.
	 * @param ctx the parse tree
	 */
	void enterExprlist(MT22Parser.ExprlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#exprlist}.
	 * @param ctx the parse tree
	 */
	void exitExprlist(MT22Parser.ExprlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expprime}.
	 * @param ctx the parse tree
	 */
	void enterExpprime(MT22Parser.ExpprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expprime}.
	 * @param ctx the parse tree
	 */
	void exitExpprime(MT22Parser.ExpprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MT22Parser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MT22Parser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr1}.
	 * @param ctx the parse tree
	 */
	void enterExpr1(MT22Parser.Expr1Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr1}.
	 * @param ctx the parse tree
	 */
	void exitExpr1(MT22Parser.Expr1Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterExpr2(MT22Parser.Expr2Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitExpr2(MT22Parser.Expr2Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr3}.
	 * @param ctx the parse tree
	 */
	void enterExpr3(MT22Parser.Expr3Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr3}.
	 * @param ctx the parse tree
	 */
	void exitExpr3(MT22Parser.Expr3Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr4}.
	 * @param ctx the parse tree
	 */
	void enterExpr4(MT22Parser.Expr4Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr4}.
	 * @param ctx the parse tree
	 */
	void exitExpr4(MT22Parser.Expr4Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr5}.
	 * @param ctx the parse tree
	 */
	void enterExpr5(MT22Parser.Expr5Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr5}.
	 * @param ctx the parse tree
	 */
	void exitExpr5(MT22Parser.Expr5Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr6}.
	 * @param ctx the parse tree
	 */
	void enterExpr6(MT22Parser.Expr6Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr6}.
	 * @param ctx the parse tree
	 */
	void exitExpr6(MT22Parser.Expr6Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr7}.
	 * @param ctx the parse tree
	 */
	void enterExpr7(MT22Parser.Expr7Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr7}.
	 * @param ctx the parse tree
	 */
	void exitExpr7(MT22Parser.Expr7Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#callexpr}.
	 * @param ctx the parse tree
	 */
	void enterCallexpr(MT22Parser.CallexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#callexpr}.
	 * @param ctx the parse tree
	 */
	void exitCallexpr(MT22Parser.CallexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#subexpr}.
	 * @param ctx the parse tree
	 */
	void enterSubexpr(MT22Parser.SubexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#subexpr}.
	 * @param ctx the parse tree
	 */
	void exitSubexpr(MT22Parser.SubexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#indexop}.
	 * @param ctx the parse tree
	 */
	void enterIndexop(MT22Parser.IndexopContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#indexop}.
	 * @param ctx the parse tree
	 */
	void exitIndexop(MT22Parser.IndexopContext ctx);
}