        print(Parser(tokens).parse())
        parsedRes=Parser(tokens).parse()
        if not parsedRes:
             print(f"{RED} Something Might be Wrong {RESET}")
             continue
        
        res=Interpreter().recursive_Calc(parsedRes)
        if not res:
            print(f"{RED} Something Might be Wrong {RESET}")
            continue


        print(res)