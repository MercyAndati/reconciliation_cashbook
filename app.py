import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mpesa Data Splitter", layout="wide")

st.title("📂 Monthly Cash Book Splitter")
st.markdown("Select a month (sheet) to extract and split into Mpesa and Non-Mpesa files.")

# Sidebar for file upload
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

uploaded_file = st.sidebar.file_uploader("Upload Cash Book (Excel)", type=['xlsx'], key="file_input")

if uploaded_file:
    # Use ExcelFile to see all sheet names
    xl = pd.ExcelFile(uploaded_file)
    sheet_names = xl.sheet_names
    
    st.sidebar.success(f"Loaded {len(sheet_names)} sheets.")
    
    # 1. Choose the Sheet (Month)
    selected_sheet = st.selectbox("Select the Sheet/Month to process:", sheet_names)
    
    # 2. Load the specific sheet
    # We skip rows to find the headers
    df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)
    
    st.info(f"Currently viewing: **{selected_sheet}**")
    
    # 3. Choose the Particulars Column
    part_col = st.selectbox("Select the 'Particulars' Column:", df.columns, key=f"col_{selected_sheet}")
    
    # 4. Processing Logic
    # Filter for MPESA
    is_mpesa = df[part_col].astype(str).str.contains('MPESA', case=False, na=False)
    df_mpesa = df[is_mpesa]
    df_non_mpesa = df[~is_mpesa]

    # --- Display Results ---
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"📱 Mpesa ({selected_sheet})")
        st.metric("Total Entries", len(df_mpesa))
        st.dataframe(df_mpesa, use_container_width=True)
        
        # Dynamic File Name
        mpesa_name = f"{selected_sheet}-mpesa-entries.csv"
        st.download_button(
            label=f"📥 Download {mpesa_name}",
            data=df_mpesa.to_csv(index=False),
            file_name=mpesa_name,
            mime="text/csv",
            key=f"dl_mpesa_{selected_sheet}"
        )
        
    with col2:
        st.subheader(f"🏦 Non-Mpesa ({selected_sheet})")
        st.metric("Total Entries", len(df_non_mpesa))
        st.dataframe(df_non_mpesa, use_container_width=True)
        
        # Dynamic File Name
        non_mpesa_name = f"{selected_sheet}-non-mpesa-entries.csv"
        st.download_button(
            label=f"📥 Download {non_mpesa_name}",
            data=df_non_mpesa.to_csv(index=False),
            file_name=non_mpesa_name,
            mime="text/csv",
            key=f"dl_non_mpesa_{selected_sheet}"
        )

    # --- Reset Option ---
    st.sidebar.divider()
    if st.sidebar.button("♻️ Refresh / New Cashbook"):
        st.rerun()

else:
    st.warning("Please upload the Cash Book Excel file in the sidebar to start.")