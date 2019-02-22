import fmna.data_loader as dl

france = ['PGP', 'MRK', 'HSB', 'MCNV', 'MC', 'FP', 'OR', 'LLY', 'SAN', 'SANNV', 'DGE', 'AIR', 'CATR', 'VALE3', 'CDI', 'GNE', 'SLB', 'BNP', 'SAF', 'RMS', 'CS', 'KER', 'CSNV', 'AI', 'DG', 'BN', 'DGNV', 'EL', 'ORA', 'RI', 'SU', 'SUNV', 'ACA', 'ENGI', 'VIV', 'DSY', 'GLE', 'LHN', 'HO', 'HONV', 'SGO', 'RNO', 'CAP', 'UG', 'ML', 'MLNV', 'KN', 'LR', 'CNP', 'SW', 'CA', 'EN', 'PUB', 'AM', 'BOLNV', 'BOL', 'STM', 'AC', 'IAM', 'VIE', 'AMUN', 'IPN', 'FTI', 'GFC', 'LI', 'ALO', 'DIM', 'FGR', 'BVI', 'SESG', 'SEV', 'TEP', 'SCR', 'ATO', 'BIM', 'UBI', 'EDEN', 'ILD', 'ERF', 'COV', 'FR', 'AKE', 'DEC', 'GET', 'WLN', 'ORP', 'SK', 'EO', 'ERFNV', 'DECNV', 'ICAD', 'ODET', 'RCO', 'RF', 'MF', 'RE', 'AF', 'BB', 'RUICOE']

# excluded: FIVE, TRNF, AVAZ, GAZT, RAVN
russia = ['SBER', 'ROSN', 'LKOH', 'GAZP', 'NVTK', 'GMKN', 'TATN', 'SIBN', 'SNGS', 'NLMK', 'CHMF', 'PLZL', 'ALRS', 'YNDX', 'MAGN', 'MTSS', 'VTBR', 'RUAL', 'MGNT', 'IRAO', 'MFON', 'UNAC', 'POLY', 'BANE', 'ENPL', 'PHOR', 'URKA', 'PIKK', 'HYDR', 'FEES', 'MOEX', 'RTKM', 'RSTI', 'VSMO', 'AKRN', 'KZOS', 'RNFT', 'UPRO', 'MGTS', 'CBOM', 'NMTP', 'NKNC', 'AGRO', 'AFLT', 'LNTA', 'RASP', 'ROSB', 'AFKS', 'MSNG', 'RGSS', 'MVID', 'IRGZ', 'TRCN', 'DSKY', 'LSRG', 'QIWI', 'CHEP', 'UWGN', 'SFIN', 'LSNG', 'ALNU', 'IRKT', 'TRMK', 'GCHE', 'MRKK', 'MTLR', 'MFGS', 'AVAN', 'APTK', 'PRTK', 'KMAZ', 'ENRU', 'OGKB', 'TGKA', 'MSRS', 'UCSS', 'MRKP', 'OPIN', 'UTAR', 'DVEC', 'KAZT']

usa = ['MSFT', 'AAPL', 'AMZN', 'GOOGL', 'GOOG', 'BRK-A', 'FB', 'BABA', 'JNJ', 'JPM', 'XOM', 'V', 'WMT', 'BAC', 'RDS-A', 'UNH', 'PFE', 'PG', 'BA', 'CVX', 'WFC', 'MA', 'VZ', 'INTC', 'T', 'CHL', 'CSCO', 'KO', 'HD', 'NVS', 'MRK', 'TM', 'PTR', 'TSM', 'ORCL', 'CMCSA', 'HSBC', 'DIS', 'PEP', 'NFLX', 'C', 'BUD', 'UL', 'TOT', 'UN', 'BP', 'MCD', 'NKE', 'ABT', 'LLY', 'ADBE', 'PM', 'SAP', 'IBM', 'ABBV', 'BBL', 'BHP', 'CRM', 'MDT', 'UNP', 'DWDP', 'AMGN', 'MMM', 'AVGO', 'HON', 'RY', 'PYPL', 'SNY', 'UTX', 'ACN', 'TD', 'SNP', 'GSK', 'TXN', 'TMO', 'ITUB', 'PBR', 'RIO', 'AZN', 'DEO', 'NVO', 'UPS', 'FOX', 'FOXA', 'MO', 'COST', 'NVDA', 'LFC', 'AXP', 'NEE', 'SBUX', 'BKNG', 'GILD', 'GE']

prices = dl.load_data(dl.add_suffix(france, 'PA'), '20170101', '20180101')
#prices = dl.load_data(usa, '20170101', '20180101')

for date, prices in prices.items():
    print('%s, %s' % (date, prices))