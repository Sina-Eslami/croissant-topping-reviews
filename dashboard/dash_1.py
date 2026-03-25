import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from matplotlib.ticker import FormatStrFormatter

df = pd.read_csv('data/anonymized_output.csv')
df['dates'] = pd.to_datetime(df['dates'])

st.set_page_config(layout="wide")

culinary_dict = {
    'cheese': 118, 'butter': 80, 'jam': 57, 'cream': 56, 'chocolate': 51,
    'strawberries': 41, 'egg': 31, 'sprinkles': 26, 'honey': 25,
    'strawberry': 23, 'sugar': 21, 'salmon': 20, 'brie': 16, 'chicken': 15,
    'salt': 14, 'peanut': 13, 'lemon': 12, 'rocket': 10,
    'sauce': 10, 'pepper': 10, 'spread': 10, 'tomato': 10, 'ham': 9,
    'raspberries': 9, 'avocado': 9, 'paste': 8, 'nuts': 8, 'walnuts': 8,
    'lettuce': 8, 'pesto': 7, 'banana': 7, 'pistachio': 7, 'bacon': 7,
    'mascarpone': 7, 'chives': 7, 'onion': 7, 'lavender': 6, 'sausage': 6,
    'raspberry': 6, 'syrup': 6, 'eggs': 6, 'curd': 6, 'mustard': 6,
    'mayonnaise': 5, 'cucumber': 5, 'salad': 5,
    'prosciutto': 4, 'fig': 4, 'pineapple': 4, 'caramel': 4,
    'vanilla': 4, 'mozzarella': 4, 'dill': 4, 'beef': 4, 'pistachios': 4,
    'arugula': 3, 'chili': 3, 'mayo': 3,
    'hazelnut': 3, 'roll': 3, 'custard': 3, 'basil': 3, 'fruit': 3,
    'tomatoes': 3, 'apple': 3,
    'paashagel': 2, 'marshmallow': 2, 'compote': 2, 'pecans': 2,
    'parmesan': 2, 'cucumbers': 2, 'blueberries': 2, 'grapes': 2, 'onions': 2,
    'buttercream': 2, 'milk': 2, 'frikandel': 2,
    'garlic': 2, 'cherry': 2, 'figs': 2, 'mint': 2, 'seed': 2,
    'croquette': 2, 'carpaccio': 2, 'dressing': 2, 'salami': 2, 'sesame': 2,
    'apricots': 2, 'lime': 2, 'iceberg': 2, 'cherries': 2,
    'feta': 1, 'hummus': 1, 'blackberries': 1,
    'sardines': 1, 'oil': 1, 'beurre': 1,
    'spices': 1, 'quark': 1, 'pumpkin': 1, 'almond': 1,
    'maple': 1, 'filet': 1, 'spice': 1, 'rusk': 1,
    'rusks': 1, 'guacamole': 1, 'guava': 1, 'chutney': 1, 'moccassant': 1,
    'cinnamon': 1, 'nutella': 1, 'passionfruit': 1, 'fudge': 1,
    'tiramisu': 1, 'cocoa': 1,
    'pudding': 1, 'peanuts': 1, 'crackling': 1, 'chia': 1,
    'shumai': 1, 'paprika': 1, 'tuna': 1, 'duck': 1,
    'liver': 1, 'fenugreek': 1, 'capers': 1, 'vinegar': 1,
    'dates': 1, 'truffle': 1, 'maio': 1, 'olives': 1, 'cod': 1, 'praline': 1,
    'crompouce': 1, 'bavette': 1, 'seeds': 1, 'americain': 1, 'hazelnuts': 1,
    'poutine': 1, 'lotus': 1, 'speculaas': 1,
    'creme': 1, 'cumin': 1, 'majo': 1, 'thyme': 1, 'parma': 1,
    'matcha': 1, 'cheeses': 1, 'vegetable': 1,
    'pear': 1, 'anise': 1, 'frangipane': 1, 'dairy': 1, 'shawarma': 1,
    'marshmallows': 1, 'nut': 1, 'soufflé': 1,
    'spinach': 1, 'ragout': 1,
    'guanciale': 1, 'sausages': 1, 'speculoos': 1,
    'camembert': 1, 'prawns': 1, 'crab': 1
}

ALL_ITEMS = culinary_dict.keys()


def visualize(list):
    df_meal = df.copy()

    df_meal = df_meal[df_meal['dates'].dt.hour > 7]
    group1 = list
    # group1 = ['almond', 'chia', 'hazelnut', 'hazelnuts', 'nut', 'nuts', 'peanut', 'peanuts', 'pecans', 'pine', 'pistachio', 'pistachios', 'seed', 'seeds', 'sesame', 'walnuts',]
    # group2 = ['jam', 'apple', 'apricots', 'banana', 'blackberries', 'blueberries', 'cherries', 'cherry', 'compote', 'dates', 'fig', 'figs', 'fruit', 'grapes', 'guava', 'lemon', 'lime', 'passionfruit', 'pear', 'pineapple', 'raspberries', 'raspberry', 'strawberries', 'strawberry', 'tomato', 'tomatoes']
    # group2 = ['coffee', 'tea', 'americano', 'matcha', 'tea', 'milk', 'juice']
    df_meal['group1'] = df_meal['comments'].apply(
        lambda x: 1 if any(item in str(x).lower() for item in group1) else 0)
    group1_hourly = df_meal.groupby(df_meal['dates'].dt.hour)['group1'].mean()

    m1, b1 = np.polyfit(group1_hourly.index.to_numpy(),
                        group1_hourly.values, 1)
    x_line1 = [5, 23]
    y_line1 = [m1*5+b1, m1*23+b1]

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=group1_hourly.index, y=group1_hourly.values)
    sns.lineplot(x=x_line1, y=y_line1, color='green', linewidth=3, alpha=0.5)

    plt.title('Hourly Trends of Your Chosen Toppings!')
    plt.xlabel('Hour of Day')
    plt.ylabel('Proportion of the CMs')
    plt.xlim(0, 24)
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.show()
    fig = plt
    text = f'The correlation of first group hourly proportion with hour of day is {np.corrcoef(group1_hourly.index, group1_hourly.values)[0,1].round(3)}.'
    return fig, text


dash_intro = """
This dashboard shows how croissant topping preferences vary across the hours of the day. 
It is designed to help identify daily taste patterns and reveal when specific topping groups are mentioned more often. Enjoy it!

Detailed analysis:
- [GitHub repository](https://github.com/Sina-Eslami/croissant-topping-reviews)
- [LinkedIn](https://www.linkedin.com/in/siina-eslami/)
"""

st.title('Croissant Favorite Topping by Dutch People', text_alignment='center')
st.markdown(dash_intro)

if "selected_items" not in st.session_state:
    st.session_state.selected_items = []


def add_item(item):
    if item not in st.session_state.selected_items:
        st.session_state.selected_items.append(item)
    st.session_state[f"add_{item}"] = False
    st.session_state[f"keep_{item}"] = True


def remove_item(item):
    if item in st.session_state.selected_items:
        st.session_state.selected_items.remove(item)
    st.session_state.pop(f"keep_{item}", None)


left_col, right_col = st.columns([1, 1])

with right_col:
    avail_col, selected_col = st.columns([1, 1], gap="medium")

    with avail_col:
        st.subheader("Available items")
        with st.container(border=True):
            available_items = [
                item for item in ALL_ITEMS
                if item not in st.session_state.selected_items
            ]

            for i in range(0, len(available_items), 2):
                col1, col2 = st.columns(2)

                with col1:
                    item = available_items[i]
                    st.checkbox(
                        item,
                        key=f"add_{item}",
                        on_change=add_item,
                        args=(item,)
                    )

                if i + 1 < len(available_items):
                    with col2:
                        item = available_items[i + 1]
                        st.checkbox(
                            item,
                            key=f"add_{item}",
                            on_change=add_item,
                            args=(item,)
                        )

    with selected_col:
        st.subheader("Selected items")
        with st.container(border=True):
            selected_items = st.session_state.selected_items.copy()

            if not selected_items:
                st.write("No items selected yet.")
            else:
                for i in range(0, len(selected_items), 2):
                    col1, col2 = st.columns(2)

                    with col1:
                        item = selected_items[i]
                        if f"keep_{item}" not in st.session_state:
                            st.session_state[f"keep_{item}"] = True

                        st.checkbox(item, key=f"keep_{item}")

                        if not st.session_state[f"keep_{item}"]:
                            remove_item(item)
                            st.rerun()

                    if i + 1 < len(selected_items):
                        with col2:
                            item = selected_items[i + 1]
                            if f"keep_{item}" not in st.session_state:
                                st.session_state[f"keep_{item}"] = True

                            st.checkbox(item, key=f"keep_{item}")

                            if not st.session_state[f"keep_{item}"]:
                                remove_item(item)
                                st.rerun()

with left_col:
    st.subheader("Hourly Trend of Your Chosen Toppings!")

    selected = st.session_state.selected_items

    if selected:
        fig, text = visualize(selected)
        st.pyplot(fig)
        st.write(text)
    else:
        st.info("Choose one or more from the available items.")
