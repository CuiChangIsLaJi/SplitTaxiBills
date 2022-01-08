#python SplitTaxiBills.py --payers-info payers.json --names-info names.txt --output-bill bill.json [--intermediate name]

import json
import os
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--payers-info",help="path for the payers' names and corresponding money they paid")
parser.add_argument("--names-info",help="path for the names of all participants")
parser.add_argument("--output-bill",help="path for the generated bill")
parser.add_argument("--intermediate",help="determine the index of intermediate")

def getPayersInfo(file):
    path = os.path.join(".\\payersInfo",file)
    payers = json.load(open(path,"r"))
    return payers
    
def getNames(file):
    path = os.path.join(".\\payersInfo",file)
    with open(path,"r") as f:
        names = f.read().splitlines()
    return names

def calculatePayment(payers,intermediate=None):
    prices = np.array(list(payers.values()))
    prices -= np.average(prices)
    if intermediate in payers.keys():
        prices -= prices[list(payers.keys()).index(intermediate)]
    payment = dict(zip(payers.keys(),prices))
    return payment

def saveBills(payment,output):
    print(payment)
    with open(output,"w") as f:
        json.dump(payment,f)

def main():
    args = vars(parser.parse_args())

    #Loading information of payers and all participants from json files
    payers = getPayersInfo(args["payers_info"])
    names = getNames(args["names_info"])
    if set(payers.keys()) <= set(names):
        temp = {}
        for name in names:
            temp[name] = payers.get(name,0.0)
        payers = temp
    else:
        raise ValueError("Mismatch found between payers list and participants list.")
    
    #Calculating the appropriate prices for each participant
    intermediate = args["intermediate"]
    payment = calculatePayment(payers,intermediate)
    
    #Summarizing the payment information
    saveBills(payment,args["output_bill"])

if __name__ == "__main__":
    main()