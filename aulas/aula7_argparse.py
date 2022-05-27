import argparse
parser = argparse.ArgumentParser()  
parser.add_argument("--idade", type=int, default=0)
args = parser.parse_args() 

print(f"Idade = {args.idade * 2} tipo de idade = {type(args.idade)}")