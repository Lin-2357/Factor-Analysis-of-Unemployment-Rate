x = """Men White All Origins 16 to 24 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04024891

Men White All Origins 25 to 34 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000230

Men White All Origins 35 to 44 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000237

Men White All Origins 45 to 54 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000244

Women White All Origins 16 to 24 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04024892

Women White All Origins 25 to 34 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000385

Women White All Origins 35 to 44 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000392

Women White All Origins 45 to 54 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000399

Men Black or African American All Origins 16 to 24 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04024930

Men Black or African American All Origins 25 to 34 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04015832

Men Black or African American All Origins 35 to 44 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04015839

Men Black or African American All Origins 45 to 54 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04015845

Women Black or African American All Origins 16 to 24 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04024905

Women Black or African American All Origins 25 to 34 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000457

Women Black or African American All Origins 35 to 44 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000459

Women Black or African American All Origins 45 to 54 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04000461

Men Asian All Origins 16 to 24 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04079032

Men Asian All Origins 25 to 34 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04034989

Men Asian All Origins 35 to 44 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04034990

Men Asian All Origins 45 to 54 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04034991

Men Asian All Origins 55 years and over All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04032336

Women Asian All Origins 16 to 24 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04079033

Women Asian All Origins 25 to 34 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04034996

Women Asian All Origins 35 to 44 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04034997

Women Asian All Origins 45 to 54 years All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04034998

Women Asian All Origins 55 years and over All educational levels N/A Unemployment rate Not Seasonally Adjusted Monthly : LNU04032377"""

y = x.split("\n\n")
z = [y0.split(" ") for y0 in y]
w = [[z0[0], z0[1], z0[z0.index('Origins')+1], z0[z0.index(':')-1], z0[z0.index(':')+1]] for z0 in z]
print(w)
