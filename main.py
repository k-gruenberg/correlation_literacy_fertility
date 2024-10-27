# Code written by ChatGPT (27 Oct 2024)
# Prompt:
#   I have 2 CSV files with World Bank data and the header
#     "Country Name","Country Code","Indicator Name","Indicator Code","1960","1961","1962","1963", ..., "2023"
#   Create a Python program plotting literacy rate in % on the x-axis and fertility rate on the y-axis using a
#   Pyplot scatter plot. For each country, I want its dots to be connected. I want each country to be in a
#   different color.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Load the CSV files
    literacy_df = pd.read_csv("API_SE.ADT.LITR.ZS_DS2_en_csv_v2_9672.csv")  # https://data.worldbank.org/indicator/SE.ADT.LITR.ZS
    fertility_df = pd.read_csv("API_SP.DYN.TFRT.IN_DS2_en_csv_v2_10203.csv")  # https://data.worldbank.org/indicator/SP.DYN.TFRT.IN

    # Filter dataframes to retain only rows with relevant indicators
    literacy_df = literacy_df[literacy_df['Indicator Name'] == 'Literacy rate, adult total (% of people ages 15 and above)']
    fertility_df = fertility_df[fertility_df['Indicator Name'] == 'Fertility rate, total (births per woman)']

    # Set the year range (1960 to 2023)
    years = [str(year) for year in range(1960, 2024)]

    # Initialize plot
    plt.figure(figsize=(12, 8))
    plt.title("Literacy Rate vs. Fertility Rate by Country")
    plt.xlabel("Literacy Rate (%)")
    plt.ylabel("Fertility Rate (births per woman)")

    # Iterate over each country and plot connected dots
    for country in literacy_df['Country Name'].unique():
    #for country in [
    #    "Germany", "Turkiye", "Syrian Arab Republic",  # "Poland",
    #    "Iran, Islamic Rep.", "Iraq", "Ukraine",
    #    "Afghanistan", "Romania", "Morocco", "Arab World", "Middle East & North Africa"
    #]:
        # Get literacy and fertility rates for each country
        literacy_rates = literacy_df[literacy_df['Country Name'] == country][years].values.flatten()
        fertility_rates = fertility_df[fertility_df['Country Name'] == country][years].values.flatten()

        # Ensure there are no NaN values by masking them out
        mask = ~pd.isna(literacy_rates) & ~pd.isna(fertility_rates)
        literacy_rates = literacy_rates[mask]
        fertility_rates = fertility_rates[mask]

        if len(literacy_rates) > 0:
            # Plot and connect dots for each country with a unique color
            plt.plot(literacy_rates, fertility_rates, marker='o', linestyle='-', label=country)
        else:
            print(f"[Warning] Not plotting {country} due to lack of data.")

    # Add legend outside the plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
