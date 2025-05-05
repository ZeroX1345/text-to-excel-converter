import re
import csv
import streamlit as st

def split_text_to_columns(raw_text):
    """
    Splits raw text into section numbers and corresponding text.
    :param raw_text: str: The input text containing section numbers and text.
    :return: list: A list of tuples with section numbers and text.
    """
    pattern = r"(\d+(\.\d+)*)\s+(.*)"  # Regex to match section numbers and text
    lines = raw_text.splitlines()
    result = []

    for line in lines:
        match = re.match(pattern, line)
        if match:
            section_number = match.group(1)
            section_text = match.group(3)
            result.append((section_number, section_text))
    
    return result

def save_to_csv(data, output_file):
    """
    Saves the list of tuples to a CSV file.
    :param data: list: A list of tuples (section_number, section_text).
    :param output_file: str: The name of the output CSV file.
    """
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Section Number", "Text"])
        writer.writerows(data)

# Streamlit App
st.title("Text to Excel Converter")
st.write("Paste your raw text below to convert it into a two-column format (Section Number and Text).")

raw_text = st.text_area("Input Text", height=300, placeholder="Paste your raw text here...")
if st.button("Convert"):
    if raw_text.strip():
        processed_data = split_text_to_columns(raw_text)
        if processed_data:
            # Save data to CSV
            output_file = "sections_to_excel.csv"
            save_to_csv(processed_data, output_file)

            # Display data in Streamlit
            st.success("Conversion successful! Download your CSV file below.")
            st.download_button(
                label="Download CSV",
                data=open(output_file, "rb"),
                file_name="sections_to_excel.csv",
                mime="text/csv"
            )
        else:
            st.warning("No valid data found in the input text!")
    else:
        st.warning("Please paste some text before converting!")