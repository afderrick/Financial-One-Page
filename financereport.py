# Title: Family Financial Plan

import csv
import datetime
import os, sys

# Declare variables

####################
# Account Balances #
####################

filename = "assetsliabilities.csv"
with open(filename, 'r') as data:
    readCSV = csv.reader(data, delimiter=',')
    dollars = []
    for row in readCSV:
        value = float(row[1])
        dollars.append(value)

## Assets
intJointChecking = dollars[0]
intAllySavings = dollars[1]
intVanguardBrokerage = dollars[2]
intNFCUSavings1 = dollars[3]
intNFCUSavings2 = dollars[4]
intTSP = dollars[5]
intVanguardIRA = dollars[6]
intChild1529 = dollars[7]
intChild2529 = dollars[8]
intChild3529 = dollars[9]
intHouseValue = dollars[10]
intTotalAssets = intJointChecking + intAllySavings + intVanguardBrokerage + + intNFCUSavings1 + intNFCUSavings2 +intTSP + intVanguardIRA + intChild1529 + intChild2529 + intChild3529 + intHouseValue
intCurrentAssets = intTotalAssets

## Liabilities
intMortgage = dollars[11]
intTotalLiabilities = intMortgage
intCurrentLiabilities = intTotalLiabilities * -1
intCurrentNWValue = intCurrentAssets + intCurrentLiabilities
intCurrentNWValue = round(intCurrentNWValue, 0)
strCurrentNWValue = ('{:,}'.format(intCurrentNWValue))

## Emergency Fund
intEmergencyFund = dollars[12]

intChild1529YearGoal = dollars[13]
intChild2529YearGoal = dollars[14]
intChild3529YearGoal = dollars[15]
int5YearVacationCurrent = dollars[16]
intChild1529FinalGoal = 33500
intChild2529FinalGoal = 36000
intChild3529FinalGoal = 108800
int5YearVacationFinal = 20000

# Percentage Math
int5YearVacationPerc = int5YearVacationCurrent / int5YearVacationFinal
intChild1529GoalPerc = intChild1529YearGoal / intChild1529FinalGoal
intChild2529GoalPerc = intChild2529YearGoal / intChild2529FinalGoal
intChild3529GoalPerc = intChild3529YearGoal / intChild3529FinalGoal
intChild1529Perc = intChild1529 / intChild1529FinalGoal
intChild2529Perc = intChild2529 / intChild2529FinalGoal
intChild3529Perc = intChild3529 / intChild3529FinalGoal
int5YearVacationPerc = round(int5YearVacationPerc, 2)
intChild1529GoalPerc = round(intChild1529GoalPerc, 2)
intChild2529GoalPerc = round(intChild2529GoalPerc, 2)
intChild3529GoalPerc = round(intChild3529GoalPerc, 2)
intChild1529Perc = round(intChild1529Perc, 2)
intChild2529Perc = round(intChild2529Perc, 2)
intChild3529Perc = round(intChild3529Perc, 2)

# Debts
filename = "debtpayments.csv"
with open(filename, 'r') as data:
    readCSV = csv.reader(data, delimiter=',')
    dollars = []
    for row in readCSV:
        value = float(row[1])
        dollars.append(value)

intDebtMortage = dollars[0]
intTotalMonthlyDebts = intDebtMortage

############
# Net Worth #
############

filename = "networth.csv"
with open(filename, 'r') as data:
    readCSV = csv.reader(data, delimiter=',')
    dollars = []
    for row in readCSV:
        value = float(row[1])
        dollars.append(value)

int5YearAssets = dollars[0]
int4YearAssets = dollars[1]
int3YearAssets = dollars[2]
int2YearAssets = dollars[3]
int5YearLiabilities = dollars[4]
int4YearLiabilities = dollars[5]
int3YearLiabilities = dollars[6]
int2YearLiabilities = dollars[7]
int5YearNWValue = int5YearAssets + int5YearLiabilities
int4YearNWValue = int4YearAssets + int4YearLiabilities
int3YearNWValue = int3YearAssets + int3YearLiabilities
int2YearNWValue = int2YearAssets + int2YearLiabilities

##########
# Income #
##########

filename = "income.csv"
with open(filename, 'r') as data:
    readCSV = csv.reader(data, delimiter=',')
    dollars = []
    for row in readCSV:
        value = float(row[1])
        dollars.append(value)

intPayBase = dollars[0] 
intPayBAS = dollars[1]
intPayBAH = dollars[2]

## Income Taxes and Deductions
intTaxesFed = dollars[3]
intTaxesSocial = dollars[4]
intTaxesMedicare = dollars[5]
intDeductionsSGLI = dollars[6]
intDeductionsSGLIFam = dollars[7]
intDeductionsTSP = dollars[8]
intDeductionsDental = dollars[9]

### Income Math
intAnnualPay = (intPayBase + intPayBAS + intPayBAH) * 12
intGrossPay = intPayBase + intPayBAS + intPayBAH
intGrossPay = round(intGrossPay, 2)
intNetPay = (intPayBase + intPayBAS + intPayBAH) - (intTaxesFed + intTaxesSocial + intTaxesMedicare + intDeductionsSGLI + intDeductionsSGLIFam + intDeductionsTSP + intDeductionsDental)
intTotalTaxes = intTaxesFed + intTaxesSocial + intTaxesMedicare
intTotalPayInsurance = intDeductionsSGLI + intDeductionsSGLIFam + intDeductionsDental

# Math Check
intNetPay = round(intNetPay, 2)

############
############
##        ##
## Budget ##
##        ##
############
############

filename = "budget.csv"
with open(filename, 'r') as data:
    readCSV = csv.reader(data, delimiter=',')
    dollars = []
    for row in readCSV:
        value = float(row[1])
        dollars.append(value)

## Housing
intBudgetMortgage = dollars[0]
intBudgetHOA = dollars[1]
intBudgetHousingMaint = dollars[2]
intBudgetHousing = intBudgetMortgage + intBudgetHOA + intBudgetHousingMaint
intBudgetHousing = round(intBudgetHousing, 2)

## Utilities
intBudgetElectricity = dollars[3]
intBudgetWater = dollars[4]
intBudgetTrash = dollars[5]
intBudgetInternet = dollars[7]
intBudgetTV = dollars[6]
intBudgetPhone = dollars[8]
intBudgetUtilities = intBudgetElectricity + intBudgetWater + intBudgetTrash + intBudgetInternet + intBudgetTV + intBudgetPhone

## Transportation
intBudgetGas = dollars[9]
intBudgetInsurance = dollars[10]
intBudgetTransportation = intBudgetGas + intBudgetInsurance

## Food
intBudgetGroceries = dollars[11]
intBudgetRestaurants = dollars[12]
intBudgetFood = intBudgetGroceries + intBudgetRestaurants

## Savings and Giving
intBudgetTithe = dollars[13]
intBudgetGiving = intBudgetTithe

## Entertainment
intBudgetEntertainment = dollars[14]
intBudgetDateNight = dollars[15]
intBudgetVacation = dollars[23]
intBudgetEntertainmentTotal = intBudgetEntertainment + intBudgetDateNight + intBudgetVacation

## Spending Account
intBudgetJoint = dollars[16]
intBudgetSpending1 = dollars[17]
intBudgetSpending2 = dollars[18]
intBudgetKids = dollars[19]
intBudgetGifts = dollars[20]
intBudgetProfessional = dollars[21]
intBudgetSchool = dollars[22]
intBudgetSpendingAccounts = intBudgetJoint + intBudgetSpending1 + intBudgetSpending2 + intBudgetKids + intBudgetGifts + intBudgetProfessional + intBudgetSchool

## Savings
intBudgetSavings = dollars[24]

## Taxes
intBudgetCarRegistration = dollars[25]
intBudgetTaxes = intBudgetCarRegistration

# Calculate Total in Budget Spending
intBudgetTotalSpending = intBudgetHousing + intBudgetUtilities + intBudgetTransportation + intBudgetFood + intBudgetGiving + intBudgetEntertainmentTotal + intBudgetSpendingAccounts + intBudgetSavings + intBudgetTaxes

## Budget Error Checking
intBudgetCheck = intNetPay - intBudgetTotalSpending
strBudgetCheck = ('{:,}'.format(intBudgetCheck)) 
if intBudgetCheck > 0:
    print("Budget ALERT! You budgeted $" + str(strBudgetCheck) + " under your budgeted income.")
if intBudgetCheck < 0:
    print("Budget WARNING! You budgeted $" +str(strBudgetCheck) + " over your budgeted income.")
if intBudgetCheck == 0:
    print("Budget Message. You budgeted all your pennies. Congrats.")


## Average Spending over 12 months
filename = "averagespending.csv"
with open(filename, 'r') as data:
    readCSV = csv.reader(data, delimiter=',')
    dollars = []
    for row in readCSV:
        value = float(row[1])
        dollars.append(value)

## Average Income
intAvgIncome = dollars[0]

## Housing
intAvgMortgage = dollars[1]
intAvgHOA = dollars[2]
intAvgHousingMaint = dollars[3]
intAvgHousing = intAvgMortgage + intAvgHOA + intAvgHousingMaint

## Utilities
intAvgElectricity = dollars[4]
intAvgWater = dollars[5]
intAvgTrash = dollars[6]
intAvgInternet = dollars[8]
intAvgTV = dollars[7]
intAvgPhone = dollars[9]
intAvgUtilities = intAvgElectricity + intAvgWater + intAvgTrash + intAvgInternet + intAvgTV + intAvgPhone
intAvgUtilities = round(intAvgUtilities, 2)

## Transportation
intAvgGas = dollars[10]
intAvgInsurance = dollars[11]
intAvgTransportation = intAvgGas + intAvgInsurance

## Food
intAvgGroceries = dollars[12]
intAvgRestaurants = dollars[13]
intAvgFood = intAvgGroceries + intAvgRestaurants
intAvgFood = round(intAvgFood, 2)

## Savings and Giving
intAvgTithe = dollars[14]
intAvgGiving = intAvgTithe

## Entertainment
intAvgEntertainment = dollars[15]
intAvgDateNight = dollars[16]
intAvgVacation = dollars[24]
intAvgEntertainmentTotal = intAvgEntertainment + intAvgDateNight + intAvgVacation

## Spending Account
intAvgJoint = dollars[17]
intAvgSpending1 = dollars[18]
intAvgSpending2 = dollars[19]
intAvgKids = dollars[20]
intAvgGifts = dollars[21]
intAvgProfessional = dollars[22]
intAvgSchool = dollars[23]
intAvgSpendingAccounts = intAvgJoint + intAvgSpending1 + intAvgSpending2 + intAvgKids + intAvgGifts + intAvgProfessional + intAvgSchool

## Savings
intAvgSavings = dollars[25]

## Taxes
intAvgCarRegistration = dollars[26]
intAvgTaxes = intAvgCarRegistration

# Calculate Total in Budget Spending
intAvgTotalSpending = intAvgHousing + intAvgUtilities + intAvgTransportation + intAvgFood + intAvgGiving + intAvgEntertainmentTotal + intAvgSpendingAccounts + intAvgSavings + intAvgTaxes

## Actual Spending Cashflow Check
intAvgSpendingCheck = intAvgIncome - intAvgTotalSpending
intAvgSpendingCheck = round(intAvgSpendingCheck, 2)
strCashFlow = ('{:,}'.format(intAvgSpendingCheck)) 
if intAvgSpendingCheck> 0:
    print("Cashflow Message. You have a positive cashflow of $" + str(strCashFlow))
if intAvgSpendingCheck < 0:
    print("Cashflow WARNING! You have a negative cashflow of $" +str(strCashFlow))
if intAvgSpendingCheck == 0:
    print("Cashflow Warning. You spend your total income. You have no positive cash flow.")

# Money Ratio Math

## Emergency Fund
intEmergencyFundRatio = intEmergencyFund / (intAvgTotalSpending - intAvgSavings - intAvgGiving)
intEmergencyFundRatio = round(intEmergencyFundRatio, 1)
print("Your Emergency Fund Ratio is " + str(intEmergencyFundRatio) + "x")

## Target Net Worth Ratio
currentDateTime = datetime.datetime.now()
currentdate = currentDateTime.date()
intAge = currentdate.year - 1981
intTargetNetworth = intAge * (intAnnualPay / 10)
intTargetNetworthRatio = ((intTotalAssets - intHouseValue) / intTargetNetworth) * 100
intTargetNetworthRatio = round(intTargetNetworthRatio, 1)
print("Your Target Net Worth Ratio is " + str(intTargetNetworthRatio) + "%")

## House Equity
intHouseEquity = ((intHouseValue - intMortgage)/intHouseValue)*100
intHouseEquity = round(intHouseEquity, 1)
print("Your House Equity is " + str(intHouseEquity) + "%")

## Debt to Asset Ratio
intDebtAssetRatio = (intTotalLiabilities / intTotalAssets) * 100
intDebtAssetRatio = round(intDebtAssetRatio, 1)
print("Your Debt to Asset ratio is " + str(intDebtAssetRatio) + "%")

## Total Debt to Income Ratio
intDebtIncomeRatio = ((intTotalMonthlyDebts * 12) / intAnnualPay) * 100
intDebtIncomeRatio = round(intDebtIncomeRatio, 1)
print("Your Debt to Income Ratio is " + str(intDebtIncomeRatio) + "%")

## Mortgage to Income Ratio
intHouseIncomeRatio = (intAvgHousing / intNetPay) * 100
intHouseIncomeRatio = round(intHouseIncomeRatio, 1)
print("Your Mortgage to Income Ratio is " + str(intHouseIncomeRatio) + "%")

## Savings Ratio
intSavingsRatio = ((intAvgSavings * 12) / intAnnualPay) * 100
intSavingsRatio = round(intSavingsRatio, 1)
print("Your Savings Ratio is " + str(intSavingsRatio) + "%")

## Investments Ratio
intInvestmentRatio = ((intTotalAssets - intHouseValue) / intTotalAssets) * 100
intInvestmentRatio = round(intInvestmentRatio, 1)
print("Your Investment Ratio is " + str(intInvestmentRatio) + "%")

# Retirement Ratio
intRetirementRatio = ((intTSP + intVanguardIRA) / ((intAvgTotalSpending * 12)* 25)) * 100
intRetirementRatio = round(intRetirementRatio, 1)
print("Your Retirement Ratio is " + str(intRetirementRatio) + "%")

# Calculate the Living, Giving, Growing, Owing Pie Chart

intLiving = (intAvgHousing - intAvgMortgage + intAvgUtilities + intAvgTransportation + intAvgFood + intAvgEntertainmentTotal + intAvgSpendingAccounts + intAvgSavings + intAvgTaxes) / intAvgIncome
intGiving = intAvgGiving / intAvgIncome
intOwing = intAvgMortgage / intAvgIncome
intGrowing = (intAvgSpendingCheck) / intAvgIncome
intLiving = intLiving * 100
intGiving = intGiving * 100
intOwing = intOwing * 100
intGrowing = intGrowing * 100
intLiving = round(intLiving, 0)
intGiving = round(intGiving, 0)
intOwing = round(intOwing, 0)
intGrowing = round(intGrowing, 0)

# Pie Chart Math check, make sure the ratios = 100%
if (intLiving + intGiving + intOwing + intGrowing) < 100: 
    intPieChartCheck = intLiving + intGiving + intOwing + intGrowing + intTaxes
    while intPieChartCheck < 100.01:
        intLiving = intLiving + .01
        intPieChartCheck = intLiving + intGiving + intOwing + intGrowing
if (intLiving + intGiving + intOwing + intGrowing) > 100:
    intPieChartCheck = intLiving + intGiving + intOwing + intGrowing
    while intPieChartCheck > 100.01:
        intLiving = intLiving - .01
        intPieChartCheck = intLiving + intGiving + intOwing + intGrowing

intLiving = round(intLiving, 2)
print("Living: " + str(intLiving) + "% // Giving: " + str(intGiving) + "% // Owing: " + str(intOwing) + "% // Growing: " + str(intGrowing) + "%")

# Export pythong script output to a file 
with open("export.txt", "w") as export:
    if intBudgetCheck > 0:
        export.write("Budget ALERT! You budgeted $" + str(intBudgetCheck) + " under your budgeted income. \n")
    if intBudgetCheck < 0:
        export.write("Budget WARNING! You budgeted $" +str(intBudgetCheck) + " over your budgeted income. \n")
    if intBudgetCheck == 0:
        export.write("Budget Message. You budgeted all your pennies. Congrats. \n")
    if intAvgSpendingCheck> 0:
        export.write("Cashflow Message. You have a positive cashflow of $" + str(strCashFlow) + "\n")
    if intAvgSpendingCheck < 0:
        export.write("Cashflow WARNING! You have a negative cashflow of $" +str(strCashFlow) + "\n")
    if intAvgSpendingCheck == 0:
        export.write("Cashflow Warning. You spend your total income. You have no positive cash flow. \n")
    export.write("Your Emergency Fund Ratio is " + str(intEmergencyFundRatio) + "x \n")
    export.write("Your Target Net Worth Ratio is " + str(intTargetNetworthRatio) + "% \n")
    export.write("Your Solvency Ratio is " + str(intHouseEquity) + "% \n")
    export.write("Your Debt to Asset ratio is " + str(intDebtAssetRatio) + "% \n")
    export.write("Your Debt to Income Ratio is " + str(intDebtIncomeRatio) + "% \n")
    export.write("Your Mortgage to Income Ratio is " + str(intHouseIncomeRatio) + "% \n")
    export.write("Your Savings Ratio is " + str(intSavingsRatio) + "% \n")
    export.write("Your Investment Ratio is " + str(intInvestmentRatio) + "% \n")
    export.write("Your Retirement Ratio is " + str(intRetirementRatio) + "% \n")
    export.write("Living: " + str(intLiving * 100) + "% // Giving: " + str(intGiving * 100) + "% // Owing: " + str(intOwing * 100) + "% // Growing: " + str(intGrowing * 100) + "% \n")
    export.close()

#########################
# Set Colors for Ratios %
#########################

if intEmergencyFundRatio < 1:
    colorEmergencyFundRatio = "red"
elif 1 <= intEmergencyFundRatio < 3:
    colorEmergencyFundRatio = "yellow"
elif intEmergencyFundRatio >= 3:
    colorEmergencyFundRatio = "green"
else:
    colorEmergencyFundRatio = "black"

if intTargetNetworthRatio < 80:
    colorNetworthRatio= "red"
elif 80 <= intTargetNetworthRatio < 95:
    colorNetworthRatio = "yellow"
elif intNetworthRatio >= 95:
    colorNetWorthRatio = "green"
else:
    colorNetworthRatio = "black"

if intHouseEquity < 25:
    colorHouseEquity = "red"
elif 25 <= intHouseEquity < 50:
    colorHouseEquity = "yellow"
elif intHouseEquity >= 50:
    colorHouseEquity = "green"
else:
    colorHouseEquity= "black"

if intDebtAssetRatio > 36:
    colorDebtAssetRatio = "red"
elif 36 >= intDebtAssetRatio >= 30:
    colorDebtAssetRatio = "yellow"
elif intDebtAssetRatio < 30:
    colorDebtAssetRatio = "green"
else:
    colorDebtAssetRatio = "black"

if intDebtIncomeRatio > 36:
    colorDebtIncomeRatio = "red"
elif 36 >= intDebtIncomeRatio >= 30:
    colorDebtIncomeRatio = "yellow"
elif intDebtIncomeRatio < 30:
    colorDebtIncomeRatio = "green"
else:
    colorDebtIncomeRatio = "black"

if intHouseIncomeRatio > 36:
    colorHouseIncomeRatio = "red"
elif 36 >= intHouseIncomeRatio >= 30:
    colorHouseIncomeRatio = "yellow"
elif intHouseIncomeRatio < 30:
    colorHouseIncomeRatio = "green"
else:
    colorHouseIncomeRatio = "black"

if intSavingsRatio < 5:
    colorSavingsRatio = "red"
elif 10 >= intSavingsRatio >= 5:
    colorSavingsRatio = "yellow"
elif intSavingsRatio > 10:
    colorSavingsRatio = "green"
else:
    colorSavingsRatio = "black"

#################################
## Convert Integers to Strings ##
#################################

strNFCUSavings1 = ('{:,}'.format(intNFCUSavings1))
strNFCUSavings2 = ('{:,}'.format(intNFCUSavings2))
strJointChecking = ('{:,}'.format(intJointChecking))
strAllySavings = ('{:,}'.format(intAllySavings))
strVanguardBrokerage = ('{:,}'.format(intVanguardBrokerage))
strTotalonBudget = ('{:,}'.format(intNFCUSavings1 + intNFCUSavings2 + intJointChecking + intAllySavings + intVanguardBrokerage))
strBudgetMortgage = ('{:,}'.format(intBudgetMortgage))
strBudgetHOA = ('{:,}'.format(intBudgetHOA))
strBudgetHousingMaint = ('{:,}'.format(intBudgetHousingMaint))
strBudgetHousing = ('{:,}'.format(intBudgetHousing))
strBudgetElectricity = ('{:,}'.format(intBudgetElectricity))
strBudgetWater = ('{:,}'.format(intBudgetWater))
strBudgetTrash = ('{:,}'.format(intBudgetTrash))
strBudgetInternet = ('{:,}'.format(intBudgetInternet))
strBudgetTV = ('{:,}'.format(intBudgetTV))
strBudgetPhone = ('{:,}'.format(intBudgetPhone))
strBudgetUtilities = ('{:,}'.format(intBudgetUtilities))
strBudgetGas = ('{:,}'.format(intBudgetGas))
strBudgetInsurance = ('{:,}'.format(intBudgetInsurance))
strBudgetTransportation = ('{:,}'.format(intBudgetTransportation))
strBudgetGroceries = ('{:,}'.format(intBudgetGroceries))
strBudgetRestaurants = ('{:,}'.format(intBudgetRestaurants))
strBudgetFood = ('{:,}'.format(intBudgetFood))
strBudgetTithe= ('{:,}'.format(intBudgetTithe))
strBudgetGiving = ('{:,}'.format(intBudgetGiving))
strBudgetEntertainment = ('{:,}'.format(intBudgetEntertainment))
strBudgetDateNight = ('{:,}'.format(intBudgetDateNight))
strBudgetEntertainmentTotal = ('{:,}'.format(intBudgetEntertainmentTotal))
strBudgetJoint = ('{:,}'.format(intBudgetJoint))
strBudgetSpending1 = ('{:,}'.format(intBudgetSpending1))
strBudgetSpending2 = ('{:,}'.format(intBudgetSpending2))
strBudgetKids = ('{:,}'.format(intBudgetKids))
strBudgetGifts = ('{:,}'.format(intBudgetGifts))
strBudgetProfessional = ('{:,}'.format(intBudgetProfessional))
strBudgetSchool = ('{:,}'.format(intBudgetSchool))
strBudgetSpendingAccounts = ('{:,}'.format(intBudgetSpendingAccounts))
strBudgetSavings = ('{:,}'.format(intBudgetSavings))
strBudgetCarRegistration = ('{:,}'.format(intBudgetCarRegistration))
strBudgetTaxes = ('{:,}'.format(intBudgetTaxes))
strBudgetTotalSpending = ('{:,}'.format(intBudgetTotalSpending))
strBudgetVacation = ('{:,}'.format(intBudgetVacation))

strAvgIncome = ('{:,}'.format(intAvgIncome))
strAvgMortgage = ('{:,}'.format(intAvgMortgage))
strAvgHOA = ('{:,}'.format(intAvgHOA))
strAvgHousingMaint = ('{:,}'.format(intAvgHousingMaint))
strAvgHousing = ('{:,}'.format(intAvgHousing))
strAvgElectricity = ('{:,}'.format(intAvgElectricity))
strAvgWater = ('{:,}'.format(intAvgWater))
strAvgTrash = ('{:,}'.format(intAvgTrash))
strAvgInternet = ('{:,}'.format(intAvgInternet))
strAvgTV = ('{:,}'.format(intAvgTV))
strAvgPhone = ('{:,}'.format(intAvgPhone))
strAvgUtilities = ('{:,}'.format(intAvgUtilities))
strAvgGas = ('{:,}'.format(intAvgGas))
strAvgInsurance = ('{:,}'.format(intAvgInsurance))
strAvgTransportation = ('{:,}'.format(intAvgTransportation))
strAvgGroceries = ('{:,}'.format(intAvgGroceries))
strAvgRestaurants = ('{:,}'.format(intAvgRestaurants))
strAvgFood = ('{:,}'.format(intAvgFood))
strAvgTithe = ('{:,}'.format(intAvgTithe))
strAvgGiving = ('{:,}'.format(intAvgGiving))
strAvgEntertainment = ('{:,}'.format(intAvgEntertainment))
strAvgDateNight = ('{:,}'.format(intAvgDateNight))
strAvgEntertainmentTotal = ('{:,}'.format(intAvgEntertainmentTotal))
strAvgJoint = ('{:,}'.format(intAvgJoint))
strAvgSpending1 = ('{:,}'.format(intAvgSpending1))
strAvgSpending2 = ('{:,}'.format(intAvgSpending2))
strAvgKids = ('{:,}'.format(intAvgKids))
strAvgGifts = ('{:,}'.format(intAvgGifts))
strAvgProfessional = ('{:,}'.format(intAvgProfessional))
strAvgSchool = ('{:,}'.format(intAvgSchool))
strAvgSpendingAccounts = ('{:,}'.format(intAvgSpendingAccounts))
strAvgSavings = ('{:,}'.format(intAvgSavings))
strAvgCarRegistration = ('{:,}'.format(intAvgCarRegistration))
strAvgTaxes = ('{:,}'.format(intAvgTaxes))
intAvgTotalSpending = round(intAvgTotalSpending, 2)
strAvgTotalSpending = ('{:,}'.format(intAvgTotalSpending))
strAvgVacation = ('{:,}'.format(intAvgVacation))

strHouseValue = ('{:,}'.format(intHouseValue))
strTSP = ('{:,}'.format(intTSP))
strVanguardIRA = ('{:,}'.format(intVanguardIRA))
strChild1529 = ('{:,}'.format(intChild1529))
strChild2529 = ('{:,}'.format(intChild2529))
strChild3529 = ('{:,}'.format(intChild3529))
strMortgage = ('{:,}'.format(intMortgage))
intTotalOffBudget = intHouseValue + intTSP + intVanguardIRA + intChild1529 + intChild2529 + intChild3529
intTotalOffBudget = round(intTotalOffBudget, 2)
strTotalOffBudget = ('{:,}'.format(intTotalOffBudget))
strTotalLiabilities = ('{:,}'.format(intMortgage))
str5YearVacationCurrent = ('{:,}'.format(int5YearVacationCurrent))

strGrossPay = ('{:,}'.format(intGrossPay))
strNetPay = ('{:,}'.format(intNetPay))
strTotalTaxes = ('{:,}'.format(intTotalTaxes))
strDeductionsTSP = ('{:,}'.format(intDeductionsTSP))
strTotalPayInsurance = ('{:,}'.format(intTotalPayInsurance))
################################
# Calculate Budget Percentages #
################################
intHousingPerc = (intBudgetHousing / intNetPay) * 100
intHousingPerc = round(intHousingPerc, 1)
intUtilitiesPerc = (intBudgetUtilities / intNetPay) * 100
intUtilitiesPerc = round(intUtilitiesPerc, 1)
intTransportationPerc = (intBudgetTransportation / intNetPay) * 100
intTransportationPerc = round(intTransportationPerc, 1)
intFoodPerc = (intBudgetFood / intNetPay) * 100
intFoodPerc = round(intFoodPerc, 1)
intGivingPerc = (intBudgetGiving / intNetPay) * 100
intGivingPerc = round(intGivingPerc, 1)
intEntertainmentPerc = (intBudgetEntertainmentTotal / intNetPay) * 100
intEntertainmentPerc = round(intEntertainmentPerc, 1)
intSpendingAccountsPerc = (intBudgetSpendingAccounts / intNetPay) * 100
intSpendingAccountsPerc = round(intSpendingAccountsPerc, 1)
intSavingsPerc = (intBudgetSavings / intNetPay) * 100
intSavingsPerc = round(intSavingsPerc, 1)
intTaxesPerc = (intBudgetTaxes / intNetPay) * 100
intTaxesPerc = round(intTaxesPerc, 1)
intTotalBudgetPerc = intHousingPerc + intUtilitiesPerc + intTransportationPerc + intFoodPerc + intGivingPerc + intEntertainmentPerc + intSpendingAccountsPerc + intSavingsPerc + intTaxesPerc
intTotalBudgetPerc = round(intTotalBudgetPerc, 1)

################
# Export Latex #
################


with open("report.tex", "w") as latex:
    latex.write("\documentclass[11pt]{article}\n")
    latex.write("\\usepackage{fontspec}\n")
    latex.write("\\setmainfont{Fira Sans}\n")
    latex.write("\\usepackage[margin=0.5in]{geometry}\n")
    latex.write("\\usepackage{parskip}\n")
    latex.write("\\usepackage{float} % This allows the H option in table formatting\n")
    latex.write("\\usepackage{tikz}\n")
    latex.write("\\usetikzlibrary{arrows}\n")
    latex.write("\\usepackage{multicol}\n")
    latex.write("\\usepackage{multirow}\n")
    latex.write("\\usepackage{paracol}\n")
    latex.write("\n")
    latex.write("\\usepackage{pgfplots}\n")
    latex.write("\\usepackage{pgfplotstable}\n")
    latex.write("\\pgfplotsset{compat=1.18}\n")
    latex.write("\\usepgfplotslibrary{fillbetween}\n")
    latex.write("\n")
    latex.write("\\definecolor{blue}{HTML}{268bd2}\n")
    latex.write("\\definecolor{green}{HTML}{859900}\n")
    latex.write("\\definecolor{accent}{HTML}{073642}\n")
    latex.write("\\definecolor{yellow}{HTML}{b58900}\n")
    latex.write("\\definecolor{red}{HTML}{dc322f}\n")
    latex.write("\n")
    latex.write("%This is for the pie charts\n")
    latex.write("\\tikzset{\n")
    latex.write("  chart/.style={\n")
    latex.write("    legend label/.style={font={\scriptsize},anchor=west,align=left},\n")
    latex.write("    legend box/.style={rectangle, draw, minimum size=5pt},\n")
    latex.write("    axis/.style={black,semithick,->},\n")
    latex.write("    axis label/.style={anchor=east,font={\\tiny}},\n")
    latex.write("  },\n")
    latex.write("  pie chart/.style={\n")
    latex.write("    chart,\n")
    latex.write("    slice/.style={line cap=round, line join=round, very thick,draw=white},\n")
    latex.write("    pie title/.style={font={\\bfseries}},\n")
    latex.write("    slice type/.style 2 args={\n")
    latex.write("        ##1/.style={fill=##2},\n")
    latex.write("        values of ##1/.style={}\n")
    latex.write("    }\n")
    latex.write("  }\n")
    latex.write("}\n")
    latex.write("\n")
    latex.write("\\pgfdeclarelayer{background}\n")
    latex.write("\\pgfdeclarelayer{foreground}\n")
    latex.write("\\pgfsetlayers{background,main,foreground}\n")
    latex.write("\n")
    latex.write("\\newcommand{\pie}[3][]{\n")
    latex.write("    \\begin{scope}[#1]\n")
    latex.write("    \\pgfmathsetmacro{\\curA}{90}\n")
    latex.write("    \\pgfmathsetmacro{\\radius}{1}\n")
    latex.write("    \\def\Centre{(0,0)}\n")
    latex.write("    \\node[pie title] at (90:1.3) {#2};\n")
    latex.write("    \\foreach \\v/\\s in{#3}{\n")
    latex.write("        \\pgfmathsetmacro{\deltaA}{\\v/100*360}\n")
    latex.write("        \\pgfmathsetmacro{\\nextA}{\\curA + \\deltaA}\n")
    latex.write("        \\pgfmathsetmacro{\\midA}{(\\curA+\\nextA)/2}\n")
    latex.write("\n")
    latex.write("        \\path[slice,\\s] \\Centre\n")
    latex.write("            -- +(\\curA:\\radius)\n")
    latex.write("            arc (\\curA:\\nextA:\\radius)\n")
    latex.write("            -- cycle;\n")
    latex.write("   % to determine direction of lines (left/right, up/down\n")
    latex.write("   \\pgfmathsetmacro{\\ysign}{ifthenelse(mod(\\midA,360)<=180,1,-1)}\n")
    latex.write("   \\pgfmathsetmacro{\\xsign}{ifthenelse(mod(\\midA-90,360)<=180,-1,1)}\n")
    latex.write("\n")
    latex.write("   \\begin{pgfonlayer}{foreground}\n")
    latex.write("        \\draw[*-,thin] \\Centre ++(\midA:\\radius/2) -- \n")
    latex.write("                               ++(\\xsign*0.07*\\radius,\\ysign*0.2*\\radius) -- \n")
    latex.write("                               ++(\\xsign*\\radius,0) \n")
    latex.write("                      node[above,near end,pie values,values of \\s]{$\\v\\%$};\n")
    latex.write("   \\end{pgfonlayer}\n")
    latex.write("\n")
    latex.write("\n")
    latex.write("        \\global\\let\\curA\\nextA\n")
    latex.write("    }\n")
    latex.write("    \\end{scope}\n")
    latex.write("}\n")
    latex.write("\n")
    latex.write("\\newcommand{\\legend}[2][]{\n")
    latex.write("    \\begin{scope}[#1]\n")
    latex.write("    \\path\n")
    latex.write("        \\foreach \\n/\\s in {#2}\n")
    latex.write("            {\n")
    latex.write("                  ++(0,-10pt) node[\\s,legend box] {} +(5pt,0) node[legend label] {\\n}\n")
    latex.write("            }\n")
    latex.write("    ;\n")
    latex.write("    \\end{scope}\n")
    latex.write("}\n")
    latex.write("\n")
    latex.write("%% This is the end of the pie chart section\n")
    latex.write("\n")
    latex.write("% This is for the financial goals section\n")
    latex.write("\n")
    latex.write("\\newcommand{\DrawPercentageBar}[2]{%\n")
    latex.write("  \\begin{tikzpicture}\n")
    latex.write("    \\fill[color=blue] (#1*200pt, 0.0) rectangle (200pt, 10pt);\n")
    latex.write("    \\fill[color=red] (#2*200pt, 0.0) rectangle (#2*200pt+2pt, 10pt);\n")
    latex.write("    \\fill[color=accent]  (0.0 , 0.0) rectangle (#1*200pt , 10pt );\n")
    latex.write("  \\end{tikzpicture}%\n")
    latex.write("}\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%%%\n")
    latex.write("% PreAmble %\n")
    latex.write("%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("%\\title{My Family Financial Plan}\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%%%\n")
    latex.write("% Document %\n")
    latex.write("%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("\\begin{document}\n")
    latex.write("\n")
    latex.write("\\section*{The My Family Financial Plan}\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%\n")
    latex.write("% Values %\n")
    latex.write("%%%%%%%%%%\n")
    latex.write("\\begin{multicols}{2}\n")
    latex.write("\\raggedcolumns\n")
    latex.write("\\textbf{\Large Financial Values}\n")
    latex.write("\\begin{enumerate}\n")
    latex.write("        \\item\n")
    latex.write("                God Honoring Stewardship.  \\vspace{-5pt}\n")
    latex.write("                %{\small(1 Chronicles 29:14; Proverbs 3:9; 2 Corinthians 9:7)}  \\vspace{-5pt}\n")
    latex.write("        \\item\n")
    latex.write("                Financial Freedom.  \\vspace{-5pt}\n")
    latex.write("                %{\small(Matthew 6:24; Romans 13:7-8; Proverbs 22:7)}   \\vspace{-5pt}\n")
    latex.write("        \\item\n")
    latex.write("                Contentment.  \\vspace{-5pt}\n")
    latex.write("                %{\\small (Philippians 4:11 1 Timothy 6:9-10; Luke 12:15)} \n")
    latex.write("\\end{enumerate}\n")
    latex.write("\\columnbreak\n")
    latex.write("%%%%%%%%%%%%%%%%%%\n")
    latex.write("% Net Worth Graph %\n")
    latex.write("%%%%%%%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("\\textbf{\Large Net Worth} \\$" + str(strCurrentNWValue) + " \\\\\n")
    latex.write("\\begin{tikzpicture}\n")
    latex.write("\\begin{axis}[\n")
    latex.write("        width=3in,height=1.5in,\n")
    latex.write("        axis lines = left,\n")
    latex.write("        xtick = \\empty, ytick = \\empty,\n")
    latex.write("        %\\node [right] at (current axis.right of origin) {$year$};\n")
    latex.write("        %\\node [above] at (current axis.above origin) {$value$};\n")
    latex.write("        ]\n")
    latex.write("        \\path [name path=xaxis]\n")
    latex.write("                (\\pgfkeysvalueof{/pgfplots/xmin},0) --\n")
    latex.write("                (\\pgfkeysvalueof{/pgfplots/xmax},0);\n")
    latex.write("        \\addplot[color=green,  name path = assets] coordinates {\n")
    latex.write("                (0, " +str(int5YearAssets) +")\n")
    latex.write("                (1, " +str(int4YearAssets) + ")\n")
    latex.write("                (2, " +str(int3YearAssets) + ")\n")
    latex.write("                (3, " +str(int2YearAssets) + ")\n")
    latex.write("                (4, " +str(intCurrentAssets) + ")\n")
    latex.write("                };\n")
    latex.write("        \\addplot [green, opacity=0.8] fill between [of = assets and xaxis];\n")
    latex.write("        \\addplot[color=red, name path = liabilities] coordinates {\n")
    latex.write("                (0, " + str(int5YearLiabilities) + ")\n")
    latex.write("                (1, " + str(int5YearLiabilities) + ")\n")
    latex.write("                (2, " + str(int5YearLiabilities) + ")\n")
    latex.write("                (3, " + str(int5YearLiabilities) + ")\n")
    latex.write("                (4, " + str(intCurrentLiabilities) + ")\n")
    latex.write("                };\n")
    latex.write("        \\addplot [red, opacity=0.8] fill between [of = liabilities and xaxis];\n")
    latex.write("        \\addplot[color=accent, thick] coordinates {\n")
    latex.write("                (0, " +str(int5YearNWValue) + ")\n")
    latex.write("                (1, " +str(int4YearNWValue) + ")\n")
    latex.write("                (2, " +str(int3YearNWValue) + ")\n")
    latex.write("                (3, " +str(int2YearNWValue) + ")\n")
    latex.write("                (4, " +str(intCurrentNWValue) + ")\n")
    latex.write("                };\n")
    latex.write("\\end{axis}\n")
    latex.write("\\end{tikzpicture}\n")
    latex.write("\n")
    latex.write("\\end{multicols}\n")
    latex.write("\n")
    latex.write("\\vspace{-15pt}\n")
    latex.write("\\begin{center}\n")
    latex.write("        \\rule{5in}{1pt}\n")
    latex.write("\\end{center}\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("% Income Statement %\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("\\begin{multicols}{2}\n")
    latex.write("\n")
    latex.write("\\textbf{\\Large Cash Flow} \\\\\n")
    latex.write("Avg Monthly Income: \\$" + str(strAvgIncome) + " \\\\\n")
    latex.write("Avg Monthly Expenses: \\$" + str(strAvgTotalSpending) + " \\\\\n")
    latex.write("Avg Monthly Flow: {\\color{green} \\$" + str(strCashFlow) + " \\\\}\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("% Cash Flow Pie Chart %\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("{\\color{blue} \\textbf{Living}}, {\\color{yellow} \\textbf{Giving}}, {\\color{green} \\textbf{Growing}}, {\\color{red} \\textbf{Owing}}\n")
    latex.write("\\vspace{-5pt}\n")
    latex.write("\n")
    latex.write("\\begin{tikzpicture}\n")
    latex.write("[\n")
    latex.write("pie chart,\n")
    latex.write("slice type={giving}{yellow},\n")
    latex.write("slice type={living}{blue},\n")
    latex.write("slice type={growing}{green},\n")
    latex.write("slice type={owing}{red},\n")
    latex.write("slice type={taxes}{accent},\n")
    latex.write("pie values/.style={font={\\scriptsize}},\n")
    latex.write("scale=1.5\n")
    latex.write("]\n")
    latex.write("\pie{}{" + str(intGrowing) + "/growing," + str(intLiving) + "/living," + str(intGiving) + "/giving," + str(intOwing) + "/owing}\n")
    latex.write("\end{tikzpicture}\n")
    latex.write("\n")
    latex.write("\columnbreak\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%%%%%%%%%%\n")
    latex.write("% Financial Goals %\n")
    latex.write("%%%%%%%%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("\\textbf{\Large Financial Goals} \\\\\n")
    latex.write("\\vspace{-5pt}\n")
    latex.write("\n")
    latex.write("\\textbf{5 Year Big Vacation} \\$" + str(str5YearVacationCurrent) + "\\$20,000 \\\\\n")
    latex.write("\\DrawPercentageBar{" +str(int5YearVacationPerc) + "}{" +str(int5YearVacationPerc) + "}\n")
    latex.write("\n")
    latex.write("\\textbf{Child1' College Savings} \\$" + str(strChild1529) + "/\\$33,500 \\\\\n")
    latex.write("\\DrawPercentageBar{" +str(intChild1529Perc) + "}{" + str(intChild1529GoalPerc) + "}\n")
    latex.write("\n")
    latex.write("\\textbf{Child2's College Savings} \\$" + str(strChild2529) + "/\\$36,000 \\\\\n")
    latex.write("\\DrawPercentageBar{" +str(intChild2529Perc) + "}{" +str(intChild2529GoalPerc) + "}\n")
    latex.write("\n")
    latex.write("\\textbf{Child3's College Savings} \\$" + str(strChild3529) + "/\\$108,800 \\\\\n")
    latex.write("\\DrawPercentageBar{" +str(intChild3529Perc) + "}{" +str(intChild3529GoalPerc) + "}\n")
    latex.write("\n")
    latex.write("\\end{multicols}\n")
    latex.write("\n")
    latex.write("\n")
    latex.write("\\vspace{-15pt}\n")
    latex.write("\\begin{center}\n")
    latex.write("        \\rule{5in}{1pt}\n")
    latex.write("\\end{center}\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("% Assets and Liabilities %\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("\\columnratio{0.4}\n")
    latex.write("\\begin{paracol}{2}\n")
    latex.write("\n")
    latex.write("\\textbf{\\Large Assets}\n")
    latex.write("\n")
    latex.write("\\begin{table}[H]\n")
    latex.write("        \\begin{tabular}{l l}\n")
    latex.write("                \\multicolumn{1}{l} \\textbf{On Budget} \\\\\n")
    latex.write("                \\textbf{Account} &  \\textbf{Amount} \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                NFCU Savings Account & \\$" +str(strNFCUSavings1) + " \\\\\n")
    latex.write("                NFCU Savings Account & \\$" +str(strNFCUSavings2) + " \\\\\n")
    latex.write("                USAA Checking & \\$" + str(strJointChecking) + " \\\\\n")
    latex.write("                Ally Savings Account & \\$" + str(strAllySavings) + " \\\\\n")
    latex.write("                Vanguard Mutual Fund & \\$" + str(strVanguardBrokerage) + " \\\\\n")
    latex.write("                \\hline   \n")
    latex.write("                \\textbf{Total} & \\$" +str(strTotalonBudget) + " \\\\\n")
    latex.write("        \\end{tabular}\n")
    latex.write("\\end{table}\n")
    latex.write("\\vspace{-20pt}\n")
    latex.write("\\begin{table}[H]\n")
    latex.write("        \\begin{tabular}{l l}\n")
    latex.write("                \\multicolumn{1}{l} \\textbf{Off Budget} \\\\\n")
    latex.write("                \\textbf{Account} &  \\textbf{Amount} \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                House Zestimate & \\$" + str(strHouseValue) + " \\\\\n")
    latex.write("                TSP & \\$" + str(strTSP) + " \\\\\n")
    latex.write("                Vanguard Roth IRA & \\$" + str(strVanguardIRA) + " \\\\\n")
    latex.write("                Child1' 529 Account & \\$" + str(strChild1529) + " \\\\\n")
    latex.write("                Child2's 529 Account & \\$" + str(strChild2529) + " \\\\\n")
    latex.write("                Child3's 529 account & \\$" + str(strChild3529) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Total} & \\$" + str(strTotalOffBudget) + " \\\\\n")
    latex.write("        \\end{tabular}\n")
    latex.write("\\end{table}\n")
    latex.write("\n")
    latex.write("\\vspace{-10pt}\n")
    latex.write("\\textbf{\\Large Liabilities}\n")
    latex.write("\n")
    latex.write("\\begin{table}[H]\n")
    latex.write("        \\begin{tabular}{l l}\n")
    latex.write("                \\textbf{Account} &  \\textbf{Amount} \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                NFCU Mortgage & \\$" + str(strMortgage) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Total} & \\$" + str(strTotalLiabilities) + " \\\\\n")
    latex.write("        \\end{tabular}\n")
    latex.write("\\end{table}\n")
    latex.write("\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("% Financial Ratios %\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("\\switchcolumn\n")
    latex.write("\n")
    latex.write("\\begin{center}\n")
    latex.write("\\textbf{\\Large Financial Ratios}\n")
    latex.write("\\end{center}\n")
    latex.write("\n")
    latex.write("\\begin{table}[H]\n")
    latex.write("        \\begin{tabular}{c c c}\n")
    latex.write("                {\\color{" +str(colorEmergencyFundRatio) + "} {\\Huge " +str(intEmergencyFundRatio) + "x}} & {\\color{" +str(colorNetworthRatio) + "} {\\Huge " +str(intTargetNetworthRatio) + "\\%}} & {\\color{" + str(colorHouseEquity) + "} {\\Huge " +str(intHouseEquity) + "\\%}}  \\\\\n")
    latex.write("                Emergency Fund & Target Net Worth Ratio & House Equity \\\\\n")
    latex.write("                \\\\\n")
    latex.write("                {\\color{" + str(colorDebtAssetRatio) + "} {\\Huge " +str(intDebtAssetRatio) + "\\%}} & {\\color{" + str(colorDebtIncomeRatio) + "} {\\Huge " +str(intDebtIncomeRatio) + "\\%}} & {\\color{" + str(colorHouseIncomeRatio) + "} {\\Huge " +str(intHouseIncomeRatio) + "\\%}} \\\\\n")
    latex.write("                Debt:Asset & Total Debt:Income & Housing:Income\\\\\n")
    latex.write("                \\\\\n")
    latex.write("                {\\color{" + str(colorSavingsRatio) + "} {\\Huge " +str(intSavingsRatio) + "\\%}} & {\\Huge " +str(intInvestmentRatio) + "\\%} & {\\Huge " +str(intRetirementRatio) + "\\%} \\\\\n")
    latex.write("                Savings Ratio & Investments Ratio & Retirement Ratio\\\\\n")
    latex.write("        \\end{tabular}\n")
    latex.write("\\end{table}\n")
    latex.write("\n")
    latex.write("% Money Ratios Math\n")
    latex.write("% Emergency Fund = Emergency Fund / Monthly Expenses (remove savings and givings) // 3x is base, 6x is good\n")
    latex.write("% Target Net Worth Ratio = Age x (Pre-Tax Salary / 10)\n")
    latex.write("% Solvency Ratio = Networth / Total Liabilities // Answer the question, could you \n")
    latex.write("% Debt:Assets Ratio = Total Liabilities / Total Assets // 10% is a great goal, <50% is good\n")
    latex.write("% Total Debt:Income Ratio = (Annual Debt Payments / Gross Income) x 100  // it should never be over 36%\n")
    latex.write("% Mortgage:Income Ratio = Monthly Housing Cost / Gross Income // <28% is desireable; include mortgage payment, HOA and housing maintenance\n")
    latex.write("% Savings Ratio = Savings / Gross Income  // 10% - 20% is great\n")
    latex.write("% Investment Ratio : Total Assets Ratio = Investment Assets / Total Assets\n")
    latex.write("% Retirement Ratio : (Retirement Savings) / (25 x Annual Income) / // Measure how close you are to retirement goals\n")
    latex.write("\n")
    latex.write("\\rule{4in}{1pt} \\\\\n")
    latex.write("\\rule{0in}{5pt} \\\\\n")
    latex.write("\\rule{4in}{1pt} \\\\\n")
    latex.write("\\rule{0in}{5pt} \\\\\n")
    latex.write("\\rule{4in}{1pt} \\\\\n")
    latex.write("\\rule{0in}{5pt} \\\\\n")
    latex.write("\\rule{4in}{1pt} \\\\\n")
    latex.write("\\rule{0in}{5pt} \\\\\n")
    latex.write("\\rule{4in}{1pt} \\\\\n")
    latex.write("\\rule{0in}{5pt} \\\\\n")
    latex.write("\\rule{4in}{1pt} \\\\\n")
    latex.write("\n")
    latex.write("\\end{paracol}\n")
    latex.write("\n")
    latex.write("\\pagebreak\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("% Budget Breakdown and Analysis %\n")
    latex.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    latex.write("\n")
    latex.write("\\begin{table}[H]\n")
    latex.write("        \\begin{tabular}{l l l l}\n")
    latex.write("                \\multicolumn{4}{c}{\\textbf{\\Large Budget Analysis}} \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\hline\n")
    latex.write("                \\multicolumn{4}{c}{\\textbf{Income}} \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Category} & & \\textbf{Expected} & \\textbf{Actual} \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Combined Pay & & \\$" + str(strGrossPay) + " \\\\\n")
    latex.write("                Combined Taxes & & -\\$" + str(strTotalTaxes) + " \\\\\n")
    latex.write("                Combined Insurance & & -\\$" + str(strTotalPayInsurance) + " \\\\\n")
    latex.write("                Roth TSP & & -\\$" + str(strDeductionsTSP) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Monthly Net Income} & & \\$" + str(strNetPay) + " & \\$" + str(strAvgIncome) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\hline\n")
    latex.write("                \\multicolumn{4}{c}{\\textbf{Expenses}} \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Budget Category} & \\textbf{\\%} & \\textbf{Budget} & \\textbf{Avg Spent} \\\\\n")
    latex.write("                \\hline \n")
    latex.write("                \\textbf{Housing} & " + str(intHousingPerc) + "\\% & \\$" + str(strBudgetHousing) + " & \\$" + str(strAvgHousing) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Mortage & & \\$" + str(strBudgetMortgage) + " & \\$" + str(strAvgMortgage) + " \\\\\n")
    latex.write("                HOA & & \\$" + str(strBudgetHOA) + " & \\$" + str(strAvgHOA) + " \\\\\n")
    latex.write("                House Maintenance & & \\$" + str(strBudgetHousingMaint) + " & \\$" + str(strAvgHousingMaint) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Utilities} & " + str(intUtilitiesPerc) + "\\% & \\$" + str(strBudgetUtilities) + " & \\$" + str(strAvgUtilities) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Electricity & & \\$" + str(strBudgetElectricity) + " & \\$" + str(strAvgElectricity) + "  \\\\\n")
    latex.write("                Water & & \\$" + str(strBudgetWater) + " & \\$" + str(strAvgWater) + " \\\\\n")
    latex.write("                Trash & & \\$" + str(strBudgetTrash) + " & \\$" + str(strAvgTrash) + " \\\\\n")
    latex.write("                Internet & & \\$" + str(strBudgetInternet) + " & \\$" + str(strAvgInternet) + " \\\\\n")
    latex.write("                TV & & \\$" + str(strBudgetTV) + " & \\$" + str(strAvgTV) + " \\\\\n")
    latex.write("                Phone & & \\$" + str(strBudgetPhone) + " & \\$" + str(strAvgPhone) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Transportation} & " + str(intTransportationPerc) + "\\% & \\$" + str(strBudgetTransportation) + " & \\$" + str(strAvgTransportation) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Gas & & \\$" + str(strBudgetGas) + " & \\$" + str(strAvgGas) + " \\\\\n")
    latex.write("                Insurance & & \\$" + str(strBudgetInsurance) + " & \\$" + str(strAvgInsurance) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Food} & " + str(intFoodPerc) + "\\% & \\$" + str(strBudgetFood) + " & \\$" + str(strAvgFood) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Groceries & & \\$" + str(strBudgetGroceries) + " & \\$" + str(strAvgGroceries) + " \\\\\n")
    latex.write("                Restaurants & & \\$" + str(strBudgetRestaurants) + " & \\$" + str(strAvgRestaurants) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Entertainment} & " + str(intEntertainmentPerc) + "\\% & \\$" + str(strBudgetEntertainment) + " & \\$" + str(strAvgEntertainment) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Entertainment & & \\$" + str(strBudgetEntertainment) + " & \\$" + str(strAvgEntertainment) + " \\\\\n")
    latex.write("                Date Night & & \\$" + str(strBudgetDateNight) + " & \\$" + str(strAvgDateNight) + " \\\\\n")
    latex.write("                Vacation & & \\$" + str(strBudgetVacation) + " & \\$" + str(strAvgVacation) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Spending Accounts} & " + str(intSpendingAccountsPerc) + "\\% & \\$" + str(strBudgetSpendingAccounts) + " & \\$" + str(strAvgSpendingAccounts) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Joint Spending & & \\$" + str(strBudgetJoint) + " & \\$" + str(strAvgJoint) + " \\\\\n")
    latex.write("                Spending1's Spending & & \\$" + str(strBudgetSpending1) + " & \\$" + str(strAvgSpending1) + " \\\\\n")
    latex.write("                Spending2's Spending & & \\$" + str(strBudgetSpending2) + " & \\$" + str(strAvgSpending2) + " \\\\\n")
    latex.write("                Kids' Spending & & \\$" + str(strBudgetKids) + " & \\$" + str(strAvgKids) + " \\\\\n")
    latex.write("                Gifts & & \\$" + str(strBudgetGifts) + " & \\$" + str(strAvgGifts) + " \\\\\n")
    latex.write("                Professional & & \\$" + str(strBudgetProfessional) + " & \\$" + str(strAvgGifts) + " \\\\\n")
    latex.write("                School & & \\$" + str(strBudgetSchool) + " & \\$" + str(strAvgSchool) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Giving} & " + str(intGivingPerc) + "\\% & \\$" + str(strBudgetGiving) + " & \\$" + str(strAvgGiving) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Tithe & & \\$" + str(strBudgetTithe) + " & \\$" + str(strAvgTithe) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Saving} & " + str(intSavingsPerc) + "\\% & \\$" + str(strBudgetSavings) + " & \\$" + str(strAvgSavings) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                General Savings & & \\$" + str(strBudgetSavings) + " & \\$" + str(strAvgSavings) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Taxes} & " + str(intTaxesPerc) + "\\% & \\$" + str(strBudgetTaxes) + " & \\$" + str(strAvgTaxes) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                Car Registration & & \\$" + str(strBudgetCarRegistration) + " & \\$" + str(strAvgCarRegistration) + " \\\\\n")
    latex.write("                \\hline\n")
    latex.write("                \\textbf{Total Monthly Expenses} & " + str(intTotalBudgetPerc) + "\\% & \\$" + str(strBudgetTotalSpending) + " & \\$" + str(strAvgTotalSpending) + "  \\\\\n")
    latex.write("        \\end{tabular}\n")
    latex.write("\\end{table}\n")
    latex.write("\n")
    latex.write("\n")
    latex.write("\\input{guide}\n")
    latex.write("\n")
    latex.write("\n")
    latex.write("\n")
    latex.write("%%%%%%%\n")
    latex.write("% END %\n")
    latex.write("%%%%%%%\n")
    latex.write("\n")
    latex.write("\\end{document}\n")
    latex.close()

os.system("xelatex -interaction=\"batchmode\" report.tex")
