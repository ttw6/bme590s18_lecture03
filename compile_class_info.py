# Import libraries
import os
import pandas as pd


def main():
    Filenames = collect_csv_files()
    Everyone = cat_data(Filenames)
    read_csv(Everyone)
    write_data(Everyone)


def collect_csv_files():
    import glob
    # Collect all except mlp6
    filenames = glob.glob('*.csv')
    filenames.remove('mlp6.csv')
    if 'everyone.csv' in filenames:     # This breaks code. What is another way to rewrite everyone.csv?
        os.remove('everyone.csv')
    else:
        pass
    return filenames


def cat_data(Filenames):
    ind_data = []  #initialize for dataframe
    for f in Filenames:  # More efficent way to do this?
        df = pd.read_csv(f, delimiter=',', index_col=None, header=None)
        ind_data.append(df)
    everyone = pd.concat(ind_data, ignore_index=True)
    everyone.columns = ['First', 'Last', 'NetID', 'GitHub', 'Teamname']
    everyone = everyone.drop([2])
    everyone.to_csv('everyone.csv', index=False)
    return everyone


def read_csv(Everyone):
    check_no_spaces(Everyone)
    check_camel_case(Everyone)


def check_no_spaces(Everyone):
    for index, row in Everyone.iterrows():
        if ' ' in row[-1]:
            print('Error: Space in Team name.')
            # Refine to ignore first space, remove other spaces, and put in camelcase
        else:
            print(row[-1])
            pass


def check_camel_case(Everyone):
    total_teams = Everyone.drop_duplicates(subset='Teamname')
    camel_count = 0
    for index, row in total_teams.iterrows():
        if row[-1].istitle():  # No uppercase after lowercase
            pass
        else:
            camel_count +=1
    print('\n CamelCase {} out of {} teams.'.format(camel_count, len(total_teams.index)))
    # Debug: Make sure teamname is consistent between team members


def write_data(Everyone):
    # CSV or JSON
    for index, row in Everyone.iterrows():
        name = row[-3]
        row.to_json(name + '.json')
    # Other possible method?
    #name = Everyone['NetID'].to_string(index_names=False)
    #print(name)



if __name__ == "__main__":
    main()
