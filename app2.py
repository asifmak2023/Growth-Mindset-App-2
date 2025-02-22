import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
EXCEL_FILE = "growth_mindset_data.xlsx"

def display_quotes():
    """Display growth mindset quotes from the Excel file."""
    quotes_df = pd.read_excel(EXCEL_FILE, sheet_name="Quotes")
    st.write("### Growth Mindset Quotes")
    for index, row in quotes_df.iterrows():
        st.write(f'**"{row["Quote"]}"** - *{row["Author"]}*')

def display_goals():
    """Display user goals and progress."""
    goals_df = pd.read_excel(EXCEL_FILE, sheet_name="Goals")
    st.write("### Your Goals")
    st.write(goals_df)

def add_goal():
    """Allow the user to add a new goal."""
    st.write("### Add a New Goal")
    goal = st.text_input("Enter your new goal:")
    progress = st.slider("Enter your current progress (0-100):", 0, 100)
    
    if st.button("Add Goal"):
        if goal:
            # Load the existing goals
            goals_df = pd.read_excel(EXCEL_FILE, sheet_name="Goals")
            
            # Add the new goal
            new_goal = pd.DataFrame({"Goal": [goal], "Progress (%)": [progress]})
            goals_df = pd.concat([goals_df, new_goal], ignore_index=True)
            
            # Save back to the Excel file
            with pd.ExcelWriter(EXCEL_FILE, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
                goals_df.to_excel(writer, sheet_name="Goals", index=False)
            
            st.success("Goal added successfully!")
        else:
            st.error("Please enter a goal.")

def visualize_progress():
    """Visualize progress using a bar chart."""
    goals_df = pd.read_excel(EXCEL_FILE, sheet_name="Goals")
    
    st.write("### Your Progress Towards Goals")
    fig, ax = plt.subplots()
    ax.bar(goals_df["Goal"], goals_df["Progress (%)"], color="skyblue")
    ax.set_xlabel("Goals")
    ax.set_ylabel("Progress (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

def main():
    """Main function to run the app."""
    st.title("Growth Mindset App 🌱")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = ["Home", "Quotes", "Goals", "Add Goal", "Progress Chart"]
    choice = st.sidebar.radio("Choose an option:", options)
    
    if choice == "Home":
        st.write("Welcome to the Growth Mindset App! Use the sidebar to navigate.")
    elif choice == "Quotes":
        display_quotes()
    elif choice == "Goals":
        display_goals()
    elif choice == "Add Goal":
        add_goal()
    elif choice == "Progress Chart":
        visualize_progress()

if __name__ == "__main__":
    main()