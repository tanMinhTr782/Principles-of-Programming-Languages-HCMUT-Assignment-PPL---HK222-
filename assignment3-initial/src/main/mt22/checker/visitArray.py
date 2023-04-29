  def visitArrayLit(self, ast, o): # nho suy dien kieu o day nha :> 
        ele = []
        # typehashmap = {
        #     "IntegerType": 0, 
        #     "FloatType": 0,
        #     "StringType": 0,
        #     "BooleanType":0,
        #     "AutoType": 0,
        #     "ArrayType": 0
        #     "VoidType": 0
        # }
        typehashmap = [0,0,0,0,0,0,0]
        for i in ast.explist: 
            ele += [self.visit(i,ele)]
        for i in range(0, len(ele) - 1):
            if type(ele[i]) is IntegerType: 
                typehashmap[0] += 1
            elif type(ele[i]) is FloatType: 
                typehashmap[1] += 1
            elif type(ele[i]) is StringType: 
                typehashmap[2] += 1
            elif type(ele[i]) is BooleanType: 
                typehashmap[3] += 1
            elif type(ele[i]) is AutoType:
                typehashmap[4] += 1
            elif type(ele[i]) is ArrayType:
                typehashmap[5] += 1
            else: typehashmap[6] += 1
        if typehashmap[4] == len(ele): 
            return ArrayType([len(ele)],AutoType())
        else:
            count = 0
            type2Infer = -1
            for i in range(7): 
                if typehashmap[i] > 0: count = count + 1
                if count > 2: raise IllegalArrayLiteral(ast)
            if count == 2:
                for i in range(7):
                    if i != 4: 
                        if typehashmap[i] == len(ele) - typehashmap[4]:
                            if i == 6:  raise IllegalArrayLiteral(ast)
                            type2Infer = i
                            break
                            
            if type2Infer == 0: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(IntegerType(),x)
            if type2Infer == 1: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(FloatType(),x)
            if type2Infer == 2: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(StringType(),x)
            if type2Infer == 3: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(BooleanType(),x)
            # if type2Infer == 5: 
            #     for x in ast.explist: 
            #         kind = self.visit(x,o)
            #         if type(kind) is AutoType:
            #             self.inferArrayLitEle(ArrayType(),x)
        if typehashmap[5] == len(ele):
            return ArrayType([len(ele)],ArrayType())
        if typehashmap[6] == len(ele): 
            raise IllegalArrayLiteral(ast)
        for i in range(len(ele) - 1): 
            if type(ele[i]) != type(ele[i+1]): 
                raise IllegalArrayLiteral(ast)
            # trong array co arraylit thi sao ? rofllmao , case nay bo nha ! 
            # tinh sau, met qua !
        if (type(ele[0])) is IntegerType: 
            return ArrayType([len(ele)],IntegerType())
        if (type(ele[0])) is BooleanType: 
            return ArrayType([len(ele)],BooleanType())
        if (type(ele[0])) is FloatType: 
            return ArrayType([len(ele)],FloatType())
        return ArrayType([len(ele)],StringType())       