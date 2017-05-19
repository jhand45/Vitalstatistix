import quandl
import pandas as pd
import numpy as np
import matplotlib as plt

######################################################################################################
#                    Vitalstatistix                                                                  #
#  - Performs basic statistical analysis of gross data as well as monthly and annualised changes     #
#  - Assumes that data input is monthly data                                                         #
#                                                                                                    #
######################################################################################################



data = #insert monthly dataset here


period = data.pct_change()
period = period.replace([np.inf, -np.inf], np.nan)
period = period.dropna()
annual = data.pct_change(periods=13)
period = period.reset_index()
annual = annual.reset_index()


grossmean = round(np.mean(data),1)
grossSD = round(np.std(data),4)
FirstPosGros = (round(grossmean + grossSD, 1))
SecondPosGros = (round(grossmean + (2 * grossSD),1))
ThirdPosGros = (round(grossmean + (3 * grossSD),1))
FirstNegGros = (round(grossmean - grossSD,1))
SecondNegGros = (round(grossmean - (2 * grossSD),1))
ThirdNegGros = (round(grossmean - (3 * grossSD),1))
grosshigh = np.nanmax(np.isfinite(data))
grosslow = np.nanmin(np.isfinite(data))


periodmean = round(np.mean(period) * 100,4)
periodmean = periodmean.iloc[-1]
periodSD = round(np.std(period) * 100,4)
periodSD = periodSD.iloc[-1]
FirstPosPOP = round(periodmean + periodSD, 4)
SecondPosPOP = round(periodmean + (2 * periodSD),4)
ThirdPosPOP = round(periodmean + (3 * periodSD),4)
FirstNegPOP = round(periodmean - periodSD,4)
SeconNegPOP = round(periodmean - (2 * periodSD),4)
ThirdNegPop = round(periodmean - (3 * periodSD),4)
periodhigh = np.amax(period)
periodlow = np.amin(period)
periodhigh = round(periodhigh.iloc[-1] * 100,4)
periodlow = round(periodlow.iloc[-1] * 100,4)

annualmean = round(np.mean(annual) * 100,4)
annualmean = annualmean.iloc[-1]
annualSD = round(np.std(annual) * 100,4)
annualSD = annualSD.iloc[-1]
FirstPosAn = round(annualmean + annualSD, 4)
SecondPosAn = round(annualmean + (2 * annualSD),4)
ThirdPosAn = round(annualmean + (3 * annualSD),4)
FirstNegAn = round(annualmean - annualSD,4)
SeconNegAn = round(annualmean - (2 * annualSD),4)
ThirdNegAn = round(annualmean - (3 * annualSD),4)
anhigh = np.amax(annual)
anlow = np.amin(annual)
anhigh =round(anhigh.iloc[-1] * 100,4)
anlow =round(anlow.iloc[-1] * 100,4)


print("Gross mean is {}".format(grossmean))
print("Gross Standard Deviation is {}".format(grossSD))
print("First Positive SD is {}".format(FirstPosGros))
print("Second Positive SD is {}".format(SecondPosGros))
print("Third Positive SD is {}".format(ThirdPosGros))
print("First Negative SD is {}".format(FirstNegGros))
print("Second Negative SD is {}".format(SecondNegGros))
print("Third Negative SD is {}".format(ThirdNegGros))
print("Gross maximum is {}".format(periodhigh))
print("Gross minimum is {}".format(periodlow))
print("")
print("Period on period mean is {}%".format(periodmean))
print("Period Standard Deviation is {}".format(periodSD))
print("First Positive SD is {}".format(FirstPosPOP))
print("Second Positive SD is {}".format(SecondPosPOP))
print("Third Positive SD is {}".format(ThirdPosPOP))
print("First Negative SD is {}".format(FirstNegPOP))
print("Second Negative SD is {}".format(SeconNegPOP))
print("Third Negative SD is {}".format(ThirdNegPop))
print("Period on period maximum is {}%".format(periodhigh))
print("Period on period minimum is {}%".format(periodlow))
print("")
print("Annualized mean is {}%".format(annualmean))
print("Annualized Standard Deviation is {}".format(annualSD))
print("First Positive SD is {}".format(FirstPosAn))
print("Second Positive SD is {}".format(SecondPosAn))
print("Third Positive SD is {}".format(ThirdPosAn))
print("First Negative SD is {}".format(FirstNegAn))
print("Second Negative SD is {}".format(SeconNegAn))
print("Third Negative SD is {}".format(ThirdNegAn))
print("The annualized maximum is {}%".format(anhigh))
print("The annualized minimum is {}%".format(anlow))
