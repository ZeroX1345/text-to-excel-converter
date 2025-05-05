import streamlit as st
import pandas as pd
import re

# Streamlit App Title
st.title("Section Number Splitter")

# Description
st.markdown("""
Paste your raw text with section numbers and corresponding text below. 
The app will split the section numbers into one column and the text into another.
You can then download the processed data as a CSV file.
""")

# Text Input
raw_text = st.text_area("Paste your text here:", height=300, placeholder="e.g., 6.1 This is a sample text")

# Process the text when the button is clicked
if st.button("Process Text"):

    # Validate input
    if not raw_text.strip():
        st.warning("Please paste some text to process.")
    else:
        # Split the input text into lines
        lines = raw_text.splitlines()
        
        # Extract section numbers and text using regex
        data = []
        for line in lines:
            match = re.match(r"^(\d+(\.\d+)*)\s+(.*)", line.strip())
            if match:
                section_number = match.group(1)
                text = match.group(3)
                data.append({"Section Number": section_number, "Text": text})
            else:
                # Handle lines that don't match the expected format
                data.append({"Section Number": "", "Text": line.strip()})
        
        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Display the DataFrame
        st.write("Processed Data:")
        st.dataframe(df, use_container_width=True)

        # Provide download option
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="processed_text.csv",
            mime="text/csv",
        )
