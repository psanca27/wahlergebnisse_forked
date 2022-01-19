import pandas as pd
import numpy as np
import seaborn as sns

#load dataset
df = pd.read_json('./wahlergebnisse.json')

#select states after 1990 and drop some cols
df = df.drop(['title', 'url', 'kind'], axis=1)
drop_t = ['BRD', 'Europawahl', 'Württemberg-Hohenzollern', 'DDR', 'Deutschland']
df = df[~df['territory'].isin(drop_t)]
df = df.loc[(df.date > '1990') & (df.date < '2014')]
df.reset_index(drop=True, inplace=True)

#date shocks
first_pisa_shock = pd.to_datetime('2001-12-04')
second_pisa_shock = pd.to_datetime('2002-06-26')

df['after_pisa_shock'] = 'no'
df.loc[df['date'] > first_pisa_shock, 'after_pisa_shock'] = 'yes'

#tag last election before shock
df['election_before_ps'] = 'no'
df.loc[(df.territory == 'Berlin') & (df.date == '2001-10-21'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Bremen') & (df.date == '1999-06-06'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Hamburg') & (df.date == '2001-09-23'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Baden-Württemberg') & (df.date == '2001-03-25'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Bayern') & (df.date == '1998-09-13'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Brandenburg') & (df.date == '1999-09-05'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Hessen') & (df.date == '1999-02-07'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Mecklenburg-Vorpommern') & (df.date == '1998-09-27'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Niedersachsen') & (df.date == '1998-03-01'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Nordrhein-Westfalen') & (df.date == '2000-05-14'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Rheinland-Pfalz') & (df.date == '2001-03-25'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Saarland') & (df.date == '1999-09-05'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Sachsen') & (df.date == '1999-09-19'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Sachsen-Anhalt') & (df.date == '1998-04-26'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Schleswig-Holstein') & (df.date == '2000-02-27'), 'election_before_ps'] = 'yes'
df.loc[(df.territory == 'Thüringen') & (df.date == '1999-09-12'), 'election_before_ps'] = 'yes'

#tag first election after shock
df['election_after_ps'] = df['election_before_ps'].shift(1)
df.loc[0, 'election_after_ps'] = 'no'

#add state acronyms
df['state'] = 'no'
df.loc[(df.territory == 'Berlin'), 'state'] = 'BE'
df.loc[(df.territory == 'Bremen'), 'state'] = 'HB'
df.loc[(df.territory == 'Hamburg'), 'state'] = 'HH'
df.loc[(df.territory == 'Baden-Württemberg'), 'state'] = 'BW'
df.loc[(df.territory == 'Bayern'), 'state'] = 'BY'
df.loc[(df.territory == 'Brandenburg'), 'state'] = 'BB'
df.loc[(df.territory == 'Hessen'), 'state'] = 'HE'
df.loc[(df.territory == 'Mecklenburg-Vorpommern'), 'state'] = 'MV'
df.loc[(df.territory == 'Niedersachsen'), 'state'] = 'NI'
df.loc[(df.territory == 'Nordrhein-Westfalen'), 'state'] = 'NW'
df.loc[(df.territory == 'Rheinland-Pfalz'), 'state'] = 'RP'
df.loc[(df.territory == 'Saarland'), 'state'] = 'SL'
df.loc[(df.territory == 'Sachsen'), 'state'] = 'SN'
df.loc[(df.territory == 'Sachsen-Anhalt'), 'state'] = 'ST'
df.loc[(df.territory == 'Schleswig-Holstein'), 'state'] = 'SH'
df.loc[(df.territory == 'Thüringen'), 'state'] = 'TH'

#add reading scores in 2000
df['pisa_reading_score'] = np.nan
df.loc[(df.territory == 'Bremen'), 'pisa_reading_score'] = 448
df.loc[(df.territory == 'Baden-Württemberg'), 'pisa_reading_score'] = 500
df.loc[(df.territory == 'Bayern'), 'pisa_reading_score'] = 510
df.loc[(df.territory == 'Brandenburg'), 'pisa_reading_score'] = 459
df.loc[(df.territory == 'Hessen'), 'pisa_reading_score'] = 476
df.loc[(df.territory == 'Mecklenburg-Vorpommern'), 'pisa_reading_score'] = 467
df.loc[(df.territory == 'Niedersachsen'), 'pisa_reading_score'] = 474
df.loc[(df.territory == 'Nordrhein-Westfalen'), 'pisa_reading_score'] = 482
df.loc[(df.territory == 'Rheinland-Pfalz'), 'pisa_reading_score'] = 485
df.loc[(df.territory == 'Saarland'), 'pisa_reading_score'] = 484
df.loc[(df.territory == 'Sachsen'), 'pisa_reading_score'] = 491
df.loc[(df.territory == 'Sachsen-Anhalt'), 'pisa_reading_score'] = 455
df.loc[(df.territory == 'Schleswig-Holstein'), 'pisa_reading_score'] = 478
df.loc[(df.territory == 'Thüringen'), 'pisa_reading_score'] = 482

#add wahlperiode
df['wp'] = np.nan

df.loc[(df.state =='BE') & (df.date == '1990-12-02'), 'wp'] = 12
df.loc[(df.state =='BE') & (df.date == '1995-10-22'), 'wp'] = 13
df.loc[(df.state =='BE') & (df.date == '1999-10-10'), 'wp'] = 14
df.loc[(df.state =='BE') & (df.date == '2001-10-21'), 'wp'] = 15
df.loc[(df.state =='BE') & (df.date == '2006-09-17'), 'wp'] = 16
df.loc[(df.state =='BE') & (df.date == '2011-09-18'), 'wp'] = 17

df.loc[(df.state =='HB') & (df.date == '1991-09-29'), 'wp'] = 13
df.loc[(df.state =='HB') & (df.date == '1995-05-14'), 'wp'] = 14
df.loc[(df.state =='HB') & (df.date == '1999-06-06'), 'wp'] = 15
df.loc[(df.state =='HB') & (df.date == '2003-05-25'), 'wp'] = 16
df.loc[(df.state =='HB') & (df.date == '2007-05-13'), 'wp'] = 17
df.loc[(df.state =='HB') & (df.date == '2011-05-22'), 'wp'] = 18

df.loc[(df.state =='HH') & (df.date == '1991-06-02'), 'wp'] = 14
df.loc[(df.state =='HH') & (df.date == '1993-09-19'), 'wp'] = 15
df.loc[(df.state =='HH') & (df.date == '1997-09-21'), 'wp'] = 16
df.loc[(df.state =='HH') & (df.date == '2001-09-23'), 'wp'] = 17
df.loc[(df.state =='HH') & (df.date == '2004-02-29'), 'wp'] = 18
df.loc[(df.state =='HH') & (df.date == '2008-02-24'), 'wp'] = 19
df.loc[(df.state =='HH') & (df.date == '2011-02-20'), 'wp'] = 20

df.loc[(df.state =='BW') & (df.date == '1992-04-05'), 'wp'] = 11
df.loc[(df.state =='BW') & (df.date == '1996-03-24'), 'wp'] = 12
df.loc[(df.state =='BW') & (df.date == '2001-03-25'), 'wp'] = 13
df.loc[(df.state =='BW') & (df.date == '2006-03-26'), 'wp'] = 14
df.loc[(df.state =='BW') & (df.date == '2011-03-27'), 'wp'] = 15

df.loc[(df.state =='BY') & (df.date == '1990-10-14'), 'wp'] = 12
df.loc[(df.state =='BY') & (df.date == '1994-09-25'), 'wp'] = 13
df.loc[(df.state =='BY') & (df.date == '1998-09-13'), 'wp'] = 14
df.loc[(df.state =='BY') & (df.date == '2003-09-21'), 'wp'] = 15
df.loc[(df.state =='BY') & (df.date == '2008-09-28'), 'wp'] = 16
df.loc[(df.state =='BY') & (df.date == '2013-09-15'), 'wp'] = 17

df.loc[(df.state =='BB') & (df.date == '1990-10-14'), 'wp'] = 1
df.loc[(df.state =='BB') & (df.date == '1994-09-11'), 'wp'] = 2
df.loc[(df.state =='BB') & (df.date == '1999-09-05'), 'wp'] = 3
df.loc[(df.state =='BB') & (df.date == '2004-09-19'), 'wp'] = 4
df.loc[(df.state =='BB') & (df.date == '2009-09-27'), 'wp'] = 5

df.loc[(df.state =='HE') & (df.date == '1991-01-20'), 'wp'] = 13
df.loc[(df.state =='HE') & (df.date == '1995-02-19'), 'wp'] = 14
df.loc[(df.state =='HE') & (df.date == '1999-02-07'), 'wp'] = 15
df.loc[(df.state =='HE') & (df.date == '2003-02-02'), 'wp'] = 16
df.loc[(df.state =='HE') & (df.date == '2008-01-27'), 'wp'] = 17
df.loc[(df.state =='HE') & (df.date == '2009-01-18'), 'wp'] = 18
df.loc[(df.state =='HE') & (df.date == '2013-09-22'), 'wp'] = 19

df.loc[(df.state =='MV') & (df.date == '1990-10-14'), 'wp'] = 1
df.loc[(df.state =='MV') & (df.date == '1994-10-16'), 'wp'] = 2
df.loc[(df.state =='MV') & (df.date == '1998-09-27'), 'wp'] = 3
df.loc[(df.state =='MV') & (df.date == '2002-09-22'), 'wp'] = 4
df.loc[(df.state =='MV') & (df.date == '2006-09-17'), 'wp'] = 5
df.loc[(df.state =='MV') & (df.date == '2011-09-04'), 'wp'] = 6

df.loc[(df.state =='NI') & (df.date == '1990-05-13'), 'wp'] = 12
df.loc[(df.state =='NI') & (df.date == '1994-03-13'), 'wp'] = 13
df.loc[(df.state =='NI') & (df.date == '1998-03-01'), 'wp'] = 14
df.loc[(df.state =='NI') & (df.date == '2003-02-02'), 'wp'] = 15
df.loc[(df.state =='NI') & (df.date == '2008-01-27'), 'wp'] = 16
df.loc[(df.state =='NI') & (df.date == '2013-01-20'), 'wp'] = 17

df.loc[(df.state =='NW') & (df.date == '1990-05-13'), 'wp'] = 11
df.loc[(df.state =='NW') & (df.date == '1995-05-14'), 'wp'] = 12
df.loc[(df.state =='NW') & (df.date == '2000-05-14'), 'wp'] = 13
df.loc[(df.state =='NW') & (df.date == '2005-05-22'), 'wp'] = 14
df.loc[(df.state =='NW') & (df.date == '2010-05-09'), 'wp'] = 15
df.loc[(df.state =='NW') & (df.date == '2012-05-13'), 'wp'] = 16

df.loc[(df.state =='RP') & (df.date == '1991-04-21'), 'wp'] = 12
df.loc[(df.state =='RP') & (df.date == '1996-03-24'), 'wp'] = 13
df.loc[(df.state =='RP') & (df.date == '2001-03-25'), 'wp'] = 14
df.loc[(df.state =='RP') & (df.date == '2006-03-26'), 'wp'] = 15
df.loc[(df.state =='RP') & (df.date == '2011-03-27'), 'wp'] = 16

df.loc[(df.state =='SL') & (df.date == '1990-01-28'), 'wp'] = 10
df.loc[(df.state =='SL') & (df.date == '1994-10-16'), 'wp'] = 11
df.loc[(df.state =='SL') & (df.date == '1999-09-05'), 'wp'] = 12
df.loc[(df.state =='SL') & (df.date == '2004-09-05'), 'wp'] = 13
df.loc[(df.state =='SL') & (df.date == '2009-08-30'), 'wp'] = 14
df.loc[(df.state =='SL') & (df.date == '2012-03-25'), 'wp'] = 15

df.loc[(df.state =='SN') & (df.date == '1990-10-14'), 'wp'] = 1
df.loc[(df.state =='SN') & (df.date == '1994-09-11'), 'wp'] = 2
df.loc[(df.state =='SN') & (df.date == '1999-09-19'), 'wp'] = 3
df.loc[(df.state =='SN') & (df.date == '2004-09-19'), 'wp'] = 4
df.loc[(df.state =='SN') & (df.date == '2009-08-30'), 'wp'] = 5

df.loc[(df.state =='ST') & (df.date == '1990-10-14'), 'wp'] = 1
df.loc[(df.state =='ST') & (df.date == '1994-06-26'), 'wp'] = 2
df.loc[(df.state =='ST') & (df.date == '1998-04-26'), 'wp'] = 3
df.loc[(df.state =='ST') & (df.date == '2002-04-21'), 'wp'] = 4
df.loc[(df.state =='ST') & (df.date == '2006-03-26'), 'wp'] = 5
df.loc[(df.state =='ST') & (df.date == '2011-03-20'), 'wp'] = 6

df.loc[(df.state =='SH') & (df.date == '1992-04-05'), 'wp'] = 13
df.loc[(df.state =='SH') & (df.date == '1996-03-24'), 'wp'] = 14
df.loc[(df.state =='SH') & (df.date == '2000-02-27'), 'wp'] = 15
df.loc[(df.state =='SH') & (df.date == '2005-02-20'), 'wp'] = 16
df.loc[(df.state =='SH') & (df.date == '2009-09-27'), 'wp'] = 17
df.loc[(df.state =='SH') & (df.date == '2012-05-06'), 'wp'] = 18

df.loc[(df.state =='TH') & (df.date == '1990-10-14'), 'wp'] = 1
df.loc[(df.state =='TH') & (df.date == '1994-10-16'), 'wp'] = 2
df.loc[(df.state =='TH') & (df.date == '1999-09-12'), 'wp'] = 3
df.loc[(df.state =='TH') & (df.date == '2004-06-13'), 'wp'] = 4
df.loc[(df.state =='TH') & (df.date == '2009-08-30'), 'wp'] = 5

df['wp'] = df.wp.astype(int)

#add share cdu share
cdu_share = []
for i in range(len(df)):
    if df.loc[i, 'state'] == 'BY':
        #print(df.loc[i, 'state'], df.loc[i, 'date'], df.loc[i, 'results']['CSU']['pct'])
        cdu_share.append(df.loc[i, 'results']['CSU']['pct'])
    else:
        #print(df.loc[i, 'state'], df.loc[i, 'date'], df.loc[i, 'results']['CDU']['pct'])
        cdu_share.append(df.loc[i, 'results']['CDU']['pct'])

df['cdu_share'] = cdu_share

#add share spd share
spd_share = []
for i in range(len(df)):
    #print(df.loc[i, 'state'], df.loc[i, 'date'], df.loc[i, 'results']['SPD']['pct'], i)
    spd_share.append(df.loc[i, 'results']['SPD']['pct'])

df['spd_share'] = spd_share

df.to_pickle('./election_results_expanded.pkl')

print("executed; df exported as pkl")