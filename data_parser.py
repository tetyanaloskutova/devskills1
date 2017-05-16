import pandas

filename_easy = "dsbase-easy.csv"
filename_medium = "dsbase-medium.csv"
filename_hard = "dsbase-hard.csv"

# Read the 'easy' file
df = pandas.read_csv(filename_easy)
print("Read easy file")
print(df.values)
print(list(df))


# Read the 'medium' file
df = pandas.read_csv(filename_medium, lineterminator='#', delimiter='|' )
print("Read medium file")
print(df.values)
print(list(df))


# Read the 'hard' file
df = pandas.read_csv(filename_hard, lineterminator='#', delimiter='|' )
print("Read hard file")
print(df.values)
# the header has an extra column
print(len(df[df.SPEND.notnull()])) # this is 0, so the only row with 6 columns is the header
# reread the data without the header
df = pandas.read_csv(filename_hard, lineterminator='#', delimiter='|', skiprows = 1, header = None, names=['CID','GENDER','AGE','SPEND'])
print(df.values)
print(list(df))

print("Are there any nulls in the data?")
print(df.isnull()) # Many nulls, will fix by column

print("Testing CID column")
print(df['CID'].head(10)) # type is int64, so it seems to be right
df[df.CID.isnull()] # no nulls here
# are there any duplicates?
ids = df['CID']
df[ids.isin(ids[ids.duplicated()])].sort_values(by='CID')

print("Testing SPEND column")
print(df['SPEND'].head(10)) #type float63, so no wrong character values
df[df.SPEND.isnull()] # a few rows with nulls. I replace with 0, another solution can be to reject the rows. The solution would depend on a particular need
df['SPEND'].fillna(0, inplace=True)
print(df[df.SPEND.isnull()])

print("Testing AGE column")
print(df['AGE'].head(10)) #type int64, so no wrong character values
print(df[df.AGE.isnull()] ) #no nulls
# if age is more than 120, probably, that's an error. Again, I replace with 0, but another solution may be necessary depending on the needs
df.ix[df.AGE > 120, 'AGE'] = 0

print("Testing GENDER column")
print(df['GENDER'].head(10)) # type object, need to check if gender is only M or F. If not, replace with N for 'Not known'
df['GENDER'].fillna(0, inplace=True) # this seems to be unnecessary in python but in other languages may be necessary to get rid of nulls before comparing characters
df['GENDER'] = df['GENDER'].apply(lambda x: 'N' if (x != 'M' and x != 'F') else x)

print("A view on the fixed dataset")

print(df.head(10))
# I did not find the name of any Asian country because there seem to be only charachers for SUDAN and OMAN but they are not in order