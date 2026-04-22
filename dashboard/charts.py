import matplotlib.pyplot as plt


def plot_top_gap(df):
    top_gap = df.sort_values(by='gap', ascending=False).head(10)

    fig, ax = plt.subplots()
    ax.barh(top_gap['state'], top_gap['gap'])
    ax.invert_yaxis()
    ax.set_title("Top 10 States by Gap")

    return fig


def plot_state_comparison(state_data):
    fig, ax = plt.subplots()

    ax.bar(['Rural', 'Urban'], [
        state_data['rural'].values[0],
        state_data['urban'].values[0]
    ])

    ax.set_title("Rural vs Urban MPCE")

    return fig


def plot_spending_bar(rural_row, urban_row):
    categories = ['Food', 'Non-Food', 'Education', 'Health', 'Conveyance', 'Services']

    rural_values = [
        rural_row['food_total'].values[0],
        rural_row['nonfood_total'].values[0],
        rural_row['education'].values[0],
        rural_row['health_total'].values[0],
        rural_row['conveyance'].values[0],
        rural_row['services'].values[0]
    ]

    urban_values = [
        urban_row['food_total'].values[0],
        urban_row['nonfood_total'].values[0],
        urban_row['education'].values[0],
        urban_row['health_total'].values[0],
        urban_row['conveyance'].values[0],
        urban_row['services'].values[0]
    ]

    x = range(len(categories))

    fig, ax = plt.subplots()

    ax.bar([i - 0.2 for i in x], rural_values, width=0.4, label='Rural')
    ax.bar([i + 0.2 for i in x], urban_values, width=0.4, label='Urban')

    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45)
    ax.legend()

    return fig


def plot_pie(food, nonfood, title):
    fig, ax = plt.subplots()

    ax.pie(
        [food, nonfood],
        labels=['Food', 'Non-Food'],
        autopct='%1.1f%%'
    )

    ax.set_title(title)

    return fig


def plot_percentage_bar(rural_row, urban_row):
    categories = ['Food', 'Non-Food', 'Education', 'Health', 'Conveyance', 'Services']

    rural_values = [
        rural_row['food_percent'].values[0],
        rural_row['nonfood_percent'].values[0],
        rural_row['education_percent'].values[0],
        rural_row['health_percent'].values[0],
        rural_row['conveyance_percent'].values[0],
        rural_row['services_percent'].values[0]
    ]

    urban_values = [
        urban_row['food_percent'].values[0],
        urban_row['nonfood_percent'].values[0],
        urban_row['education_percent'].values[0],
        urban_row['health_percent'].values[0],
        urban_row['conveyance_percent'].values[0],
        urban_row['services_percent'].values[0]
    ]

    x = range(len(categories))

    fig, ax = plt.subplots()

    ax.bar([i - 0.2 for i in x], rural_values, width=0.4, label='Rural')
    ax.bar([i + 0.2 for i in x], urban_values, width=0.4, label='Urban')

    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45)
    ax.legend()

    return fig