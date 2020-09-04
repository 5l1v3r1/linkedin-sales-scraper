from LinkedinScraper import LinkedinScraper

import pandas as pd


def main():
    scraper = LinkedinScraper('New York Community Bank', 1, [], [], guess_email=True, link_scrape=True)
    scraper.run()

    # SCRAPE RESULTS SALESFORCE DROP SCRIPT
    # salesforce_accounts = pd.read_csv('testing/salesforce_accounts.csv')
    # my_accounts = pd.read_csv('testing/accounts.csv')
    # print(my_accounts, '=' * 100, sep='\n')
    #
    # accounts = my_accounts[['First Name', 'Last Name', 'Company']]
    # salesforce = salesforce_accounts[['First Name', 'Last Name', 'Company']]
    #
    # merged = accounts.merge(salesforce, how='left', indicator=True).query('_merge == "both"').drop(['_merge'], axis=1)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(merged)
    #     print(len(merged))
    # indices = merged.index
    # my_accounts = my_accounts.drop(index=indices)
    # print(my_accounts)
    #
    # my_accounts.to_csv('testing/accounts_updated.csv')


if __name__ == '__main__':
    main()
