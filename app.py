import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch  # <- make sure this is imported
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# --- Page Setup ---
st.set_page_config(layout='wide')
st.title("🚢 Titanic Survival Data Dashboard")

# --- Load & Clean Dataset ---
df = pd.read_csv("train.csv")
df.drop(['Cabin', 'Ticket'], axis=1, inplace=True)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df.dropna(inplace=True)

# Add readable labels for plotting
df['Survived_raw'] = df['Survived']
df['Pclass_raw'] = df['Pclass']
df['Survived_label'] = df['Survived'].map({0: 'No', 1: 'Yes'})
df['Pclass_label'] = df['Pclass'].map({1: '1st', 2: '2nd', 3: '3rd'})

# --- Model Training ---
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]
y = df["Survived"]
models = {
    "Logistic Regression": LogisticRegression(max_iter=200).fit(X, y),
    "Decision Tree": DecisionTreeClassifier().fit(X, y),
    "Random Forest": RandomForestClassifier().fit(X, y)
}

# --- Layout ---
main_col, side_col = st.columns([4, 1])

with main_col:
    # tab1, tab2, tab3, tab4 = st.tabs([
    #     "📈 Data Insights", "🔍 Filters & Charts", "🔮 Prediction", "📚 Data Dictionary"
    # ])
    tab0, tab1, tab2, tab3, tab4 = st.tabs([
        "🏠 Home", "📈 Data Insights", "🔍 Filters & Charts", "🔮 Prediction", "📚 Data Dictionary"
    ])
    
    with tab0:
        st.header("🚢 Welcome to the Titanic Survival Dashboard")
        
        st.markdown("""
        This interactive dashboard explores survival data from the famous Titanic disaster.  
        The dataset used for analysis is the `train.csv` file from the Kaggle Titanic competition:
        
        👉 [Kaggle Titanic Dataset Overview](https://www.kaggle.com/competitions/titanic/overview)
    
        ### 🔍 Data Preprocessing
        - Only rows with **non-null values** for the `Age` and `Embarked` columns are used to simplify analysis.
        - Categorical variables (like Sex and Pclass) are encoded for modeling purposes.
    
        ### 🧭 Tab Guide
    
        - **📈 Data Insights**: Get an overview of the dataset with statistics, distributions, and correlations.
        - **🔍 Filters & Charts**: Use filters to explore survival trends by gender, class, and age dynamically.
        - **🔮 Prediction**: Simulate survival prediction based on inputs using various machine learning models.
        - **📚 Data Dictionary**: Understand the variables used in the dataset and what they mean.
    
        ---  
    
        We hope this dashboard helps you uncover interesting insights.  
        Enjoy your journey!  
        **— Nguyen Chien Thang**
        """)

    # --- TAB 1: Data Insights ---
    # with tab1:
    #     st.header("🧠 Dataset Overview and Correlations")

    #     st.subheader("📋 Descriptive Statistics")
    #     desc_stats = {
    #         "Total Passengers": df.shape[0],
    #         "Average Age": round(df['Age'].mean(), 2),
    #         "Average Fare": round(df['Fare'].mean(), 2),
    #         "Male Passengers": df[df['Sex'] == 0].shape[0],
    #         "Female Passengers": df[df['Sex'] == 1].shape[0],
    #         "1st Class Passengers": df[df['Pclass'] == 1].shape[0],
    #         "2nd Class Passengers": df[df['Pclass'] == 2].shape[0],
    #         "3rd Class Passengers": df[df['Pclass'] == 3].shape[0]
    #     }
    #     st.dataframe(pd.DataFrame.from_dict(desc_stats, orient='index', columns=["Value"]))
# --- TAB 1: Data Insights ---
    with tab1:
        st.header("🧠 Dataset Overview and Correlations")
    
        # Summary statistics
        st.subheader("📋 Descriptive Statistics")
        desc_stats = {
            "Total Passengers": df.shape[0],
            "Average Age": round(df['Age'].mean(), 2),
            "Average Fare": round(df['Fare'].mean(), 2),
            "Male Passengers": df[df['Sex'] == 0].shape[0],
            "Female Passengers": df[df['Sex'] == 1].shape[0],
            "1st Class Passengers": df[df['Pclass'] == 1].shape[0],
            "2nd Class Passengers": df[df['Pclass'] == 2].shape[0],
            "3rd Class Passengers": df[df['Pclass'] == 3].shape[0]
        }
        st.dataframe(pd.DataFrame.from_dict(desc_stats, orient='index', columns=["Value"]))
    
        # Row 1: Age and Fare Distribution
        st.subheader("📊 Distributions")
        col1, col2 = st.columns(2)
    
        with col1:
            fig_age, ax_age = plt.subplots()
            sns.histplot(df['Age'], bins=30, kde=True, ax=ax_age)
            ax_age.set_title("Age Distribution")
            st.pyplot(fig_age)
    
        with col2:
            fig_fare, ax_fare = plt.subplots()
            sns.histplot(np.log1p(df['Fare']), bins=30, kde=True, ax=ax_fare)
            ax_fare.set_title("Log Fare Distribution")
            st.pyplot(fig_fare)
    
        # Row 2: Scatterplot and Correlation Heatmap
        st.subheader("📈 Relationships and Correlations")
        col3, col4 = st.columns(2)
    
        with col3:
            fig_scatter, ax_scatter = plt.subplots()
            sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived_label', ax=ax_scatter)
            ax_scatter.set_title("Age vs Fare (Colored by Survival)")
            st.pyplot(fig_scatter)
    
        with col4:
            corr_matrix = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Survived"]].corr()
            fig_corr, ax_corr = plt.subplots()
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax_corr)
            ax_corr.set_title("Feature Correlation Heatmap")
            st.pyplot(fig_corr)

    # --- TAB 2: Filters & Charts ---
    with tab2:
        st.header("🎛️ Interactive Filters")

        gender = st.multiselect("Select Gender", [0, 1], format_func=lambda x: 'Male' if x == 0 else 'Female', default=[0, 1])
        pclass = st.multiselect("Select Passenger Class", [1, 2, 3], default=[1, 2, 3])
        age_range = st.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (0, 80))

        filtered_df = df[
            (df['Sex'].isin(gender)) &
            (df['Pclass'].isin(pclass)) &
            (df['Age'].between(age_range[0], age_range[1]))
        ]

        st.subheader("🔍 Filtered Data Preview")
        # st.dataframe(filtered_df.head())
        columns_to_hide = filtered_df.columns[[10, 11]]
        st.dataframe(filtered_df.drop(columns=columns_to_hide).head())
        
        st.metric("Filtered Survival Rate", f"{filtered_df['Survived'].mean():.2%}")

        st.subheader("📊 Filtered Survival Charts")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**✅ Survivors vs Non-Survivors (Filtered)**")
            fig1, ax1 = plt.subplots()
            sns.countplot(data=filtered_df, x='Survived', hue='Survived', palette={0: "#1f77b4", 1: "#ff7f0e"}, ax=ax1)
            ax1.set_title("Survival Count")
            ax1.set_xlabel("Survival Status")
            ax1.set_ylabel("Passenger Count")
            ax1.set_xticks([0, 1])
            ax1.set_xticklabels(['No', 'Yes'])
            ax1.legend(title="Survived", labels=["No", "Yes"])
            st.pyplot(fig1)

        with col2:
            st.markdown("**👩‍🦰 Survival by Gender (Filtered)**")
            fig2, ax2 = plt.subplots()
            sns.countplot(data=filtered_df, x='Sex', hue='Survived', palette={0: "#1f77b4", 1: "#ff7f0e"}, ax=ax2)
            ax2.set_title("Survival by Gender")
            ax2.set_xlabel("Gender")
            ax2.set_ylabel("Passenger Count")
            ax2.set_xticks([0, 1])
            ax2.set_xticklabels(['Male', 'Female'])
            ax2.legend(title="Survived", labels=["No", "Yes"])
            st.pyplot(fig2)
        with col3:
            st.markdown("**🎟️ Survival by Passenger Class (Filtered)**")
            fig3, ax3 = plt.subplots()
            sns.countplot(data=filtered_df, x='Pclass', hue='Survived', order=[1, 2, 3], palette={0: "#1f77b4", 1: "#ff7f0e"}, ax=ax3)
            ax3.set_title("Survival by Passenger Class")
            ax3.set_xlabel("Passenger Class")
            ax3.set_ylabel("Passenger Count")
            ax3.set_xticklabels(['1st Class', '2nd Class', '3rd Class'])
            ax3.legend(title="Survived", labels=["No", "Yes"])
            st.pyplot(fig3)


    # --- TAB 3: Prediction ---
    with tab3:
        st.header("🔮 Survival Prediction")

        model_choice = st.selectbox("Which model do you want to use?", list(models.keys()))

        st.markdown("### Please fill in the following information:")
        user_pclass = st.selectbox("Pclass", [1, 2, 3])
        user_sex = st.selectbox("Sex", ["Male", "Female"])
        user_age = st.slider("Age", 0, 80, 25)
        user_sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
        user_parch = st.number_input("Parents/Children Aboard (Parch)", 0, 10, 0)
        user_fare = st.number_input("Fare", 0.0, 600.0, 32.0)

        input_data = pd.DataFrame([{
            "Pclass": user_pclass,
            "Sex": 0 if user_sex == "Male" else 1,
            "Age": user_age,
            "SibSp": user_sibsp,
            "Parch": user_parch,
            "Fare": user_fare
        }])

        if st.button("🚀 Predict"):
            model = models[model_choice]
            prediction = model.predict(input_data)[0]
            result = "🎉 Survived!" if prediction == 1 else "💀 Not Survived"
            accuracy = model.score(X, y)
            st.success(f"Prediction Result: {result}")
            st.info(f"Model Training Accuracy (on full dataset): {accuracy:.2f}")

    # --- TAB 4: Data Dictionary ---
    with tab4:
        st.header("📚 Titanic Dataset Dictionary")
        data_dict = {
            "Survived": ["Survived", "0 = No, 1 = Yes"],
            "Pclass": ["Ticket class", "1 = 1st, 2 = 2nd, 3 = 3rd"],
            "Sex": ["Sex", "0 = Male, 1 = Female"],
            "Age": ["Age in years", ""],
            "Sibsp": ["# of siblings / spouses aboard the Titanic", ""],
            "Parch": ["# of parents / children aboard the Titanic", ""],
            "Ticket": ["Ticket number", ""],
            "Fare": ["Passenger fare", ""],
            "Cabin": ["Cabin number", ""],
            "Embarked": ["Port of Embarkation", "C = Cherbourg, Q = Queenstown, S = Southampton"]
        }
        dict_df = pd.DataFrame.from_dict(data_dict, orient='index', columns=["Definition", "Key"])
        dict_df.index.name = "Variable"
        st.dataframe(dict_df)

# --- RIGHT COLUMN: Static Image ---
with side_col:
    try:
        image = Image.open("IMG_9989.JPG")
        st.image(image, caption="Nguyen Chien Thang", use_container_width=True)
    except FileNotFoundError:
        st.warning("Profile image not found.")
